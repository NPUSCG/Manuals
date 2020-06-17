# Markdown 手册

## 环境配置

### VSCode 设置

1. 搜索安装并启用  `Markdown All in One` 插件
2. 依次打开 `File -> Preferences -> Settings`，搜索 `math` 找到该插件的“启用基本的数学支持”，将选项打开，即 `"markdown.extension.math.enabled": true`
3. （可选）依次打开 `File -> Preferences -> User Snippets`，选择 `New Global Snippets File` 来新建一份全局用户代码段，输入文件名之后，你的编辑器会创建一份默认用户代码片段模板，然后复制粘贴如下内容
```json
{
    "Environment": {
        "scope": "latex,markdown",
        "prefix": "begin",
        "body": [
            "\\begin{$1}\n\t$2\n\\end{$1}\n$0",
        ],
        "description": "Insert New Environment"
    }
}
```
4. （可选）如果对数学公式有其他更严格的要求，搜索安装并启用 `Markdown+Math` 插件，然后关闭第二步中 `Markdown All in One` 的“基本的数学支持”，并且根据插件介绍自行配置

### Typora 设置

1. 依次打开  `File -> Preferences`，在 `General` 选项卡中勾选 `Auto Save` 保持自动保存
2. 切换至 `Markdown` 选项卡，勾选 `Sritct Mode`，并根据个人喜好选择默认的 `Heading Style`，`Unordered List`，`Ordered List` 语法格式
2. 勾选 `Syntax Support` 中的 `Inline Math` 行内公式支持
3. 勾选 `Code Fences` 中的 `Display line numbers for code fences` 显示行号，并自行调整默认缩进字符数量（推荐设置为 4）

## 基本语法说明

### 标题

1. 使用 `#` 号
    ```markdown
    # 一级标题
    ## 二级标题
    ### 三级标题
    #### 四级标题
    ##### 五级标题
    ###### 六级标题
    ```

2. 使用 `====` 或 `----` 分割线
    ```markdown
    一级标题
    ================
    正文
    
    二级标题
    ----------------
    正文
    ```

### 列表

1. 有序列表
    ```markdown
    1. 列表 1
    2. 列表 2
       1. 子列表 1
       2. 子列表 2
    3. 列表 3
    ```

    1. 列表 1
    2. 列表 2
       1. 子列表 1
       2. 子列表 2
    3. 列表 3

2. 无序列表
    ```markdown
    * 无序列表可以用提示符加空格进行标记
    * 提示符可以是三种之一
      * 星号 `*`
      * 加号 `+`
      * 减号 `-` 
    * 同一个列表内部应当保持同一个提示符
    ```

    * 无序列表可以用提示符加空格进行标记
    * 提示符可以是三种之一
      * 星号 `*`
      * 加号 `+`
      * 减号 `-` 
    * 同一个列表内部应当保持同一个提示符

3. 待办列表
    ```markdown
    * [x] 待办事项 1
    * [ ] 待办事项 2
      * [ ] 待办事项 2.1
      * [x] 待办事项 2.2
    * [ ] 待办事项 3
    ```

    * [x] 待办事项 1
    * [ ] 待办事项 2
      * [ ] 待办事项 2.1
      * [x] 待办事项 2.2
    * [ ] 待办事项 3

### 强调

|                      格式                       |                    效果                     |
| :---------------------------------------------: | :-----------------------------------------: |
|            `**加粗**` 或 `__加粗__`             |            **加粗** 或 __加粗__             |
|              `*倾斜*` 或 `_倾斜_`               |              *倾斜* 或 _倾斜_               |
| `*__加粗倾斜__*` 或 `**_加粗倾斜_**` 等类似组合 | *__加粗倾斜__* 或 **_加粗倾斜_** 等类似组合 |
|                  `` `等宽` ``                   |                   `等宽`                    |
|                 `~~删除横线~~`                  |                ~~删除横线~~                 |

### 特殊块

1. 代码块
    ````markdown
    ​```python
    def fib(n):
        return 1 if n <= 1 else fib(n - 1) + fib(n - 2)
            
    print(fib(5))
    ​```
    ````
    ```python
    def fib(n):
        return 1 if n <= 1 else fib(n - 1) + fib(n - 2)

    print(fib(5))
    ```

2. 引用块 `quote`
    ```markdown
    > Stay Hungry Stay Foolish. --Steve Jobs
    ```

    > Stay Hungry Stay Foolish. --Steve Jobs

