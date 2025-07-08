from azure.identity import DefaultAzureCredential

# from azure.ai.openai import OpenAIClient
import openai

from typing import List, Dict
import os

endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
api_key = os.environ.get("AZURE_OPENAI_API_KEY")
deployment_name = "gpt-4.1"
model_name = "gpt-4.1"

openai.api_type = "azure"
openai.base_url = endpoint
openai.api_version = "2024-12-01-preview"
openai.api_key = api_key


def find_most_relevant_question(questions: List[str], question: str) -> str:
    """
    Sends a list of questions to an Azure OpenAI model to find the most relevant question.
    Returns the most relevant question from the list.
    """
    prompt = f"""
    Given the following list of Stack Overflow questions (as JSON objects) and the query: '{question}',
    find the most relevant question from the list and return only the full JSON object of that question. 
    Do not return anything else except the JSON object.

    Questions:
    {questions}
    """

    try:
        response = openai.chat.completions.create(
            model=deployment_name,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that finds the most relevant question.",
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=200,
            temperature=0.7,
        )

        content = response.choices[0].message.content
        print(f"Response content: {response}")

        if content is not None:
            return content.strip()
        else:
            return ""
    except Exception as e:
        print(f"Error: {e}")
        return ""


def arrange_answers_by_relevance(answers: List[Dict], question: str) -> List[Dict]:
    """
    Sends Stack Overflow answers to an Azure OpenAI model to arrange them by relevance.
    Returns a new list of answers sorted by relevance (most relevant first).
    """
    prompt = f"""
    Given the following Stack Overflow answers to the question: '{question}',
    arrange them in order of relevance (most relevant first). Return the list of answer indices in the new order.
    Answers:
    """
    for idx, ans in enumerate(answers):
        prompt += f"\n{idx+1}. Title: {ans['title']} | Score: {ans['score']} | Answers: {ans['answers']} | Link: {ans['link']}"

    try:
        response = openai.chat.completions.create(
            model=deployment_name,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that sorts answers by relevance.",
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=200,
            temperature=0.7,
        )

        content = response.choices[0].message.content
        if content is not None:
            order_str = content.strip()
            order = [int(i) - 1 for i in eval(order_str) if 0 < int(i) <= len(answers)]
            sorted_answers = [answers[i] for i in order]
            return sorted_answers
        else:
            return answers
    except Exception as e:
        print(f"Error: {e}")
        return []
