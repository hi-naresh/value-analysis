from fastapi import APIRouter, HTTPException
from src.schemas import JournalEntry, ScoreResponse
from src.core.classifier import classify_text

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Welcome to value analyzer!"}


@router.get("/health")
def health():
    return {"Status": "Ok"}


@router.post("/analyze", response_model=ScoreResponse)
def classify_journal_entry(entry: JournalEntry):
    try:
        scores = classify_text(entry.text)
        return ScoreResponse(scores=scores)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
