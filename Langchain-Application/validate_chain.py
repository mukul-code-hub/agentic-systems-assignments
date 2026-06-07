from lcel_ollama_example import build_chain

chain = build_chain()

def is_response_valid(response: str) -> tuple[bool, list[str]]:
    """
    This function determine whether response generated follows a define criteria or not.
    
    Success Criteria:
    1. Response should be string.
    2. REsponse should not be empty.
    3. Response should contain exactly 3 bullet point.
    4. Response should not be too long.
    """

    # List of String
    errors = []

    #REsponse is not string
    if isinstance(response, str):
        # Response is not of string type.
        errors.append("Response is not string")
        return False, errors
    
    # Response is not empty
    if not response.strip():
        errors.append("Response is empty")
    
    # Response should contain 3 bullet point


    # Response should be 100 words.
    word_count = len(response.split())
    if word_count > 100:
        errors.append("Response is too long")

    if len(errors) == 0:
        return True, errors
    
    return False, errors

def main():
    test_case = {
        "topic" : "LCEL in Langchain",
        "analogy_domain" : "Software Engineering"
    }

    response = chain.invoke(test_case)

    print(response)
    
# Validte the response.
is_valid, errors = is_response_valid(response)

if is_valid:
    print("Valid response")
else:
    print("Invalid response.")
    print(errors)



