from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse

from file_service import prepare_share
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

share = prepare_share('requirements.txt')

@app.get('/')
def read_root(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='sender.html',
        context=share,
    )


@app.get('/dl/{token}/{filename}')
def download_file(token: str, filename: str):
    if token != share.get('token'):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(
        filename=share.get('file_name'),
        path=share.get('file_path'),
    )


@app.get('/download/{token}')
def download_page(token: str, request: Request):
    if token != share.get('token'):
        raise HTTPException(status_code=404, detail="File not found")
    
    return templates.TemplateResponse(
        request=request,
        name='download.html',
        context=share,
    )


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)