3. 表格块
   
    ```markdown
    | Raggedright   | Centering |     Raggedleft |
    | :------------ | :-------: | -------------: |
    | Left          |  Center   |          Right |
    | Aligning left | Centering | Aligning Right |
    ```

    | Raggedright   | Centering |     Raggedleft |
    | :------------ | :-------: | -------------: |
    | Left          |  Center   |          Right |
    | Aligning left | Centering | Aligning Right |

### 超链接

1. 就地链接写法
    ```markdown
    <https://github.com/>
    ```

    <https://github.com/>

2. 超链接写法
    ```markdown
    只需要点击 [GitHub](https://github.com/) 即可访问
    ```

    只需要点击 [GitHub](https://github.com/) 即可访问

3. 汇总链接写法
    ```markdown
    关于 [GitHub][ref01] 以及 [git][ref02] 的使用可以点击超链接进一步查看
    <!-- References: -->
    [ref01]: https://github.com/ "GitHub is how people build software"
    [ref02]: https://git-scm.com/ "git --distributed-is-the-new-centralized"
    ```

    关于 [GitHub][ref01] 以及 [git][ref02] 的使用可以点击超链接进一步查看

### 插图

```markdown
![img01](https://desktop.github.com/images/desktop-icon.svg)
```

![img01](https://desktop.github.com/images/desktop-icon.svg)


## 数学公式说明

### 行内公式

```markdown
行内编写时一般不要出现分式，如 $\frac34$、$\frac1{\mathrm e}$、$\frac{\pi}{2}$ 这种，不仅显着紧凑局促，而且也不易阅读。应当尽量使用 $3/4$、${\mathrm e}^{-1}$、$\pi / 2$ 这种简单形式，保持文字排版的整齐与美观。
```

行内编写时一般不要出现分式，如 $\frac34$、$\frac1{\mathrm e}$、$\frac{\pi}{2}$ 这种，不仅显着紧凑局促，而且也不易阅读。应当尽量使用 $3/4$、${\mathrm e}^{-1}$、$\pi / 2$ 这种简单形式，保持文字排版的整齐与美观。

### 行间公式

```markdown
遇到大段的公式，或者是较为重要的公式时，应当使用行间公式将其从文章段落当中独立出来，这样更方便读者阅读与把握重点。比如欧拉公式
$$
\begin{equation}
{\mathrm e}^{{\mathrm i}\theta} = \cos \theta + {\mathrm i} \sin \theta
\label{eq:eular}
\end{equation}
$$
如果取 $\theta = \pi$ 则 $\eqref{eq:eular}$ 可以化简为更简单的形式
$$
\begin{equation}
{\mathrm e}^{{\mathrm i}\pi} + 1 = 0
\label{eq:eular-sp}
\end{equation}
$$
$\eqref{eq:eular-sp}$ 也被称作世界上最美的公式之一。整个公式用到了自然数单位 1，虚数单位 ${\mathrm i}$，自然对数 ${\mathrm e}$，圆周率 $\pi$，以及有理数 0。这 5 个数字的背后是人类从简单计数逐渐迈入到更高深的数学领域这一求知之路的一个缩影。
```

遇到大段的公式，或者是较为重要的公式时，应当使用行间公式将其从文章段落当中独立出来，这样更方便读者阅读与把握重点。比如欧拉公式
$$
\begin{equation}
{\mathrm e}^{{\mathrm i}\theta} = \cos \theta + {\mathrm i} \sin \theta
\label{eq:eular}
\end{equation}
$$
如果取 $\theta = \pi$ 则 $\eqref{eq:eular}$ 可以化简为更简单的形式
$$
\begin{equation}
{\mathrm e}^{{\mathrm i}\pi} + 1 = 0
\label{eq:eular-sp}
\end{equation}
$$
$\eqref{eq:eular-sp}$ 也被称作世界上最美的公式之一。整个公式用到了自然数单位 1，虚数单位 ${\mathrm i}$，自然对数 ${\mathrm e}$，圆周率 $\pi$，以及有理数 0。这 5 个数字的背后是人类从简单计数逐渐迈入到更高深的数学领域这一求知之路的一个缩影。


<!-- References: -->
[ref01]: https://github.com/ "GitHub is how people build software"
[ref02]: https://git-scm.com/ "git --distributed-is-the-new-centralized"
