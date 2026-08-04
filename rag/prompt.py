from typing import Dict, List

def build_rag_prompt(question: str, search_results: List[Dict]) -> str:
    """
    Formata os documentos recuperados e constrói o prompt final (Augment).
    """

    context_parts = []
    for i, result in enumerate(search_results, 1):
        source_name = result["metadata"].get("title", result["metadata"].get("source", f"Doc {i}"))
        page = result["metadata"].get("page", "?")
        context_parts.append(f"Source {i} ({source_name}, Pág. {page}):\n{result['content']}")
    
    context_text = "\n\n".join(context_parts)

    return f"""You are a technical assistant specialized in solar boat telemetry.

Answer using only the information provided in the context.
If the answer cannot be found in the provided context, explicitly state that the information is not available in the documentation.
Do not make assumptions or use external knowledge.

CONTEXT:
{context_text}

QUESTION:
{question}
"""