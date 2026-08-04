from rag.prompt import build_rag_prompt
from rag.embeddings import embed_query
from llm_client import stream_response
from rag.retrieval import search_vector_database


question = input("Ask something: ")

query = embed_query(question)
results = search_vector_database(
    query_embedding=query,
)
prompt = build_rag_prompt(question=question, search_results=results)

print('\nFINAL PROMPT:\n' + prompt + '\n')

print("LLM RESPONSE:\n")
for token in stream_response(prompt=prompt):
    print(token, end="", flush=True)