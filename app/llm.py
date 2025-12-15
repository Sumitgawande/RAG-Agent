from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def generate_answer(question, context):
    prompt = f"""
You are a financial analyst.
Answer ONLY using the context.

Context:
{context}

Question:
{question}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text
