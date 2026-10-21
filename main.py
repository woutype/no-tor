from fastapi import FastAPI

app = FastAPI()

active_share = {}

@app.get('/')
def read_root():
    pass


@app.get('/dl/{token}')
def download_file(token: str):
    pass