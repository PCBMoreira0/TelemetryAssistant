from typing import Dict, List


def augment_prompt(query: str, search_results: List[Dict]) -> str:
    context_parts = []
    for i, result in enumerate(search_results, 1):
        source_name = result["metadata"].get(
            "title", result["metadata"].get("source", f"Documento {i}")
        )
        context_parts.append(f"{source_name}\n{result['content']}")

    context = "\n\n".join(context_parts)

    return context
