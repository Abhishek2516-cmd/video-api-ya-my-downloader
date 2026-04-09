import os
from fastapi import FastAPI, HTTPException
import yt_dlp

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Backend is Live!"}

@app.get("/dl")
def download(url: str):
    try:
        ydl_opts = {
            'format': 'best',
            'quiet': True,
            'no_warnings': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                "title": info.get('title'),
                "url": info.get('url'),
                "thumb": info.get('thumbnail')
            }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Ye part Render ke liye bahut zaruri hai
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
