from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from amis.amis import amis

app = FastAPI()


@app.get("/")
def home():
    button1 = amis().button().label("按钮1").size("lg").level("primary").set("className", "my-custom-class")
    button2 = amis().button().label("按钮2").url("https://example.com").tooltip("点击跳转")
    button3 = amis().button().label("按钮3").actionType("submit").disabled(True)

    page = amis().page().body(
        button1,
        button2
        , button3
    )
    amis_html = page.to_html()
    print(amis_html)
    return HTMLResponse(content=amis_html, status_code=200)


# 将public目录挂载为静态文件目录
app.mount("/", StaticFiles(directory="public", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001)
