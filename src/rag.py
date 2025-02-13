from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_google_genai import GoogleGenerativeAIEmbeddings

import os
from dotenv import load_dotenv

load_dotenv()

# generate system prompt
class SystemPrompt:
    def __init__(self) -> None:
        pass

    def generate_system_context(self):
        system_context = ("""You are an AI-powered exam conductor responsible for creating and administering tests on a defined subject.  
            Your goal is to generate structured exams with varying difficulty levels, ensuring a balanced assessment of the student's knowledge.  
            The test should include a mix of question types, such as:  

            - **Multiple Choice Questions (MCQs)**  
            - **True/False Questions**  
            - **Fill in the Blanks**  
            - **Reasoning and Analytical Questions**  
            - **Paragraph-based Questions**  
            - **Short and Long Essays**  

            Adapt the difficulty level based on the student's proficiency and provide clear instructions for each section.  
            Ensure the questions are diverse, fair, and encourage critical thinking while maintaining subject relevance.  

            {context}
            """)
        
        return system_context
    
# embedder class
class GetEmbedder:
    def __init__(self):
        pass

    def embedding_instance_provider(self):
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        return embeddings
    
# configuring Google Gemini API
apiKey = os.getenv('GOOGLE_API_KEY')

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = apiKey

print("Gemini API Key set successfully!")

# configuring PineCone API Credentials
pineconeKey = os.getenv('PINECONE_API_KEY')

if "PINECONE_API_KEY" not in os.environ:
    os.environ["PINECONE_API_KEY"] = pineconeKey

print("PineCone API Key set successfully!")

# 🔹 Pinecone Connector Class
class PineConeConnector:
    def __init__(self, uid, embedder) -> None:
        self.uid = uid
        self.embedder = embedder
        self.index_name = f"{self.uid}"

        # Initialize Pinecone once
        self.pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

    def get_retriever(self):
        """Retrieves stored embeddings from Pinecone."""
        doc_store = PineconeVectorStore.from_existing_index(
            index_name=self.index_name,
            embedding=self.embedder,
        )
        retriever = doc_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})
        return retriever
    
class GeminiRag:
    def __init__(self, retriever, question):
        self.retriever = retriever
        self.question = question

        # Initialize LLM
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.9,)

        # Generate system context and set up prompt template
        system_context = SystemPrompt().generate_system_context()
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_context),
                ("human", "{input}"),
            ]
        )

    def answer_prompt(self):
        """Retrieves documents and answers the prompt."""
        prompt_answer_chain = create_stuff_documents_chain(self.llm, self.prompt)
        rag_chain = create_retrieval_chain(self.retriever, prompt_answer_chain)

        return rag_chain.invoke({"input": self.question})