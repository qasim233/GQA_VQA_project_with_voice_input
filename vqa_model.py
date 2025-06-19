import torch
from transformers import BlipProcessor, BlipForQuestionAnswering
from PIL import Image
import speech_recognition as sr
from gtts import gTTS
import os
import tempfile
import playsound

class VQAModel:
    def __init__(self):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
        self.model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base").to(self.device)

    def predict(self, image: Image.Image, question: str) -> str:
        # Filter out questions that are likely unrelated to image content
        irrelevant_keywords = ["capital", "president", "prime minister", "country", "nation", "currency", "population"]
        if any(keyword in question.lower() for keyword in irrelevant_keywords):
            return "I can only answer questions related to the image."

        inputs = self.processor(image, question, return_tensors="pt").to(self.device)
        out = self.model.generate(**inputs)
        answer = self.processor.decode(out[0], skip_special_tokens=True)

        # Filter uncertain or generic responses
        if answer.lower() in ["i don't know", "", "n/a"] or any(word in answer.lower() for word in ["sorry", "unable", "cannot"]):
            return "I am not sure how to answer that based on the image."

        return answer

    def ask_with_voice(self, image: Image.Image):
        recognizer = sr.Recognizer()
        mic = sr.Microphone()
        print("🎤 Please ask your question after the beep...")

        with mic as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            question = recognizer.recognize_google(audio)
            print(f"You asked: {question}")
            answer = self.predict(image, question)
            print(f"Answer: {answer}")

            # Save audio to temp file, then play and delete
            tts = gTTS(text=answer, lang='en')
            temp_path = os.path.join(tempfile.gettempdir(), "vqa_answer.mp3")
            tts.save(temp_path)
            playsound.playsound(temp_path)
            os.remove(temp_path)

            return question, answer

        except sr.UnknownValueError:
            return None, "Could not understand audio. Please try again."
        except sr.RequestError as e:
            return None, f"Speech recognition error: {e}"