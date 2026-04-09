import os
from fastapi import FastAPI, HTTPException
import yt_dlp
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"status": "API is Running"}

@app.get("/dl")
def download(url: str):
    try:
        ydl_opts = {'format': 'best', 'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                "title": info.get('title'),
                "url": info.get('url')
            }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
