from fastapi import APIRouter, HTTPException
from transformers import pipeline

router = APIRouter()

# Initialize Hugging Face pipeline for general queries and translation
qa_pipeline = pipeline("question-answering")
translation_pipeline = pipeline("translation_en_to_fr")

@router.post("/query")
async def handle_query(question: str, context: str):
    try:
        result = qa_pipeline(question=question, context=context)
        return {"answer": result['answer']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/translate")
async def handle_translation(text: str):
    try:
        result = translation_pipeline(text)
        return {"translation": result[0]['translation_text']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))