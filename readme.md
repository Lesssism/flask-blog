**这是一个用Flask搭建的博客，[系列教程](https://www.webskill.cn/post/环境的配置)**

<br>

运行教程

**第一步，下载完解压文件**  

<br>

**第二步，配置环境**

(选项1): Windows
``` bash
cd flask-blog-0.1  # 进入flask-blog-master目录
python3 -m venv venv  # 新建一个python3虚拟环境
venv\Scripts\activate.bat # 激活虚拟环境 （Windows）
pip install -r requirements.txt  # 安装python的依赖包
```

(选项2): Linux或Mac
``` bash
cd flask-blog-master  # 进入flask-blog-master目录
python3 -m venv venv  # 新建一个python3虚拟环境
source venv/bin/activate  # 激活虚拟环境
pip install -r requirements.txt  # 安装python的依赖包
```


<br>

**第三步，启动flask-blog**

(选项1): Windows
``` bash
set FLASK_APP=application
flask run
```

(选项2): Linux或Mac
``` bash
export FLASK_APP=application
flask run
```

打开 [127.0.0.1:5000/index](http://127.0.0.1:5000/index)
