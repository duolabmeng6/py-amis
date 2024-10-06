from amis.amis import amis

if __name__ == "__main__":
    page = amis().Page().body([
        amis().Form().body([
            amis().InputText().label("用户名").name('username'),
            amis().InputPassword().label("密码").name('password'),
        ]).api("/add").actions([
            amis().Button().label("提交").actionType("submit").level("primary")
        ])
    ])
    amis_json = page.to_json()
    print(amis_json)
    # amis_html = page.to_html()
    # print(amis_html)
