import requests
from typing import List, Dict
import openai_azure

STACKOVERFLOW_API_URL = "https://api.stackexchange.com/2.3/search/advanced"


def fetch_stackoverflow_answers(
    question: str, site: str = "stackoverflow", use_ai_sort: bool = True
) -> List[Dict]:
    """
    Fetch answers from Stack Overflow API for a given question string.
    Returns a list of answer dicts, optionally re-ranked by an LLM for relevance/accuracy.
    """
    params = {
        "order": "desc",
        "sort": "relevance",
        "q": question,
        "site": site,
        "filter": "!9_bDDxJY5",
    }
    response = requests.get(STACKOVERFLOW_API_URL, params=params)
    response.raise_for_status()
    data = response.json()

    results = []
    for item in data.get("items", []):
        if item.get("is_answered"):
            results.append(
                {
                    "title": item.get("title"),
                    "link": item.get("link"),
                    "question_id": item.get("question_id"),
                    "score": item.get("score"),
                    "answers": item.get("answer_count"),
                }
            )

    if results and use_ai_sort:
        results = openai_azure.arrange_answers_by_relevance(results, question)

    return results
