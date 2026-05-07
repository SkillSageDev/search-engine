# Search Engine
Have you ever imagined a website that you upload a document to it and you forget about it, then when you search it popups to you, thats what a search engine is!

This is an opensource project that you can steal and do whatever you want of it.

## Getting Started
### installing the project
you can install the project with

```bash
git clone https://github.com/SkillSageDev/search-engine.git
```
### running the backend
create an image from the dockerfile that is indside the backend folder

```bash
docker build -t backend_python backend/
```

create a container from it. make sure to give it a port and use the same name of the image you created which is **backend_python** 
```bash
docker run -p 8000:8000 backend_python
```

now the backend should be running without any errors. you can open http://localhost:8000 to check it out.

### running the frontend
coming soon...
