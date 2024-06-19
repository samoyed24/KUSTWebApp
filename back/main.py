from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello World"}


@app.get('/test/{content}')
async def test(needy: str, content: str or None = None):
    return {"content": content, "needy": needy}
