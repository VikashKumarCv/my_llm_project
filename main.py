from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Initialize translation pipelines for different languages
translation_pipelines = {
    "fr": pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr"),
    "es": pipeline("translation", model="Helsinki-NLP/opus-mt-en-es"),
    "de": pipeline("translation", model="Helsinki-NLP/opus-mt-en-de"),
    "hi": pipeline("translation", model="Helsinki-NLP/opus-mt-en-hi")
}

class TranslationRequest(BaseModel):
    text: str
    target_language: str

@app.post("/translate/")
def translate_text(request: TranslationRequest):
    if request.target_language not in translation_pipelines:
        raise HTTPException(status_code=400, detail="Unsupported language")
    translated_text = translation_pipelines[request.target_language](request.text)
    return {"translated_text": translated_text[0]['translation_text']}

class QuestionRequest(BaseModel):
    question: str
    context: str

qa_pipeline = pipeline("question-answering")

@app.post("/question/")
def answer_question(request: QuestionRequest):
    answer = qa_pipeline(question=request.question, context=request.context)
    return {"answer": answer['answer']}

# Serve the static files
app.mount("/", StaticFiles(directory="static", html=True), name="static")