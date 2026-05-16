import json
import math
from pathlib import Path
import re
# # from nltk import word_tokenize
# # from nltk.tokenize import word_tokenize
#nltk.download('punkt') # to split text into individual sentences or words
#nltk.download('stopwords') # download Stopping Words
#nltk.download('wordnet') # for stemming
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer #for stemming
from collections import defaultdict, Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

#-------------------------------------------------------------------------------------------

# corpus = collection of documents
def read_corpus():
    CORPUS_PATH = Path("data/sample_docs/")
    corpus = {}
    for file in CORPUS_PATH.glob('*.txt'):
        content = file.read_text(encoding='utf-8')
        corpus[file.name.removesuffix('.txt')] = content
    return corpus

#corpus = {"the-jungle-book" : "In The Morning Mougly", "file2": "content"}
#inverted_index = {'play': {'aliace':2, 'aladdin':5}}

def create_standard_inverted_index(corpus: dict):
    # Using a nested defaultdict: { term: { doc_id: count } }
    inverted_index = defaultdict(lambda: defaultdict(int))

    for file_name, file_content in corpus.items():
        # 1. Clean text: remove punctuation and lowercase
        clean_text = re.sub(r'[^\w\s]', '', file_content).lower()
        tokens = clean_text.split()
        
        # 2. Filter out stop words and apply stemming
        stems = [ps.stem(token) for token in tokens if token not in stop_words]
        
        # 3. Count frequencies of each stem in the CURRENT document
        # Counter(['apple', 'apple', 'orange']) -> {'apple': 2, 'orange': 1}
        term_counts = Counter(stems)
        
        # 4. Populate the inverted index
        # stem: {
        #   file_name: count      
        # }
        for stem, count in term_counts.items():
            inverted_index[stem][file_name] = count
            
    # Convert defaultdict back to a standard dict for clean printing/json compatibility
    return {term: dict(docs) for term, docs in inverted_index.items()}

index = create_standard_inverted_index(read_corpus())
# print(json.dumps(index, indent=2))

def normalize_text(query: str) -> list[str]:
    # 1. Clean text: remove punctuation and lowercase
    clean_text = re.sub(r'[^\w\s]', '', query).lower()
    tokens = clean_text.split()
        
    # 2. Filter out stop words and apply stemming
    stems = [ps.stem(token) for token in tokens if token not in stop_words]
    
    #return list(set(stems))
    return list(dict.fromkeys(stems))

def tf_idf(inverted_index : dict[str: dict[str:int]], query : str) -> dict:
    normalized_query = normalize_text(query)
    # scores = {word: inverted_index.get(word) for word in normalized_query}
    scores = {}
    n = len(inverted_index)
    
    for term in normalized_query:
        postings_list : dict = inverted_index.get(term)
        if(postings_list):
            tfidf_postings = {}
            
            df = len(postings_list)
            idf = math.log10(n / df)

            for doc, tf in postings_list.items():
                weight = 1 + math.log10(tf)
                tfidf = weight * idf
                tfidf_postings[doc] = tfidf
            scores[term] = tfidf_postings
    return scores
    
# score = { 'term1': {doc1_score : 123, doc2_score: 12,....}, 'term2': {doc1_score : 0, doc2_score: 22,....} }


#-------------------------------------------------------------------------------------------

# 1. Define your documents and your query
query = ["Winnie The Pooh Eats Honey with the winnies"]

# 2. Initialize the TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# 3. Fit and transform the documents and the query
doc = read_corpus()
doc_term_matrix = vectorizer.fit_transform(list(doc.values()))
query_term_matrix = vectorizer.transform(query)

# 4. Compute Cosine Similarity
scores = cosine_similarity(query_term_matrix, doc_term_matrix).flatten()

# 5. Rank the documents
doc_names = list(doc.keys())
ranked_indices = sorted(zip(doc_names, scores), key=lambda x: x[1], reverse=True)

for name, score in ranked_indices:
    print(f"{name} Score: {score:.4f}")

#-------------------------------------------------------------------------------------------