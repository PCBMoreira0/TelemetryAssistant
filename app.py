from prompts.prompt import build_prompt
from rag.augment import augment_prompt
from rag.embeddings import embed_query
from rag.response_gen import stream_response
from rag.retrieval import search_vector_database


question = input("Faça uma pergunta: ")

query = embed_query(question)
results = search_vector_database(
    query_embedding=query,
)
context = augment_prompt(query=question, search_results=results)
prompt = build_prompt(question=question, context=context)

print('\nFINAL PROMPT:\n' + prompt + '\n')

print("LLM RESPONSE:\n")
for token in stream_response(prompt=prompt):
    print(token, end="", flush=True)