
import uvicorn
from fastapi import FastAPI

app = FastAPI()


# route 已经过时 如下使用的是api_route
@app.api_route("/",methods=["POST"])
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
@app.post("/hello")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
# 支持请求 /test/1 这样类型的参数
@app.get("/test/{id}")
async def test(id):
    return id

# 支持请求 /test?id=1 这样类型的参数
@app.get("/test1")
async def test1(id):
    return id
if __name__ == '__main__':
    uvicorn.run(app)
