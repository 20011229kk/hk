import uvicorn
from fastapi import FastAPI, Body

app = FastAPI()


@app.api_route("/test/")
async def root(user=Body(None)):
    return user


if __name__ == '__main__':
    uvicorn.run(app)
