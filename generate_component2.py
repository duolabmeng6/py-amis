# 读取 /Users/ll/Downloads/amis-master/docs/zh-CN/components 的所有文件路径
import json
import os
import re
import pyefun

def to_camel_case(string):
    # 将字符串按 '-' 分割，然后将每个单词首字母大写，最后合并 第一个字符小写
    words = string.split('-')
    return ''.join(word.capitalize() for word in words)


def 生成类(类名称, 函数名和参数列表, 组件名称):
    pass
    # 类名称 VanillaAction
    # 函数名和参数列表 [
    #    {
    #        "name": "$$id",
    #        "type": "string",
    #        "description": "组件唯一 id，主要用于页面设计器中定位 json 节点"
    #    },

    code = f"""
from amis.AmisComponent import AmisComponent

class {类名称}(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "{组件名称}")
    """
    for 函数名和参数 in 函数名和参数列表:

        description = ""
        if 函数名和参数['description'] != {}:
            description = f"{函数名和参数['description']}"
            # 替换\n为空格
            description = description.replace("\n", " ")

        enum = ""
        if 函数名和参数['enum'] != {}:
            enum = f"可选项: {函数名和参数['enum']}"

        code += f"""
    def {函数名和参数['name']}(self, {函数名和参数['name']}):
        # {description} {enum}
        return self.set("{函数名和参数['name']}", {函数名和参数['name']})

        """
    return code



def 读取文件路径():
    components_dir = "/Users/ll/Downloads/amis-master/docs/zh-CN/components"
    file_paths = []
    for root, dirs, files in os.walk(components_dir):
        for file in files:
            if file.endswith(".md"):
                file_paths.append(os.path.join(root, file))
    return file_paths


def 解析markdown文件(文件路径):
    with open(文件路径, "r", encoding="utf-8") as file:
        内容 = file.read()

    # 解析标题
    标题匹配 = re.search(r'title: (.+)', 内容)
    标题 = 标题匹配.group(1) if 标题匹配 else "未找到标题"

    # 解析属性表
    属性表匹配 = re.search(r'## 属性表\n\n([\s\S]+?)(?=\n##|\Z)', 内容)
    属性表 = 属性表匹配.group(1).strip() if 属性表匹配 else "未找到属性表"

    return 标题, 属性表


def 解析属性表(属性表):
    行列表 = 属性表.split('\n')[2:]  # 跳过表头和分隔线
    属性列表 = []
    for 行 in 行列表:
        # 文本替换行 \|转换为 ,

        行 = 行.replace('\|', ',')
        列 = 行.split(' | ')
        if len(列) != 4:
            continue
        列 = [x.replace('|', '').strip() for x in 列]
        列[1] = 列[1].replace("'", "").replace("'", "")
        列[1] = 列[1].replace("`", "")
        列[1] = 列[1].replace(" ", "")
        if "." in 列[0]:
            continue
        if "[" in 列[0]:
            # print(列[0],)
            # print(列[1],)
            if "SchemaNode" in 列[1]:
                continue

            列[0] = pyefun.strCut(列[0], "[$]")
        if "--" in 列[0]:
            continue
        if 列[0] == "":
            continue


        # print(列)
        属性列表.append({
            'name': 列[0],
            'enum': 列[1],
            'default': 列[2],
            'description': 列[3]
        })
    return 属性列表


def 生成文档组件():
    文件路径列表 = 读取文件路径()
    # 读取文件路径列表 的 所有文件内容
    # 按照a-z排序
    文件路径列表.sort()
    组件名称列表 = []
    for 文件路径 in 文件路径列表:
        # print(文件路径)
        # 删除.md
        文件名 = 文件路径.split("/")[-1].replace(".md", "")
        # print(文件名)
        if 文件名 != "":
            标题, 属性表 = 解析markdown文件(文件路径)
            # print(f"组件: {标题}")
            # print(f"属性表: {属性表}")
            属性列表 = 解析属性表(属性表)
            # print(f"属性列表: {json.dumps(属性列表, ensure_ascii=False, indent=4)}")

            类名 = to_camel_case(文件名)
            code = 生成类(类名, 属性列表, 文件名)
            print(类名)
            print(code)
            组件名称列表.append(类名)


            pyefun.写到文件(f"components/{类名}.py", code)



# 枚举components2目录和components的文件夹
def 覆盖组件():
    components2_dir = "./components2"
    components_dir = "./components"
    components2_files = [f for f in os.listdir(components2_dir) if f.endswith('.py')]
    for 文件名 in components2_files:
        print(f"新增 {文件名}")
        # 删除
        pyefun.删除文件(os.path.join(components_dir, 文件名))
        pyefun.写到文件(os.path.join(components_dir, 文件名),pyefun.读入文本(os.path.join(components2_dir, 文件名)))

def 生成工具类():
    def 生成amis组件类(组件名称列表):
        importcde = ""
        fccode = ""
        for 组件名称 in 组件名称列表:
            importcde += f"""from amis.components.{组件名称} import {组件名称}\r\n"""
            fccode += f"""
    @staticmethod
    def {组件名称}() -> {组件名称}:
        return {组件名称}()
        """
        code = f"""
{importcde}

class amis:
    {fccode}

    """
        return code
    components_dir = "./components"
    components_files = [f for f in os.listdir(components_dir) if f.endswith('.py')]
    components_files.sort()
    components_files = [pyefun.strCut(x, "$.py") for x in components_files]
    # 删除 __init__
    components_files = [x for x in components_files if x != "__init__"]
    code = 生成amis组件类(components_files)
    print(code)
    pyefun.写到文件("./amis.py", code)

# 生成文档组件()
覆盖组件()
生成工具类()
