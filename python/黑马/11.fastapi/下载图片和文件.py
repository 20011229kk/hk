import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/testimg/")
async def root():
    # 不加filename是预览图片 加了filename可以下载，也可以预览
    return FileResponse('xiaobai.png', filename='xiaobai.png')


if __name__ == '__main__':
    uvicorn.run(app)
