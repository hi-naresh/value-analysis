from transformers import pipeline
from src.core.config import settings

classifier = pipeline("zero-shot-classification", model=settings.MODEL_NAME)

prompts = {
    "Sincerity": "Does this journal entry reflect sincerity or honesty?",
    "Humility": "Does this journal entry demonstrate humility or modesty?",
    "Gratitude": "Does this journal entry express gratitude or thankfulness?",
    "Perseverance": "Does this journal entry show perseverance or determination?",
    "Aspiration": "Does this journal entry convey aspiration or ambition?",
    "Receptivity": "Does this journal entry indicate receptivity or openness to new ideas?",
    "Progress": "Does this journal entry reflect progress or improvement?",
    "Courage": "Does this journal entry demonstrate courage or bravery?",
    "Goodness": "Does this journal entry exhibit goodness or moral integrity?",
    "Generosity": "Does this journal entry show generosity or selflessness?",
    "Equanimity": "Does this journal entry reflect equanimity or calmness in difficult situations?",
    "Peace": "Does this journal entry demonstrate peace or tranquility?"
}

candidate_labels = [
    "Sincerity", "Humility", "Gratitude", "Perseverance", "Aspiration",
    "Receptivity", "Progress", "Courage", "Goodness", "Generosity",
    "Equanimity", "Peace"
]


def classify_text(text):
    # Implementing post-processing rules
    if len(text.strip()) == 0 or text.strip().lower() == "i did nothing today":
        return {label: 0.0 for label in prompts.keys()}

    scores = {}
    for label, prompt in prompts.items():
        # Generate results using refined prompts
        result = classifier(f"{prompt} {text}", candidate_labels)
        score = max(result['scores']) * 100  # Get the highest score
        if score > settings.THRESHOLD:
            scores[label] = round(score, 2)
        else:
            scores[label] = 0.0

    return scores
