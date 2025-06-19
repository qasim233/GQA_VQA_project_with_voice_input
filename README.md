# 🧠 GQA Visual Question Answering App with Voice Input

A complete Visual Question Answering (VQA) web app using the [GQA dataset](https://cs.stanford.edu/people/dorarad/gqa/download.html) and the lightweight [BLIP VQA model](https://huggingface.co/Salesforce/blip-vqa-base). Users can upload an image, ask a question (by text or voice), and hear the AI-powered answer.

---

## 🚀 Features

✅ Upload an image and ask a question about its contents  
✅ Voice-based question input using `SpeechRecognition`  
✅ Spoken answers using `gTTS` and `playsound`  
✅ Real-time answers from a pre-trained vision-language model (BLIP)  
✅ Smart filtering: avoids answering unrelated or factual questions not tied to image content  

---

## 🧰 Tech Stack

| Component           | Technology                           |
|--------------------|--------------------------------------|
| VQA Model          | `Salesforce/blip-vqa-base` (HuggingFace) |
| Image Handling     | `PIL`                                |
| Speech Input       | `SpeechRecognition`, `PyAudio`       |
| Speech Output      | `gTTS`, `playsound`                  |
| Frontend           | `Streamlit`                          |

---

## 📁 Project Structure

```
gqa-vqa-project/
├── app.py                  # Streamlit frontend
├── vqa_model.py            # BLIP model wrapper + voice I/O
├── gqa_utils.py            # GQA data loader (optional)
├── data/
│   ├── images/             # GQA image samples (e.g. 2407890.jpg)
│   ├── questions/          # GQA question JSON files
│   └── sceneGraphs/        # GQA scene graph JSON files (optional)
├── README.md               # This file
└── .gitignore              # Ignore .venv, audio temp files, etc
```

---

## 🧑‍💻 Setup Instructions

### 1. 🔁 Clone the Repository
```bash
git clone https://github.com/qasim233/GQA_VQA_project_with_voice_input.git
cd GQA_VQA_project_with_voice_input
```

### 2. 🐍 Create and Activate a Virtual Environment (Recommended)
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS/Linux
```

### 3. 📦 Install Requirements
```bash
pip install -r requirements.txt
```

#### 🔧 Windows Users (PyAudio Fix)

If pipwin fails, [download PyAudio .whl](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install manually.

---

### 4. 📂 Add Sample GQA Data
Download a few GQA image files and place them in:
```bash
data/images/2407890.jpg
```
Also place sample questions (optional) in:
```bash
data/questions/val_balanced_questions.json
```

---

### 5. ▶️ Run the Streamlit App
```bash
streamlit run app.py
```
- Upload an image
- Ask a question OR click "🎤 Ask with Voice"
- Get your answer and hear it aloud!

---

## ❓ Example Questions

| Image Content        | Example Question                     | Answer        |
|----------------------|--------------------------------------|---------------|
| Apple on table       | Is there a red apple on the table?   | No            |
| Man in kitchen       | What is the man holding?             | A knife       |
| Living room scene    | What is near the chair?              | A table       |
| General knowledge ❌ | What is the capital of USA?          | Rejected      |

> ❌ Model filters out non-image-related questions.

---

## 🧼 To-Do / Enhancements
- [ ] Add scene graph fusion for smarter answers
- [ ] Deploy to Hugging Face Spaces / Streamlit Cloud
- [ ] Add visual annotations for detected objects


---

## 🙌 Credits
- [GQA Dataset](https://cs.stanford.edu/people/dorarad/gqa/download.html)
- [Salesforce BLIP Model](https://huggingface.co/Salesforce/blip-vqa-base)
- [Streamlit](https://streamlit.io/) for rapid prototyping
