import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_TOKEN = os.getenv('HF_TOKEN')
HF_MODEL = "openai/gpt-oss-120b"

client = InferenceClient(
    model=HF_MODEL,
    token=HF_TOKEN
)

def llm(prompt):
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024,
        temperature=0.7,
        top_p=0.9,
        stream=False 
    )
    return response.choices[0].message.content.strip() # type: ignore