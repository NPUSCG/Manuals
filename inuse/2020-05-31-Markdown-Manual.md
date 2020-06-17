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


