import requests


def zoomeye_domain_search(domian):
    headers = {
        'API-KEY': '你的API-KEY'
    }
    page = 1  # 初始化page值为1
    domain_list = []  # 用于存储每页的子域名
    ip_list = []  # 用于存储每页子域名的IP地址
    while True:
        url = "https://api.zoomeye.org/domain/search?q=" + domian + "&page=" + str(page) + "&type=1"
        response = requests.get(url, headers=headers)  # 发送get请求，附带自定义http头
        result = response.json()
        if result['list'] == []:
            break

        for i in result['list']:  # 提取list中的数据
            domain_list.append(i['name'])  # 提取子域名
            ip_list.append(i['ip'])  # 提取ip

        page = page + 1  # 控制页码

    return domain_list, ip_list


if __name__ == "__main__":
    domain = input("请输入查询的域名：")
    domain_list, ip_list = zoomeye_domain_search(domain)

for i in range(len(domain_list)):  # 输出结果
    print(domain_list[i], ip_list[i])
