from amis.amis import amis

if __name__ == "__main__":
    # 示例用法
    button1 = amis().button().label("按钮1").size("lg").level("primary").set("className", "my-custom-class")
    button2 = amis().button().label("按钮2").url("https://example.com").tooltip("点击跳转")
    button3 = amis().button().label("按钮3").actionType("submit").disabled(True)

    page = amis().page().body(
        button1,
        button2
        , button3
    )
    amis_json = page.to_json()
    print(amis_json)
