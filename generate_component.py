import re
import json
from box import Box  # pip install python-box
from pyefun import 子文本替换


def to_camel_case(string):
    # 将字符串按 '-' 分割，然后将每个单词首字母大写，最后合并 第一个字符小写
    words = string.split('-')
    return ''.join(word.capitalize() for word in words)


def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        json_str = f.read()

    try:
        return Box(json.loads(json_str),
                   default_box=True,
                   default_box_none=True,
                   conversion_box=True,
                   box_dots=True,

                   )
    except:
        return None


def 生成类(类名称, 函数名和参数列表, 组件名称, mode=""):
    pass
    # 类名称 VanillaAction
    # 函数名和参数列表 [
    #    {
    #        "name": "$$id",
    #        "type": "string",
    #        "description": "组件唯一 id，主要用于页面设计器中定位 json 节点"
    #    },
    if mode != "":
        mode = f"""self.set("mode", "{mode}")"""

    code = f"""
from amis.AmisComponent import AmisComponent

class {类名称}(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "{组件名称}")
        {mode}
    """
    for 函数名和参数 in 函数名和参数列表:

        ref = ""  # '#/definitions/SchemaClassName'
        if 函数名和参数['$ref'] != {}:
            ref = f"{函数名和参数['$ref']}"
            # 替换 #/definitions/
            ref = ref.replace("#/definitions/", "")
            ref = definitions[ref]['description']
            if ref != {}:
                ref = "# " + ref.replace("\n", " ")
            else:
                ref = ""
            pass

        description = ""
        if 函数名和参数['description'] != {}:
            description = f"# {函数名和参数['description']}"
            # 替换\n为空格
            description = description.replace("\n", " ")

        enum = ""
        if 函数名和参数['enum'] != {}:
            enum = f"# 可选项: {函数名和参数['enum']}"

        code += f"""
    def {函数名和参数['name']}(self, {函数名和参数['name']}):
        {description}{enum}
        {ref}
        return self.set("{函数名和参数['name']}", {函数名和参数['name']})

        """
    return code


schema = read_json_file('schema.json')

definitions = schema.definitions
SchemaType = definitions.SchemaType.enum
print("SchemaType", len(SchemaType), SchemaType)


def to_kebab_case(string):
    # 在大写字母前添加短横线，然后将整个字符串转换为小写
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    return pattern.sub('-', string).lower()


import pyefun


def 生成组件的类():
    k = 0
    for key, value in definitions.items():
        k = k + 1
        # 只保留 key 以 Schema 结尾 | Object 结尾 | Action 结尾
        if pyefun.判断文本s(key, ["Schema", "Action", "Object", "Control"]):
            pass
            # print(k,key)
        else:
            print("跳过", key)
            continue
        print("==========")
        # print("key", key)
        # print("value", json.dumps(value, ensure_ascii=False, indent=4))
        函数名和参数列表 = []
        # 类名称替换Schema为空
        类名称 = key.replace("Schema", "")
        # 现在组件的名称是AnchorNav 驼峰 我需要转换为 anchor-nav

        properties = value.properties
        for key, value in properties.items():
            # print("key", key)
            # print("value", json.dumps(value, ensure_ascii=False, indent=4))
            # 如果 key 包含$ 就跳过
            if "$" in key:
                continue
            函数名和参数列表.append({
                "name": key,
                "type": value.type,
                "description": value.description,
                "enum": value.enum,
                "$ref": value['$ref'],

                # "value": value,
            })

        # print("函数名和参数列表", json.dumps(函数名和参数列表, ensure_ascii=False, indent=4))

        print("类名称1", 类名称)
        if not pyefun.判断文本(类名称, ["CRUD"]):
            # 类名称 = to_camel_case(类名称)
            组件名称 = to_kebab_case(类名称)
            mode = ""
        else:
            类名称 = 类名称
            # 类名称转换为小写
            if pyefun.判断文本(类名称, ["CRUD2"]):
                组件名称 = "crud2"
            else:
                组件名称 = "crud"

            mode = 子文本替换(类名称, "CRUD2", "")
            mode = 子文本替换(mode, "CRUD", "")
            mode = mode.lower()

        print("类名称2", 类名称)
        code = 生成类(类名称, 函数名和参数列表, 组件名称, mode)
        print("类名称3", 类名称)
        # print("code", code)
        pyefun.写到文件(f"components2/{类名称}.py", code)

        # print("==========", code)


def 组件名称转换驼峰():
    def to_camel_case(string):
        # 将字符串按 '-' 分割，然后将每个单词首字母大写，最后合并 第一个字符小写
        words = string.split('-')
        return ''.join(word.capitalize() for word in words)

    newComponents = []
    for key in SchemaType:
        # key类似于 button-group需要 转换为驼峰 首字母大写
        camel_case_key = to_camel_case(key)
        newComponents.append(camel_case_key)
    print(newComponents)

    # for key in newComponents:
    # print("组件名称", key)

    return newComponents


生成组件的类()
