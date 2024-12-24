from pymongo import MongoClient
from config import settings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain_mongodb import MongoDBAtlasVectorSearch

def connect_to_mongo():
    try:
      client = MongoClient(settings.MONGO_URI)
      collection = client['mongoVector']['vectorstore']
      print("Connected to DB get set to use it")
      return collection
    except Exception as e:
      print(e)

def save_to_mongo(text):
    
    doc = Document(page_content=text)
    
    # If you have multiple texts, create a list of Document objects
    docs = [doc]
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    splits = text_splitter.split_documents(docs)
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=settings.GEMINI_API_KEY)
    
    store = [] 

    for split in splits:
        store.append(split.page_content)
        
    client = MongoClient(settings.MONGO_URI)
    collection = client['mongoVector']['vectorstore']
    
    docsearch = MongoDBAtlasVectorSearch.from_documents(
    splits, embeddings, collection=collection, index_name="vectorSearch"
    )
    
    print(docsearch)
    return "done"   

def get_docs(query):
    try:
        print("inside the function")
        print(query)
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=settings.GEMINI_API_KEY)
        client = MongoClient(settings.MONGO_URI)
        collection = client['mongoVector']['vectorstore']
        vectorStore = MongoDBAtlasVectorSearch(collection, embeddings, index_name="vector_index")
        docs = vectorStore.similarity_search(query)
        print("Vector Search Results:")
        print(len(docs))
        return docs
    except Exception as e:
        print("Database timeout or error:", str(e))
        
def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGroq(temperature=0, model_name="llama3-8b-8192",groq_api_key=settings.GROQ_API_KEY)

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

def user_input(user_question):
    docs = get_docs(user_question)

    chain = get_conversational_chain()

    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)

    print("Reply: ", response["output_text"])
    return response["output_text"]
    