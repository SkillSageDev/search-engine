import time
import requests
import re
from pathlib import Path

url = "https://www.gutenberg.org/ebooks/{id}.txt.utf-8"
api = "https://gutendex.com/books"
path = "data/sample_data"

target_txt_files_id = {
    67098: "Winnie-the-Pooh",
    2701: "Moby Dick; Or, The Whale",
    1661: "The Adventures of Sherlock Holmes",
    11: "Alice's Adventures in Wonderland",
    10148: "The Merry Adventures of Robin Hood",
    236: "The Jungle Book",
    78: "Tarzan of the Apes",
    7074: "Beauty and the Beast",
    20916: "Aladdin",
    16: "Peter Pan",
    2591: "Grimms' Fairy Tales",
}


def get_data_descriptions():
    start_time = time.perf_counter()

    ids = list(target_txt_files_id.keys())
    ids_string = ",".join(map(str, ids))

    response = requests.get(api, params={"ids": ids_string})

    if response.status_code == 200:
        books = response.json()["results"]
        for book in books:
            download_book(book["id"], book["title"])

    else:
        print(f"data not found: {response.status_code}")
        print(response.text)

    end_time = time.perf_counter()
    print(f"downloaded in: {(end_time - start_time):.4f}s")


def download_book(id, title):
    title = slugify(title)
    file = Path(f"{path}/{title}.txt")

    if file.exists():
        print(f"file already exists: {title}")
        return

    response = requests.get(url.format(id=id))

    if response.status_code == 200:
        print(f"creating a new file: {title}.txt")
        file.parent.mkdir(exist_ok=True)

        with open(file, "w") as f:
            f.write(response.text)
    else:
        print(f"Couldn't find book id {id}: {response.status_code}")


def slugify(title):
    return "-".join(re.sub(r"[^a-zA-Z0-9- ]", "", title).split()).lower()


try:
    get_data_descriptions()
except KeyboardInterrupt:
    print("\n\n[!] Execution interrupted by user. Closing safely...")
    exit(0)
