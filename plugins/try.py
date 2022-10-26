import requests

cookies = {
    'language': 'en',
    'welcomebanner_status': 'dismiss',
}

headers = {
    'Host': 'localhost:3000',
    'sec-ch-ua': '"Chromium";v="103", ".Not/A)Brand";v="99"',
    'Accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36',
    'sec-ch-ua-platform': '"Linux"',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'http://localhost:3000/',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'If-None-Match': 'W/"325f-ZyA0JRBgBO6uelkCE2/kgOaVJBU"',
    'Connection': 'close',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'language=en; welcomebanner_status=dismiss',
}

params = {
    'q': 'xx',
}

response = requests.get('http://localhost:3000/rest/products/search', params=params, cookies=cookies, headers=headers, verify=False)
print(response)