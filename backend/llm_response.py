from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_response(user_query: str, context: str):

    prompt = f"""
    You are an AI customer support assistant.

    Context:
    {context}

    User Query:
    {user_query}

    Generate a helpful response.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
