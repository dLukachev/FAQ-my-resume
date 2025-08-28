import re
from dataclasses import dataclass
from typing import Dict, List, Optional

def preprocess_text(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", (text or "").lower())
    text = re.sub(r"[\s-]+", " ", text)
    return text.strip()

SYNONYMS: Dict[str, List[str]] = {
    "docker": ["docker", "докер", "контейнер", "контейнеризация"],
    "fastapi": ["fastapi", "фастапи"],
    "postgresql": ["postgresql", "postgres", "постгрес"],
    "redis": ["redis", "редис"],
    "aiogram": ["aiogram", "айограм"],
    "sqlalchemy": ["sqlalchemy", "алхимия"],
    "celery": ["celery", "селери"],
}

@dataclass
class Intent:
    kind: str
    tech: Optional[str] = None

def detect_intent(query: str) -> Intent:
    prep = preprocess_text(query)
    for canon, alts in SYNONYMS.items():
        for w in alts:
            if w in prep:
                if "каких" in prep or "где" in prep:
                    return Intent(kind="LIST_TECH_PROJECTS", tech=canon)
                return Intent(kind="YN_TECH", tech=canon)
    return Intent(kind="GENERAL")
