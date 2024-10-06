# py-amis

```python
import random

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.exceptions import HTTPException

from amis.amis import amis
import json

app = FastAPI()


@app.get("/")
def home():
    page = amis().Page().body([
        amis().Form()
        .api("/add")
        .title("登录")
        .rules([
            {"rule": "data.usernmae", "message": "用户名 为空", "name": ["username"]},
            {"rule": "data.password", "message": "密码 为空", "name": "password"}
        ])
        .body([
            amis().InputText().label("用户名").name('username'),
            amis().InputPassword().label("密码").name('password'),
        ])
        .actions([
            amis().Button().label("重置").actionType("reset"),
            amis().Button().label("保存").actionType("submit").level("primary")
        ])
    ])
    amis_html = page.to_html()
    return HTMLResponse(content=amis_html, status_code=200)


@app.get("/table")
def home():
    page = (amis().Page()
    .type("service")
    .api("/get_table")
    .body([
        amis().CRUD().title("表格1").source("$rows").columns([
            {"name": "id", "label": "ID"},
            {"name": "name", "label": "姓名"}
        ])
    ]))
    amis_html = page.to_html()
    return HTMLResponse(content=amis_html, status_code=200)


@app.get("/get_table")
def get_table():
    # 随机生成name列表
    names = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v", "w", "x", "y", "z"]
    # 随机生成id列表
    ids = [i for i in range(1, 101)]
    # 随机生成name列表
    names = random.choices(names, k=100)
    rows = []
    for i in range(100):
        rows.append({
            "name": names[i],
            "id": ids[i]
        })
    return {
        "status": 0,
        "msg": "ok",
        "data": {
            "count": len(rows),
            "rows": rows
        }
    }


@app.api_route("/{path:path}", methods=["POST", "PUT", "DELETE"])
async def handle_all_requests(request: Request):
    json_data = await request.json()
    print(f"请求地址: {request.url}")
    print(f"请求数据: {json_data}")
    message = json.dumps({
        "json_data": json_data,
        "url": str(request.url),
        "method": request.method
    })
    return {
        "status": 0,
        "message": message,
        "mydata": message,
    }


# 将public目录挂载为静态文件目录
app.mount("/jssdk", StaticFiles(directory="public/jssdk", html=True), name="static")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=5001, reload=True)


```
