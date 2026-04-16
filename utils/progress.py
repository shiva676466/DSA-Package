import json

def save_score(topic, score, total):
    data = {
        "topic": topic,
        "score": score,
        "total": total
    }

    with open("data/progress.json", "w") as f:
        json.dump(data, f, indent=4)