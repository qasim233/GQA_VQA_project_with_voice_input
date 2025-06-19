import json
from PIL import Image
import os

def load_question_and_image(questions_path, image_dir, index=0):
    with open(questions_path, 'r') as f:
        questions = json.load(f)

    qid = list(questions.keys())[index]
    question_data = questions[qid]
    image_id = question_data["imageId"]
    image_path = os.path.join(image_dir, f"{image_id}.jpg")

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    image = Image.open(image_path).convert("RGB")
    question = question_data["question"]
    answer = question_data["answer"]

    return image, question, answer
