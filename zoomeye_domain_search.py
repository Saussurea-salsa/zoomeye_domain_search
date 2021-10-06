import requests


def zoomeye_domain_search(domian):
    headers = {
        'API-KEY': '你的API-KEY'
    }
    page = 1  
    domain_list = []  
    ip_list = [] 
    while True:
        url = "https://api.zoomeye.org/domain/search?q=" + domian + "&page=" + str(page) + "&type=1"
        response = requests.get(url, headers=headers)  
        result = response.json()
        if result['list'] == []:
            break

        for i in result['list']:  
            domain_list.append(i['name'])  
            ip_list.append(i['ip']) 

        page = page + 1  

    return domain_list, ip_list


if __name__ == "__main__":
    domain = input("请输入查询的域名：")
    domain_list, ip_list = zoomeye_domain_search(domain)

for i in range(len(domain_list)): 
    print(domain_list[i], ip_list[i])
