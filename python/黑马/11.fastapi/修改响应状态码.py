import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/test/")
async def root():
    return JSONResponse({'msg': 'hello'}, status_code=202, headers={'x-token': 'aa11233'})


if __name__ == '__main__':
    uvicorn.run(app)
