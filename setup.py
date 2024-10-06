from setuptools import setup, find_packages

def install_requires():
    try:
        with open("requirements.txt", encoding='utf-8') as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except OSError:
        return []


setup(
    name='py-amis',
    version="0.0.0",
    description='A file storage management package supporting various providers like S3, OSS, and Qiniu.',
    long_description=open('README.md').read(),  #
    long_description_content_type='text/markdown',
    author='duolabmeng6',
    author_email='1715109585@qq.com',
    url='https://github.com/duolabmeng6/py-amis',
    packages=find_packages(),
    install_requires=install_requires(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    keywords="py-amis",
    include_package_data=True,  # 包含包中的所有文件
    exclude_package_data={
        '': ['.env'],  # 排除 .env 文件
    },
)
