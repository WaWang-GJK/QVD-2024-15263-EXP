0x01 漏洞描述

禅道项目管理系统存在身份认证绕过漏洞（QVD-2024-15263），远程攻击者利用该漏洞可以绕过身份认证，调用任意API接口并修改管理员用户的密码，并以管理员用户登录该系统，配合其他漏洞进一步利用后，可以实现完全接管服务器。

0x02 漏洞影响版本

16.0 <= 禅道项目管理系统 <=18.11（开源版）

6.0  <= 禅道项目管理系统 <=8.11 （企业版）

3.0  <= 禅道项目管理系统 <=4.11（旗舰版）

0x03 工具使用

1、将批量目标放在url.txt中，每行一个

2、运行环境：python3

3、运行：python3 run.py

4、等待程序运行结束即可，默认添加用户：usertest，密码：123qwe!@#
