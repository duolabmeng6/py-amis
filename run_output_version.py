import os

version = os.environ.get('version')
version = version.replace("v", "")
print("version:", version)


fileDir = os.path.dirname(__file__)
print("file dir:", fileDir)
versionFilePath = os.path.join(fileDir, "setup.py")

with open(versionFilePath, "r") as f:
    content = f.read()
    content = content.replace("0.0.0", version)
    print("content:", content)
    with open(versionFilePath, "w") as f:
        f.write(content)

