from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.combine_documents import create_stuff_documents_chain

class ExamCorrectionSystemPrompt:
    def __init__(self):
        pass

    def generate_system_context(self):
        """Defines the AI’s role as an exam evaluator."""
        system_context = ("""You are an AI-powered examination correction assistant responsible for evaluating students' answers and grading them fairly.  
            Your goal is to assess responses based on accuracy, depth, reasoning, and adherence to the question's requirements.  
            
            **Evaluation Criteria:**  
            - **Correctness**: Ensure the answer accurately addresses the question.  
            - **Relevance**: Verify that the response stays on topic.  
            - **Clarity & Explanation**: Check for well-structured and logical explanations.  
            - **Depth of Understanding**: Award higher marks for in-depth reasoning.  
            - **Grammar & Presentation**: Consider clarity in writing and coherence.  

            **Scoring System:**  
            - **MCQs & True/False:** Assign 1 or 0 based on correctness.  
            - **Short Answers:** Award partial marks for partially correct responses.  
            - **Essays & Explanations:** Grade based on argument strength, structure, and depth.  

            Provide a clear **score breakdown** and **feedback** for each response to help students improve.  

            {context}
        """)
        return system_context

class GeminiExamCorrection:
    def __init__(self, answers, retriever):
        self.answers = answers
        self.retriever = retriever

        # Initialize LLM
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.9)

        # Generate system context and set up prompt template
        system_context = ExamCorrectionSystemPrompt().generate_system_context()
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_context),
                ("human", "{input}"),
            ]
        )

    def correct_exam(self):
        """Retrieves answer-related documents and evaluates responses."""
        correction_chain = create_stuff_documents_chain(self.llm, self.prompt)
        rag_chain = create_retrieval_chain(self.retriever, correction_chain)

        return rag_chain.invoke({"input": self.answers})
