import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/test/")
async def root(content=None):
    return HTMLResponse(content)


if __name__ == '__main__':
    uvicorn.run(app)
