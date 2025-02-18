import uvicorn
from fastapi import FastAPI, Form

app = FastAPI()

@app.api_route("/test/")
async def root(username=Form(None), password=Form(None)):
    return {"username": username, "password": password}

if __name__ == '__main__':
    uvicorn.run(app)