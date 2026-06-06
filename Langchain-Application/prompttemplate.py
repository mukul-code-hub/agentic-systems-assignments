from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

client = ChatOpenAI(
    model="gpt-5.2"
)

prompt_template = PromptTemplate.from_template(
    """
    Explain {topic} to {audience} students.

    Requirements:
    - Use {tone} tone.
    - Give one real-life analogy to explain the concept.
    - Keep the response within {limit} words.
    """
)

prompt = prompt_template.format(
    topic="LangChain Components",
    audience="Beginners",
    tone="simple",
    limit=1000
)


response = client.invoke(prompt)

print(response.content)