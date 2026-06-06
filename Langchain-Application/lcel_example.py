from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(
    model="gpt-5.2"
)

prompt = PromptTemplate.from_template(
    """
    Explain {topic} to {audience} students.

    Requirements:
    - Use {tone} tone.
    - Give one real-life analogy to explain the concept.
    - Keep the response within {limit} words.
    """
)

# Without string output parser, model return the complete response.
output_parser = StrOutputParser()

# prompt -> LLM -> outout
chain = prompt | llm | output_parser
#chain = prompt | llm

response = chain.invoke(
    {
        "topic":"SQL Indexes",
        "audience":"Beginner",
        "tone":"Simple",
        "limit":100
    }
)

print(response)