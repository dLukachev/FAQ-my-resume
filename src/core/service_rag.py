from typing import Tuple, Dict
from src.core.retriever_refactored import retrieve
from src.core.prompts import SYSTEM_PROMPT_RU, build_user_prompt
from src.core.llm import llm as call_llm

def _extract_content(resp) -> str:
    try:
        return resp.choices[0].message.content.strip()
    except Exception:
        try:
            return resp["choices"][0]["message"]["content"].strip()
        except Exception:
            return str(resp)

def generate_answer(query: str, chat_id: str = "default"):
    docs, debug = retrieve(query, chat_id)
    context = "\n\n".join(d.page_content for d in docs)
    prompt = SYSTEM_PROMPT_RU + "\n\n" + build_user_prompt(context, query)
    answer = call_llm(prompt)   # ← уже строка
    return answer, debug
