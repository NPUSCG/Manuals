# GitHub 相关

## 入门手册

* 官方入门教程 <https://lab.github.com/>
* 部分操作演示 <https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1>

## 代码库相关说明

0. 核心原则，**涉密不上网，上网不涉密**
1. 可以公开的学习资料，比如阅读笔记、操作记录、代码等：个人公开库或组内公开库
2. 正在准备的论文、代码：**务必**使用个人**私有库**或者组内**私有库**
3. 其他自己想储存的内容：自行判断私有与共有库利弊选择是否公开

## 常用命令及概念说明

### 1.  `git init`

#### 1.1 命令说明

`git init`用于在当前目录中创建一个新的本地仓库。

#### 1.2 使用说明
##### 1.2.1 GitHub Desktop
在GitHub Desktop中依次选择菜单`File\New repository`，也可以使用快捷键`Ctrl+N`。如下图：
![img01](../images/2020-6-25-GitHub-Manual-01.png)
点击`New repository`后，会弹出如下图所示的窗口。
![img02](../images/2020-6-25-GitHub-Manual-02.png)

1. 新创建的仓库的名称；
2. 对新创建仓库的简要描述。在 GitHub 网页上，该描述会显示在仓库名的下方；
3. 新建仓库在本地的储存位置。GitHub Desktop 会在该路径下创建与项目名同名的文件夹，并将仓库中的内容存放在创建的文件夹中；
4. 自动生成一个 README.md 文件并添加在仓库中。在自动创建的 README.md 中，标题是仓库名称，内容是`Description`栏中的描述；
5. 创建`.gitignore`文件，在之后的上传中，会按照`.gitignore`中的配置忽略相应的文件；
6. 选择一个`license`。关于如何选择合适的`license`，可以参照[这篇文章](https://blog.csdn.net/wadefelix/article/details/6384317)。

点击`Create repository`。如果看到了`Publish repository`按钮亮起，如下图所示，说明本地仓库创建成功。

![img03](../images/2020-6-25-GitHub-Manual-03.png)

##### 1.2.2 Git Bash

> 下面的`bash`代码中，`$`之后的是命令部分，`$`本身不是命令中的内容；没有特殊符号开头的行是上一条命令的执行结果；`#`开头的行是注释。下同。

在目录中执行`git init`命令，就可以在当前目录中创建一个 Git 仓库。比如在用户名为`YourName`的用户主文件夹下创建一个名为`TestRepo`的目录，需要执行如下命令：

```bash
# git bash example
$ mkdir TestRepo
$ cd TestRepo
$ git init
Initialized empty Git repository in /home/YourName/TestRepo/.git/
```

现在使用`ls -a`命令查看当前文件夹，会发现生成了`.git`子目录，如下：

```bash
$ ls -a
. .. .git
```

说明本地 Git 仓库创建成功。

### 2.  `git clone`





# TODO:

* [x] init
* [ ] clone
* [ ] commit
* [ ] branch
* [ ] push 
* [ ] pull 
* [ ] checkout 
* [ ] merge
* [ ] 一份简单的 git 命令的 cheatsheet