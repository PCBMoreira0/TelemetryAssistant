from ollama import generate

def stream_response(prompt: str, model: str = 'qwen2.5:3b'):
    for chunk in generate(model=model, prompt=prompt, stream=True):
        yield chunk["response"]