from fastapi import FastAPI
from  gtts import gTTS
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

@app.get("/convert")
def convert_text_to_speech(text: str):
    speech = gTTS(text=text, lang='en')
    audio_file = "Audio.mp3"
    speech.save(audio_file)
    return FileResponse(audio_file)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9999)


