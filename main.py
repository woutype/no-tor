from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from file_service import generate_token

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

active_share = {
    "file_name": "info.txt",
    "file_size": "24.5 GB",
    "token": generate_token(),
}

@app.get('/')
def read_root(request: Request):
    download_url = f"http://127.0.0.1:8080/dl/{active_share.get('token', '')}"

    return templates.TemplateResponse(
        request=request,
        name='download.html',
        context={
            "file_name": active_share.get('file_name'),
            "file_size": active_share.get("file_size", "0 B"),
            "token": active_share.get("token", ""),
            "download_url": download_url,
        }
    )


@app.get('/dl/{token}')
def download_file(token: str):

    if token != active_share.get("token"):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(
        path=active_share['file_path'],
        filename=active_share['file_name'],
    )