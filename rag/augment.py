from typing import Dict, List

def augment_prompt(query: str, search_results: List[Dict]) -> str:
    context_parts = []
    for i, result in enumerate(search_results, 1):
        context_parts.append(
            f"Source {i}: {result['metadata']['title']}\n{result['content']}"
        )

    context = "\n\n".join(context_parts)

    return context
