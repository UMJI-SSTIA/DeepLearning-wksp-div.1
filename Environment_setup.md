# 环境配置指南

## 安装 PyCharm

PyCharm 是由 JetBrains 开发的一款强大的 Python IDE。PyCharm 使用其自己的虚拟环境管理器，便于环境管理。

1. #### 访问 PyCharm 官网:
   
   访问 [PyCharm 官网](https://www.jetbrains.com/pycharm/download/) ，从“Developer Tools”一栏找到“PyCharm”，点击“Download”。
![img.png](img/Envrionment_setup_img/img.png)
2. #### 选择版本:
   
   **Professional**（专业版，收费）  
   学生认证教程：https://lic.sjtu.edu.cn/Default/index  
   **Community**（社区版，免费）  
   也可使用
   

3. #### 开始安装:
   
   双击安装程序文本，根据向导开始安装，确保安装在自己找得到的目录
![img_3.png](img/Envrionment_setup_img/img_3.png)
![img_1.png](img/Envrionment_setup_img/img_1.png)
![img_2.png](img/Envrionment_setup_img/img_2.png)


## 安装 Anaconda（非必须）

Anaconda 是一个免费且开源的 Python 和 R 语言的发行版。Anaconda附带了一大批常用的数据科学包，不需要使用pip进行下载；
自带的conda是包管理器和环境管理器，可以减少未来遇到的各种库和版本的问题。

### 推荐安装教程：
https://blog.csdn.net/fan18317517352/article/details/123035625

### 创建虚拟环境

1. #### 打开 Anaconda Prompt:
   
   在开始菜单中找到 Anaconda Prompt 并打开。

2. #### 创建新的虚拟环境:
   
   使用以下命令创建一个新的虚拟环境，其中 `your_env_name` 是你为虚拟环境选择的名称，`python=3.9` 指定了 Python 的版本。
   
   ```bash
   conda create --n your_env_name python=3.9

3. #### 进入虚拟环境：
   ```bash
   conda activate your_env_name
   
4. #### 退出该虚拟环境：
   ```bash
   conda deactivate
   
上述操作也可在pycharm里的终端完成
   
## 参考资料
pycharm安装：https://blog.csdn.net/qq_32892383/article/details/116137730  

anaconda安装：
https://blog.csdn.net/fan18317517352/article/details/123035625