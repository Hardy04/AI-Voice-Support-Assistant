from fastapi import FastAPI, UploadFile, File
from speech_to_text import transcribe_audio
from rag_pipeline import retrieve_context
from llm_response import generate_response
import shutil

app = FastAPI()


@app.get("/")
def health_check():
    return {
        "status": "running"
    }


@app.post("/voice-query")
async def voice_query(audio: UploadFile = File(...)):

    file_location = f"temp_{audio.filename}"
  
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    transcription = transcribe_audio(file_location)

    context = retrieve_context(transcription)

    ai_response = generate_response(transcription, context)

    return {
        "transcription": transcription,
        "context": context,
        "response": ai_response
    }
