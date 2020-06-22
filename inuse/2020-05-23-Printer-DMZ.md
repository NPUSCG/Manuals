---
title: "通过路由器共享打印机"
date: 2020-05-23T22:35:04+08:00
draft: false
tags:
    - 网络打印机
    - DMZ
    - 端口转发
---

网页版发布在: <https://lrtfm.gitlab.io//2020/05/printer-dmz/>

由于办公室内打印机不能自动获取所在网络 IP (连接网络需要拨号认证), 导致该打印机不能作为网络打印机使用.
所以 [polossk](https://github.com/polossk) 决定使用添加一个路由器连接该打印机, 以实现网络共享, 随即下单购买了某米的路由器.

配置完成后办公室网络拓扑结构如下:
![](https://raw.githubusercontent.com/NPUSCG/ImageCDN-Storage/master/2020/05/23/net-printer.png)

| 名称   | 型号                       |
| ------ | -------------------------- |
| 打印机 | HP LaserJet Pro MFP M126nw |
| 路由器 | 米路由器4A千兆版(R4A)      |

## 路由配置

1. 路由器上网
   路由器的上网设置中, 设置使用 PPPoE 拨号上网. 路由器联网后自动获取到 IP 地址为 10.70.148.60.
2. 打印机设置固定 IP
   在路由器的 DHCP 静态IP 分配中, 设置打印机的静态 IP 为 192.168.31.233.
3. 端口转发(以下方式任选)
   配置端口转发功能以便 **主机 A** 和 **主机 B** 可以访问打印机.
    1. 开启 DMZ (Demilitarized zone, 隔离区, 非军事化区) 功能
       在 **高级设置 -> 端口转发 -> DMZ** 中打开 DMZ 设置, 并填写IP为 192.168.31.233. 这样的效果是访问地址
       10.70.148.60 的所有连接都会转发到地址 192.168.31.233, 即打印机. 

    2. 端口转发
       在端口转发设置中, 转发端口 **3910,3911** 和 **9100** 到打印机 F, 即 192.168.31.233. 关于端口的详细描述, 请参考
       [HP Web Jetadmin - Ports](https://support.hp.com/lv-en/document/c05996543).

       | 端口       | 协议 | 描述                   |
       | ---------- | ---- | ---------------------- |
       | 3910, 3911 | TCP  | 获取打印请求和打印状态 |
       | 9100       | TCP  | 传输打印内容等         |

    如果不需要外网访问局域网内其他主机, 选择 DMZ 功能最为方便, 而设置端口转发则较为灵活, 同时也更安全. 

## PC 连接打印机

### 在主机 A 和 B 上设置连接打印机

在 **Windows 设置 -> 设备 -> 打印机与扫描仪** 中选择 **添加打印机或扫描仪**, 按如下步骤设置.

1. 选择 **添加打印机或扫描仪** 后, Windows 会开始自动搜索, 然后会有类似如下的显示, 
   选择**我需要的打印机不在列表中** (为啥找不到我们要找的打印机呢?).

   ![A](https://raw.githubusercontent.com/NPUSCG/ImageCDN-Storage/master/2020/05/23/add-printer-A.png)

2. 下面我们有两种方式, 如图红色部分, 我们选择 **通过手动...**

   ![B](https://raw.githubusercontent.com/NPUSCG/ImageCDN-Storage/master/2020/05/23/add-printer-B.png)

3. 然后我们创建新端口, 并选择 **Standard TCP/IP Port**
   
   ![C](https://raw.githubusercontent.com/NPUSCG/ImageCDN-Storage/master/2020/05/23/add-printer-C.png)

4. 填写主机名为路由器的 IP 地址 10.70.148.60. 端口名称默认就可以, 可以不用更改, 
   这个名称并非是填写端口号的, 它只是 Windows 用来标记和某个打印机的通讯方式的. 

   ![D](https://raw.githubusercontent.com/NPUSCG/ImageCDN-Storage/master/2020/05/23/add-printer-D.png)

   这里也可以勾选 **查询打印机并自动选择要使用的打印机驱动程序.

5. 安装打印机驱动程序, 选择和打印机相应的驱动, 我们的选择如下图.

   ![E](https://raw.githubusercontent.com/NPUSCG/ImageCDN-Storage/master/2020/05/23/add-printer-E.png)
   ![F](https://raw.githubusercontent.com/NPUSCG/ImageCDN-Storage/master/2020/05/23/add-printer-F.png)

6. 设置打印机名称 (默认就好)

   ![G](https://raw.githubusercontent.com/NPUSCG/ImageCDN-Storage/master/2020/05/23/add-printer-G.png)

7. 设置共享方式, 根据情况, 这里我们不共享.

   ![H](https://raw.githubusercontent.com/NPUSCG/ImageCDN-Storage/master/2020/05/23/add-printer-H.png)

8. 完成, 这里可以打印测试页测试.
   
   ![I](https://raw.githubusercontent.com/NPUSCG/ImageCDN-Storage/master/2020/05/23/add-printer-I.png)

9. 之后查看打印机和扫描仪即可看到刚添加的打印机

   ![J](https://raw.githubusercontent.com/NPUSCG/ImageCDN-Storage/master/2020/05/23/add-printer-J.png)

到这里设置就完成了.
