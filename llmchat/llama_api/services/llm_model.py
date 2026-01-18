import os
from datetime import datetime, timezone
from openai import OpenAI

BASE_URL = os.getenv("AI_MODEL_SERVICE", "http://ai-model:8080")

client = OpenAI(base_url=os.getenv("AI_BASE_URL", "http://model-runner.docker.internal/engines/llama.cpp/v1/"),
                api_key=os.getenv("AI_API_KEY", "anything"))

def to_llm_messages(messages, system_prompt=None):
    return [
        {
            "role": msg.role,
            "content": msg.text
        }
        for msg in sorted(
            messages,
            key=lambda m: m.created_at or datetime.min.replace(tzinfo=timezone.utc)
        )
    ]

def generate_llm_response(messages):
    llm_messages = to_llm_messages(messages)

    response = client.chat.completions.create(
        model=os.getenv("AI_MODEL"),
        messages=llm_messages
    )
    while (response.choices[0].message.content == ""):
        response = client.chat.completions.create(
            model=os.getenv("AI_MODEL"),
            messages=llm_messages
        )

    return response.choices[0].message.content
