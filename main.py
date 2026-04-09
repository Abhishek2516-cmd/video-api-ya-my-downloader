from fastapi import FastAPI, HTTPException
import yt_dlp

app = FastAPI()

@app.get("/")
def home():
    return {"status": "online"}

@app.get("/dl")
def download(url: str):
    try:
        ydl_opts = {'format': 'best', 'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                "title": info.get('title'),
                "url": info.get('url'),
                "thumb": info.get('thumbnail')
            }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
