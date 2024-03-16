# 环境配置指南

## 安装 PyCharm

PyCharm 是由 JetBrains 开发的一款强大的 Python IDE。PyCharm 使用其自己的虚拟环境管理器，便于环境管理。

1. #### 访问 PyCharm 官网:
   
   访问 [PyCharm 官网](https://www.jetbrains.com/pycharm/download/) ，从“Developer Tools”一栏找到“PyCharm”，点击“Download”。
   ![img.png](img/Envrionment_setup_img/img.png)
2. #### 选择版本（都可以）:

   **Community**（社区版，免费）
   **Professional**（专业版，收费）
   学生认证教程：https://lic.sjtu.edu.cn/Default/index
   
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
**注意**：如果按照上述链接中的指南操作，记得在这下面这两个步骤之间执行exit()命令，退出python环境
![img.png](img/Envrionment_setup_img/14.png)

### 创建虚拟环境

1. #### 打开 Anaconda Prompt:
   
   在开始菜单中找到 Anaconda Prompt 并打开。

2. #### 创建新的虚拟环境:
   
   使用以下命令创建一个新的虚拟环境，其中 `YourEnvName` 是你为虚拟环境选择的名称，`python=3.9` 指定了 Python 的版本。
   
   由于Pytorch只支持3.8-3.11的Python版本，请创建虚拟环境时的Python版本号。
   
   ```bash
   conda create -n YourEnvName python=3.9 -y
   
3. #### 进入新创建的虚拟环境：
   ```bash
   conda activate YourEnvName
   
4. #### 退出该虚拟环境：
   ```bash
   conda deactivate

### 在Pycharm中使用Anaconda
1. 点击左上角"File"，点击"Open"，打开一个你的工作目录  
如果是初次使用：点击"Open"，打开一个你的工作目录   
![img.png](img/Envrionment_setup_img/11.png)

2. 点击"File"，点击"Settings"

    ![img.png](img/Envrionment_setup_img/4.png)  

3. 在"Project"里找到"Python Interpreter",点击"Add interpreter"  
    ![img_1.png](img/Envrionment_setup_img/5.png)  
4. 选择Conda Environment，点击文件夹图标浏览目录，找到自己Anaconda的安装目录  
    ![img_2.png](img/Envrionment_setup_img/13.png)  
5. 选择Conda Executable， 点击右边的“Load Environments”
    ![img_4.png](img/Envrionment_setup_img/9.png)  
6. 选择刚刚创建的虚拟环境"deepLearning"  
![img_5.png](img/Envrionment_setup_img/10.png)  

或者，你也可以通过以下操作添加interpreter：

![img_6.png](img/Envrionment_setup_img/15.png)

## 安装深度学习框架和其他库

### 1. 激活虚拟环境

激活虚拟环境以在环境中安装相关的库

   ```bash
   conda activate YourEnvName
   ```

你可以通过一下命令判断是否成功切换

``` bash
conda info -e
```

如果在你想激活的环境前有一个“*”，说明已经成功切换

![img7.png](img/Envrionment_setup_img/16.png)

### 2. 安装依赖项

首先，切换目录到clone下来的仓库

接着，运行以下命令

``` bash
conda install cmake ninja
pip install -r requirements.txt
```

由于本次workshop无需用到**torch.distributed**中的内容，因此只安装了common dependencies。如果有需要，可以自行前往[Pytorch](https://github.com/pytorch/pytorch)的仓库进行查阅

### 3.安装深度学习框架

 #### For Windows

对于Windows用户，你需要根据自己的GPU选择对应的版本。

``` bash
# 如果你的GPU是NVIDIA系的，支持CUDA，你可以安装这个版本
# pip
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
# conda
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
```

``` bash
# 如果不是，你需要安装CPU版本
# pip
pip3 install torch torchvision torchaudio
# conda
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```

对于workshop来说，CPU版本绰绰有余。

#### For Mac

``` bash
# pip
pip3 install torch torchvision torchaudio
# conda
conda install pytorch::pytorch torchvision torchaudio -c pytorch
```

### For Linux

与Windows类似，需要判断GPU

```bash
# 如果你的GPU是NVIDIA系的，支持CUDA，你可以安装这个版本
# pip
pip3 install torch torchvision torchaudio
# conda
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
```

``` bash
# 如果不是，你需要安装CPU版本
# pip
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
# conda
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```



## 参考资料

pycharm安装：https://blog.csdn.net/qq_32892383/article/details/116137730  

anaconda安装：https://blog.csdn.net/fan18317517352/article/details/123035625

Pytorch官网： https://pytorch.org

Pytorch仓库：https://github.com/pytorch/pytorch

