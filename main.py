
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


loader = PyPDFLoader('YOUR_PDF_FILE.pdf')  # Replace with your PDF file name
doc = loader.load()

print(doc)

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(doc)

print(docs)

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorstore = Chroma.from_documents(docs, embedding_model)

retriever = vectorstore.as_retriever(search_type="similarity", k=5)

prompt = PromptTemplate.from_template("Give the Cloud project and realted details")


llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash", api_key = GOOGLE_API_KEY)  # Replace with your Google API key


chain = prompt | llm

query = "Give the Cloud project and realted details."
result = chain.invoke({"query": query})

print(result)

