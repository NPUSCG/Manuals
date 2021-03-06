# 公共存储

## 使用场景

1. **组内汇报 / 报告：** 课题组邀请老师 A 或组内学生 B 面向组内作报告时，PPT 是我们重要的学习资料，应当对其进行归档、分类、和保存，以备不时之需（文献调研与整理、思路创新的借鉴与参考等）；
2. **组内私有资料：** 目前组内已经有了一部分私有的学习生产资料（如已毕业师兄师姐的论文、代码），应当对这些科研成果更方便的传递给新入学的师弟师妹们，并且防止他人的抄袭剽窃（尤其是代码）；
3. **科研能力培训：** 目前组内尚没有系统的科研能力培训方案，应当把已有的部分参考资料、手稿笔记加以整合，来方便我们建立起一套快速的行之有效的系统的培训方案；
4. **科研进度汇报：** 现在周总结的汇总与整理由大总管及小组长负责，可以将流程进一步简化，每人定期上传科研进度汇报至指定文件夹即可，让小组长只负责监督谁没交而不再负责收取任务；
5. **常用资料软件：** 部分专业书籍电子版、经典文献、正在阅读的论文等，以及常用软件和配置说明可以整合管理，方便新生下载；正在一起撰写的文章 / 本子 / 代码也可以通过这一存储方式来进行协作与管理。

## 核心需求

为了方便明确使用需求，我们将用户按具体操作分成两类：一般用户（上传 / 下载 / 检索）、管理员（整理 / 更新 / 删除）。

* 一般用户
  * 文件上传 / 下载应当尽可能操作简单、快捷
  * 可能的文件类型有：文档类（pdf/doc/ppt/xls）、代码类（源码或打包）、软件类（安装包或光盘镜像）
  * 文件的分类应明晰、准确，最好支持查找检索
* 管理者
  * 应当建立整齐的文件目录树，并规范命名文件以方便文件检索命中关键词
  * 必要时对存储的软件进行更新，对旧版本及时删除
  * 对文档类应当做到至少每月整理一次，保持文件实时性

### 目标

总结整理，实质上的目标有四个<a href name="purposes"></a>：

1. 会议报告与组内汇报 PPT 的整理，科研进度汇报的收取；
2. 学术文献的汇总与整理；
3. 文章，申请书，软件代码的版本控制与多人协作；
4. 软件使用说明，与其他学习资料等。

因此整理出如下考察指标：难易程度（学习成本），带宽速度，是否支持校外访问，是否支持文件搜索，是否支持部分存储，是否支持实时更新，是否支持大文件存储。

## 可行软件

目前考察的软件工具有三种：坚果云（或其他网盘）个人版本，教研室 FTP 服务器，GitHub 私有仓库，现一一说明。

