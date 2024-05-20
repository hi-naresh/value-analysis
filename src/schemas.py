from pydantic import BaseModel
from typing import Dict

class JournalEntry(BaseModel):
    text: str

class ScoreResponse(BaseModel):
    scores: Dict[str, float]
