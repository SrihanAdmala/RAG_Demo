from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model_name = "gpt-3.5-turbo", temperature = 0)

loader = PyPDFLoader("Day02_String_Functions.pdf")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents)
print(chunks[0], len(chunks))

embeddings = OpenAIEmbeddings(model = "text-embedding-3-small")

vectorstore = Chroma.from_documents(documents = chunks, embedding = embeddings, persist_directory = "./chroma_db")

retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant answering questions about a PDF.

Use ONLY the information contained in the context below.

If the answer is not contained in the context, say:
"I couldn't find that information in the PDF."

Context:
{context}

Question:
{question}

Answer:")
""")

def ask_question(question):
    documents = retriever.invoke(question)

    context = "\n\n".join(document.page_content for document in documents)

    messages = prompt.invoke({"context": context, "question": question})

    response = llm.invoke(messages)

    return response.content

while True:
    question = input("You:")

    if question.lower() in ["exit", "quit"]:
        break

    answer = ask_question(question)
    print("AI:", answer)