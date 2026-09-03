About this project:
This is an simple RAG (Retrieval Augmented Generation) program, written using langchain. This project uses the chroma database to store vectors and openAI's own embedding service. THIS PROJECT ONLY SUPPORTS OPENAI. ALL RAG FILES MUST BE PDF's.

Downloading/Setting up:
to use simply download the zipped repo file or clone the repo, open up the folder in an IDE, and download the requirements file (after creating a venv). Next, add an .env file, and to it add a variable named "OPENAI_API_KEY", and set the value to your api key.

Changing the retrieval file:
If you want the RAG to change source files, note that this will only work for other PDF's, to the project folder add an PDF file of your choice, and swap out the "Day02_String_Functions.pdf" (in the main.py) to the name newly imported PDF file from the pyPdfLoader object (variable name: loader).


