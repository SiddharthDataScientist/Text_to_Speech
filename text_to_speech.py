from fastapi import FastAPI
from  gtts import gTTS
from fastapi.responses import FileResponse
import uvicorn
from datetime import datetime

app = FastAPI()

@app.get("/convert")
def convert_text_to_speech(text: str):
    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
    audio_file = f"Audio_{current_datetime}.mp3"
    # speech = gTTS(text=text, lang='en', slow= False, lang_check=True) --ENGLISH
    speech = gTTS(text=text, lang='kn', slow= False, lang_check=True) 
    # speech = gTTS(text=text, lang='hi', slow= False, lang_check=True) --> HINDI
    # speech = gTTS(text=text, lang='ta', slow= False) --> TAMIL
    # speech = gTTS(text=text, lang='te', slow= False) -->TELUGU

    speech.save(audio_file)
    return FileResponse(audio_file)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9999)


