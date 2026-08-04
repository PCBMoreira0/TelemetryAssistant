from ollama import generate
import config

def stream_response(prompt: str, model: str = config.LLM_MODEL):
    for chunk in generate(model=model, prompt=prompt, stream=True):
        yield chunk["response"]