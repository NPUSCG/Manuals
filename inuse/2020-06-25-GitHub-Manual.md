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
#### 1.2.1 GitHub Desktop
在GitHub Desktop中依次选择菜单`File\New repository`，也可以使用快捷键`Ctrl+N`。如下图：

![img01](../images/2020-06-25-GitHub-Manual-01.png)

点击`New repository`后，会弹出如下图所示的窗口。

![img02](../images/2020-06-25-GitHub-Manual-02.png)

1. 新创建的仓库的名称；
2. 对新创建仓库的简要描述。在 GitHub 网页上，该描述会显示在仓库名的下方；
3. 新建仓库在本地的储存位置。GitHub Desktop 会在该路径下创建与项目名同名的文件夹，并将仓库中的内容存放在创建的文件夹中；
4. 自动生成一个 README.md 文件并添加在仓库中。在自动创建的 README.md 中，标题是仓库名称，内容是`Description`栏中的描述；
5. 创建`.gitignore`文件，在之后的上传中，会按照`.gitignore`中的配置忽略相应的文件；
6. 选择一个`license`。关于如何选择合适的`license`，可以参照[这篇文章](https://blog.csdn.net/wadefelix/article/details/6384317)。

点击`Create repository`。如果看到了`Publish repository`按钮亮起，如下图所示，说明本地仓库创建成功。

![img03](../images/2020-06-25-GitHub-Manual-03.png)



#### 1.2.2 Git Bash

> 下面的`bash`代码中，`$`之后的是命令部分，`$`本身不是命令中的内容；没有特殊符号开头的行是上一条命令的执行结果；`#`开头的行是注释。下同。

在目录中执行`git init`命令，就可以在当前目录中创建一个 Git 仓库。比如在用户名为`YourName`的用户主文件夹下创建一个名为`TestRepo`的目录，需要执行如下命令：

```bash
# git init example
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

#### 2.1 命令说明

`git clone`拷贝一个 Git 仓库到本地。拷贝后可以在本地查看或修改该项目。

#### 2.2 使用说明

#### 2.2.1 GitHub Desktop

在GitHub Desktop中依次选择菜单`File\Clone repository`，也可以使用快捷键`Ctrl+Shift+O`。如下图：

![img04](../images/2020-06-25-GitHub-Manual-04.png)

点击`Clone repository`后，会弹出如下图所示的窗口。

![img05](../images/2020-06-25-GitHub-Manual-05.png)

在`GitHub.com`一栏中，可以找到自己账户中的库并克隆到本地。如果是给定 url 的库，需要按上图所示，将仓库的 url 拷贝到文本框 1，在文本框 2 中选择仓库在本地的目录。完成后点击`Clone`按钮即可。

#### 2.2 Git Bash

执行命令

```bash
$ git clone [url]
```

其中 [url] 是你想要复制到本地的项目地址。例如用户名为`YourName`的用户名为`TestRepo`的仓库`https://github.com/YourName/TestRepo.git`。执行如下命令：

```bash
# git clone example
$ git clone https://github.com/YourName/TestRepo.git
Cloning into 'TestRepo'...
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 7 (delta 2), reused 5 (delta 0), pack-reused 0
Unpacking objects: 100% (7/7), done.
```

克隆完成后会在当前目录下生成一个`TestRepo`目录。`git clone`命令默认在当前目录下创建一个与项目同名的目录存放克隆的仓库文件，如果想指定创建的目录名，在`git clone`命令后面添加你想要的名称即可。例如：

```bash
$ git clone https://github.com/YourName/TestRepo.git TestRepoRename
```

上述命令将`TestRepo`仓库克隆到当前目录下名为`TestRepoRename`的目录中。

### 3. `git commit`

#### 3.1 命令说明

`git commit`命令将暂存区里的内容提交到本地仓库中。每次使用`git commit`命令时会生成一个唯一的`commit-id`，在任何时候可以通过这个 id 回退到对应 commit 之前的仓库内容。

### 3.2 使用说明

#### 3.2.1 GitHub Desktop

在 Git 仓库中修改或添加文件后，左侧的 `Changes`一栏会显示对应的修改。例如在`TestRepo`仓库中添加文件`file1.txt`，添加后如下图所示：

![img06](../images/2020-06-25-GitHub-Manual-06.png)

在文本框 1 (Summary)中添加简要描述，在文本框 2 (Description)中添加详细描述。每次提交**必须**要有 Summary， Description 可写可不写。之后点击`Commit`按钮，完成提交。

#### 3.2.2 Git Bash

Git 会为每一次的提交记录用户名和邮箱地址。所以在第一次提交前需要配置用户名和账户地址。

```bash
$ git config --global user.name "YourName"
$ git config --global user.email your@email.com
```

在 Git Bash 中执行`git commit`前，需要先执行`git add`命令将修改的文件添加到暂存区。`git add`命令的使用方式如下：

```bash
$ git add filename1 filename2 ...
```

如果要添加所有改动的文件，可以使用`git add .`命令。

在执行完`git add`后，使用`git commit`指令提交对文件的所有改动。每次提交**必须**要有`-m`选项和提交注释（相当于 GitHub  Desktop 的 Summary 文本框）。例如在`TestRepo`仓库中添加文件`file2.txt`，执行如下命令：

```bash
# git commit example
$ git add .
$ git commit -m "Add a new file."
[master c5e1c51] Add a new file.
 1 file changed, 1 insertion(+)
 create mode 100644 file2.txt
```

可以使用`git commit -a`选项跳过`git add`这一步。对应上面的例子：

```bash
# git commit example without `git add .`
$ git commit -am "Add a new file."
[master 89c1b4b] Add a new file.
 1 file changed, 1 insertion(+)
```



# TODO:

* [x] init
* [x] clone
* [x] commit
* [ ] branch
* [ ] push 
* [ ] pull 
* [ ] checkout 
* [ ] merge
* [ ] 一份简单的 git 命令的 cheatsheet
