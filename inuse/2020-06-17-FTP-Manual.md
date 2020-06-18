# FTP 相关

## 基本操作

### 获取相关软件

所使用的的软件的FileZilla（客户端和服务端）为免费软件，可以访问其官网<https://filezilla-project.org/>，中文官网<https://www.filezilla.cn/>。从中获取对应的服务端软件（如图所示给出的详细文件信息）和客户端软件。

**注意**：FileZilla服务端仅仅支持window平台。

![img01](C:\Users\lsa\Documents\GitHub\Manuals\images\2020-06-17-FTP-Manual-01.png)

### 安装FileZilla

**注意**：所有安装按默认操作即可，建议不要修改其中的参数；软件安装以及配置过程，中文版和英文版基本一样。

1. 引导界面

   ![img02](C:\Users\lsa\Documents\GitHub\Manuals\images\2020-06-17-FTP-Manual-02.png)

2. 选择安装内容界面

   ![imag03](C:\Users\lsa\Documents\GitHub\Manuals\images\2020-06-17-FTP-Manual-03.png)

3. 修改安装路径界面

   ![imag04](C:\Users\lsa\Documents\GitHub\Manuals\images\2020-06-17-FTP-Manual-04.png)

4. 服务启动配置界面

   ![imag05](C:\Users\lsa\Documents\GitHub\Manuals\images\2020-06-17-FTP-Manual-05.png)

5. 安装完成，首次启动界面

   ![imag6](C:\Users\lsa\Documents\GitHub\Manuals\images\2020-06-17-FTP-Manual-06.png)

6. 设置密码（其他信息建议不要改动），勾选总是访问这个服务，点击连接（Connect），顺利启动FTP服务。（若有警告，参考被动模式设置，完成该项设置就无警告了）。

   ![imag07](C:\Users\lsa\Documents\GitHub\Manuals\images\2020-06-17-FTP-Manual-07.png)

## 服务端配置

> 以下是在window 10 平台上配置FileZilla server的步骤

### 用户组设置

**注意**：通过用户组设置权限可以很好的管理用户，在新建用户时选择对应的用户组，就不需要对每个用户进行设置，减少工作量。

1. 点击主界面的Edit（编辑）选择Groups（用户组）按钮

   ![imag08](C:\Users\lsa\Documents\GitHub\Manuals\images\2020-06-17-FTP-Manual-08.png)

2. 选择general（通用）按钮，选择右边的add（添加）按钮，输入用户组名称test，其余设置默认

   ![imag09](C:\Users\lsa\Documents\GitHub\Manuals\images\2020-06-17-FTP-Manual-09.png)

3. 选择Shared folders（文件路径），点击左边的add，添加用户组对应的文件夹路径，默认第一次添加的路径为ftp用户访问时的主目录，根据需求选择中间的权限设置

   ![imag10](C:\Users\lsa\Documents\GitHub\Manuals\images\2020-06-17-FTP-Manual-10.png)

4. 点击ok完成用户组配置

### 用户添加

1. 点击主界面的设置按钮，选择Users（用户）按钮（这一步与与用户组第一步操作类似）

2. 选择general（通用）按钮，选择右边的add（添加）按钮，输入用户名称test，选择设置好的用户组，添加密码，其余设置默认

   ![imag11](C:\Users\lsa\Documents\GitHub\Manuals\images\2020-06-17-FTP-Manual-11.png)

3. 选择Shared folders（文件路径），可以点击左边的add，添加用户可以访问文件夹路径，根据需求选择中间的权限设置。若此处不添加任何路径，就以对应用户组的路径为默认路径。

   ![imag12](C:\Users\lsa\Documents\GitHub\Manuals\images\2020-06-17-FTP-Manual-12.png)

4. 点击ok完成用户组配置

### 安全证书配置

1. 点击Edit（编辑），选择设置，进入设置界面

   ![imag13](C:\Users\lsa\Documents\GitHub\Manuals\images\2020-06-17-FTP-Manual-13.png)

2. 选择FTP over TLS settings

   ![imag14](C:\Users\lsa\Documents\GitHub\Manuals\images\2020-06-17-FTP-Manual-14.png)

3. 选择界面中的generate new certificate按钮，得到如下界面

   ![imag15](C:\Users\lsa\Documents\GitHub\Manuals\images\2020-06-17-FTP-Manual-15.png)

4. 可以根据情况填写相关信息（如果有相应的证书信息，county code必填），然后选择证书保存路径，没有就直接点击Generate certificate按钮，在点击确定，完成证书生成。

   ![imag16](C:\Users\lsa\Documents\GitHub\Manuals\images\2020-06-17-FTP-Manual-16.png)

5. 再点击ok完成安全证书配置。

   ![imag17](C:\Users\lsa\Documents\GitHub\Manuals\images\2020-06-17-FTP-Manual-17.png)

### 防火墙设置

1. 在window搜索工具中搜索防火墙设置

   ![imag18](C:\Users\lsa\Documents\GitHub\Manuals\images\2020-06-17-FTP-Manual-18.png)

2. 点击允许应用通过防火墙，从列表中选择Filellize相关的项目

   ![imag19](C:\Users\lsa\Documents\GitHub\Manuals\images\2020-06-17-FTP-Manual-21.png)

3. 如果没有找到，先选择更改设置，再选择允许其他应用，选择安装软件的路径，点击添加按钮

   ![imag20](C:\Users\lsa\Documents\GitHub\Manuals\images\2020-06-17-FTP-Manual-20.png)

4. 添加完成后，将对应的专用和公用都勾上，点击确定，完成防火墙配置。

   ![imag21](C:\Users\lsa\Documents\GitHub\Manuals\images\2020-06-17-FTP-Manual-19.png)

### 其他相关设置

#### 被动模式设置

1. 选择设置栏中的passive mode settings

2. 勾选 use the following IP，在输入框中填写本机IP地址（查阅本机ip地址，可以在cmd中输入ipconfig可以查看），点击ok，完成配置。

   ![imag22](C:\Users\lsa\Documents\GitHub\Manuals\images\2020-06-17-FTP-Manual-22.png)

## 其他注意事项

1. 需要合理设置普通用户权限，管理员权限，防止文件误删。
2. 需要给用户强调上传文件是一定要弄清楚，一旦上传不可修改。
3. 需要给使用者除密码和用户名外，还需要提供IP地址。
4. 在不需要使用时，将客户端关闭，减少宽带占用。
5. 需要强调错开高峰上传文件，分批传文件。

## 扩展

- [ ] 以上给出的ftp服务是搭建在window平台上的，将来若需要迁移到linux平台上，可以考虑使用vsftpd。
- [ ] 在ftp服务上有经验分享内容，可以使用Hugo在window上搭建博客系统，方便查阅信息。