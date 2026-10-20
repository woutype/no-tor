from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

app = FastAPI()
active_share = {}

@app.get('/')
def read_root():
    return {'status': 'ok'}


@app.get('/dl/{token}')
def download_file(token: str):

    if token != active_share.get("token"):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(
        path=active_share['file_path'],
        filename=active_share['file_name'],
    )