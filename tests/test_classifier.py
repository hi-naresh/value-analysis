from src.core.classifier import classify_text


def test_classify_text():
    text = "I felt grateful today for my family's support."
    scores = classify_text(text)
    assert isinstance(scores, dict)
    assert "Gratitude" in scores
