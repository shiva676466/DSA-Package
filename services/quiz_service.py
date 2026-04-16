from utils.file_handler import load_json

def get_quiz(topic):
    """
    Fetch quiz questions for a given topic.
    Example topics: 'arrays', 'strings', 'stack'
    """
    data = load_json("questions.json")
    return data.get(f"{topic}_quiz", [])