* **坚果云（或其他网盘）个人版本：** 网络存储空间的最大优点在于网络上稳定存储一个副本，可以在任意场合访问。同时，网盘普遍提供了文件搜索服务，对文档类文件的支持较好。对于大型软件安装包可能会占用大量带宽，普遍速度一般。免费版本可能不能支持较大的网络空间和多人协同处理。
* **校内 FTP 服务器：** 由于是部署在内网，所以不需要考虑校内的网络带宽问题。FTP 服务普遍不支持文件搜索功能。同时由于技术较老，一般不支持实时更新。FTP 的优点在于服务器实体就在校内，可以利用之前的废旧电脑，也可以安排多用户协同工作，而且方便大文件的传输（网速出口受限时可以通过 USB 传文件）。缺点在于如果需要校外访问，则需要安装 VPN 来访问校内资源。
* **GitHub 私有仓库：** GitHub 是典型的代码版本控制软件，国内公司的普及度较好（互联网公司及软件开发公司面试加分项），可以做到基础的文件搜索、代码内搜索，同时可以支持多人协同。缺点在于由于 [GitHub.com](http://github.com) 网站在国外服务器上，国内的特殊网络环境可能不能保障其健壮的网络连通性。另外由于 GitHub 的设计理念是开源共享，所以对于免费用户的私有仓库多人协同有人数限制。不过可以通过自己搭建 Git 服务器（如 [Gitblit](http://gitblit.github.io/gitblit/) 软件）来解决这一问题。

结合刚才的需求与软件的具体情况，可以得到对比表格如下所示。

|   考察指标   |    网盘    | FTP 服务器 | GitHub 私有仓库 | Git 服务器 |
| :----------: | :--------: | :--------: | :-------------: | :--------: |
|   学习成本   |    简单    |    中等    |      较难       |    较难    |
|   带宽速度   |    中等    |    最快    |      较慢       |    最快    |
|   校外访问   |    支持    |   否`*`    |      支持       |    否*     |
|   文件搜索   |    支持    |  部分`**`  |      支持       |    支持    |
|   版本控制   | 部分`***`  |     否     |      支持       |    支持    |
|   部分存储   |    支持    |    支持    |       否        |     否     |
|   实时更新   |    支持    |     否     |       否        |     否     |
|   文档存储   |    很好    |    很好    |      很好       |    很好    |
|   代码存储   | 一般`****` | 一般`****` |      很好       |    很好    |
|  大文件存储  |    支持    |    支持    |       否        |   不建议   |
| 最多协同数量 |     1      |   无上限   |    3`*****`     |   无上限   |

> `*` 访问校内资源需要安装 VPN 软件
> 
> `**` FTP 只可以在实际存储的计算机，或已经完全遍历文件目录树的客户端上搜索
> 
> `***` 因网盘而异，部分网盘支持文档文件的版本回溯
> 
> `****` 如果存储源代码文件会造成大量文件碎片，会对文件传输造成影响；另外与 GitHub 相比，不支持代码内搜索功能
> 
> `*****` 教育网邮箱可以申请 GitHub 学生优惠，免费使用 Pro 版本，此时私有仓库不再有人数限制

## 解决方案

针对之前所定的 [目标](#%e7%9b%ae%e6%a0%87) 我目前提出以下的解决方案：

1. 用教研室的旧电脑分别开两个服务器（考虑到旧电脑的性能），一个为 FTP 服务器，另一个为 Git 服务器，来做数据存储。
2. 针对汇报 PPT 的整理与保存，由会议相关助理负责处理。主要工作为将 PPT 规范命名（如“2020-03-03-报告人-报告题目”），并整理到相关主题的文件夹中（如“学生报告”、“数值方法相关”、“数据分析相关”等）。
3. 针对论文文献与专业书籍的整理与保存，可以借助第三方工具（如 [EndNote](https://endnote.com/)）进行分类管理，然后将仓库数据上传至 FTP 服务器中，这样任何想查阅文献的同学可以自行下载仓库副本，通过第三方工具进行查询。
4. 针对多人协同工作问题，可以先在 Git 服务器上安排账户与工作仓库，然后由这些人来协商控制版本及工作进度，必要时老板可以参与并监督。
5. 针对软件的安装包，由于我们学校内部有 PT 资源站，所以安装包可以通过 PT 站获取，也可以利用 FTP 服务器存储安装包以方便下载；对于软件的安装或使用说明，由于不涉及私有内容，且为了方便控制格式，个人建议通过 markdown 文档（现有的文档格式最简洁的工具，本文就是 markdown 版本）书写并开源至 GitHub 上，一方面工具简单容易学习并不浪费时间，另一方面可以借此机会学习并掌握 Git 工具。
6. 对于其他学习资料（如组内的讲课、个人的总结、讨论课的论文整理等等），个人建议将其整理成 PPT 或 PDF 文档，然后自主规范命名（如“2020-03-03-主题-题目”），并整理到对应文件夹中。
7. 如有必要（比如文档类数据）可以直接让 FTP 服务器与网盘服务器同步，以达到多设备多地点的访问目的。

为了完成这一目标，我预计至少需要 3 位同学进行启动，2 位同学做日常维护工作，具体安排如下：

1. 整套系统的正常启动需要 3 位同学：一名同学负责建立与维护论文文献库，并讲解第三方软件的使用方法；FTP一名同学负责 FTP 工具的讲解与 FTP 服务器建立；一名同学负责 Git 工具的讲解与 Git 服务器建立。
2. 整套系统的后期日常维护需要 2 位同学：一名同学负责维护各种软件安装使用说明（如文献管理，FTP，Git 等）；一名同学负责整理其他的学习资料与 FTP 服务器的日常维护（如账号的销毁与新建，数据的备份等）；
3. 会议相关助理只需要整理会议报告 PPT；
4. 其他同学在系统建立并拥有自己的账号之后，就可以正常使用；后续的工作也可以依托此平台来完成（如收取周总结、上传讨论课文献等）

## 具体安排

### 名词解释

* 软件使用说明
  * 使用说明应当尽可能的简洁，直观。
  * 软件使用说明应包含两部分：安装部分和实际操作部分。部分操作如果文字描述不清晰可以截图然后放在文档中。
  * 文档格式推荐使用 markdown，格式简单且方便变更为其他必要的文档格式。如果 markdown 使用不熟练可以学习（难度小于 latex），或者用 word 制作，后期由我转成markdown 文档。
* 文献、电子书、学习资料的命名方式
  * 这里讨论的命名方式是为了在文件浏览器中更直接的查找文档拟定的规则。
  * 文献的建议命名方式为：“年份-题目.pdf”。
  * 电子书的命名方式为：“领域名-书名-作者.pdf”。
  * 学习资料的命名方式为：“类型-题目”。类型举例有：课件、手稿、代码等。

### 文献整理

* 前期的工作主要为软件的学习与制作一份使用说明
  * [ ] 学习使用文献管理软件 [EndNote](https://endnote.com/)
  * [ ] 一份 [EndNote](https://endnote.com/) 的简要使用说明
  * [ ] 必要时需要给课题组全体讲一下软件的使用
* 后期工作的主要职责包含收集文献，整理论文与电子书，定期发布文献库三个职责
  * 论文需要添加必要的标签，如研究的问题（分数阶、网格剖分）或者文章的重点（应用类、数值分析、数值格式）等
  * 收集文献可直接让两个小组的组员自行添加标签和文章到文献库中，以减少整理文献带来的额外工作量
  * 每月发布一次文献库并上传至 ftp 服务器，发布的内容包含两个，一个是整个文献库的压缩包，另一个是该月度新增的文献
  * 已有的电子书籍统一命名之后按照简单的分类直接放在 FTP 服务器中，后续添加的电子书规范命名之后自行添加即可
* 主要工作量在前期文献的整理上，建议先自己拟定一个命名规则与分类规则，然后多人帮忙一起处理

### FTP 服务器管理

* 前期的工作主要为学习管理 FTP 服务器
  * [ ] 使用 [FileZilla](https://filezilla-project.org/) server 版
  * [ ] 学习如何管理账号（路径分配、权限分配）
  * [ ] 制作一份 FTP 服务的简要使用说明并准备组会时讲解（如有必要）
  * [ ] 设计文件目录树，目前需要管理的内容有三类：文献集、周总结收集整理和部分软件安装包备份
  * [ ] 自己留存一份关于账号管理与路径分配的简要说明，以便给下一个管理员
* 后期的工作主要为数据的维护与整理
  * [ ] 定期整理与备份共享文件夹
  * [ ] 新生账号的创建与毕业人员账号的清理
* 主要工作量在于软件学习与后期的管理

### 教研室内部 Git 服务器管理

* 前期的工作主要为学习管理 Git 服务器
  * [ ] 使用 [Gitblit](http://gitblit.github.io/gitblit/) 建立私有 Git 服务器
  * [ ] 学习如何管理账号（路径分配、权限分配）
  * [ ] 建立 GitHub 公共账号组
  * [ ] 制作一份 Git 服务的简要使用说明并准备组会时讲解（如有必要）
  * [ ] 在 GitHub 公共账号组发布各种软件安装及使用文档
  * [ ] 自己留存一份关于账号管理与服务搭建的简要说明，以便给下一个管理员
* 后期的工作主要为数据的维护与整理
  * [ ] 维护 GitHub 公共账号组的 repo
  * [ ] 新生账号的创建与毕业人员账号的清理
* 主要工作量在于软件学习与后期的管理
