from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# 将public目录挂载为静态文件目录
app.mount("/", StaticFiles(directory="public", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
