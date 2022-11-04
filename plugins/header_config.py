COOKIE = {
    'language': 'en',
    'welcomebanner_status': 'dismiss',
    'cookieconsent_status': 'dismiss',
    'continueCode': 'pphytRIns8UqHYurh8tMTmFkf4SBt5i9fnSLHWPu9MtrMTpni1ZfkYSVZHJDuE9hbnt1jcxqC9qSMBU4DTJZCqJspaiQMS7XtVVINMTDnCegs8li9Nf18cwOHJx',
    'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MSwidXNlcm5hbWUiOiJjb3Vwb24iLCJlbWFpbCI6ImFkbWluQGp1aWNlLXNoLm9wIiwicGFzc3dvcmQiOiI3MTk2NzkzYzQ2OGQyM2Y4NGZlOWM3ODU3MjRmMGUwMCIsInJvbGUiOiJhZG1pbiIsImRlbHV4ZVRva2VuIjoiIiwibGFzdExvZ2luSXAiOiJ1bmRlZmluZWQiLCJwcm9maWxlSW1hZ2UiOiJhc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHRBZG1pbi5wbmciLCJ0b3RwU2VjcmV0IjoiIiwiaXNBY3RpdmUiOnRydWUsImNyZWF0ZWRBdCI6IjIwMjItMTEtMDIgMjE6MTU6MjkuNzU2ICswMDowMCIsInVwZGF0ZWRBdCI6IjIwMjItMTEtMDIgMjM6Mzg6NTcuMjEzICswMDowMCIsImRlbGV0ZWRBdCI6bnVsbH0sImlhdCI6MTY2NzQzNjg4OCwiZXhwIjoxNjY3NDU0ODg4fQ.n4MtQXl6NV2kWzfmeDbBOIscom7izqYmYDFgvDepR0s7eY0GSGj1eQfvyZG9KqD1qEFlaOIbnUl1vH8-qkYOEep2W5jGezV_2YClUAuwMmApUKz9R837zniSNyrWDii95g4hVeQbD6G0gfUjA2NBqvMBWSHQ-ABY2oKt4eHWo94',
}

HEADER = {'Access-Control-Allow-Origin': '*', 'X-Content-Type-Options': 'nosniff', 'X-Frame-Options': 'SAMEORIGIN', 'Feature-Policy': "payment 'self'", 'X-Recruiting': '/#/jobs', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '830', 'ETag': 'W/"33e-U/iGgvq/5akBbVWHC2tliKBMIHA"', 'Vary': 'Accept-Encoding', 'Connection': 'keep-alive'}

HOST = "juice-shop.herokuapp.com/"
URL = "https://juice-shop.herokuapp.com/"

TEST_HEADER= {
    'Host': HOST,
    'Sec-Ch-Ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'Accept': 'application/json, text/plain, */*',
    'Sec-Ch-Ua-Mobile': '?0',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MjIsInVzZXJuYW1lIjoiIiwiZW1haWwiOiJ0ZXN0ZWVlQGdtYWlsLmNvbSIsInBhc3N3b3JkIjoiZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2UiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoiMC4wLjAuMCIsInByb2ZpbGVJbWFnZSI6Ii9hc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHQuc3ZnIiwidG90cFNlY3JldCI6IiIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDIyLTExLTAzIDA2OjA4OjA0LjM5OSArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDIyLTExLTAzIDA2OjA4OjA0LjM5OSArMDA6MDAiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE2Njc0NTYzNTcsImV4cCI6MTY2NzQ3NDM1N30.ex1aL9OCnrGl_NhA_IzkSpwoaOgLcm0aj285E4QzdRuQ5Fmvv6oeivVqTLKBBB9oPove8F0TKlW2oyTZLNrnPw-WgYpTXxLgZQP3UN380GSbMtfRuvdVE3BtFU0-nzf4RtGUhyAgsvwKTjo0mky20urTjyWamX9OvEWjlVG9Rcw',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.63 Safari/537.36',
    #'Sec-Ch-Ua-Platform': '"macOS"',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': URL,
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'language=en; welcomebanner_status=dismiss; cookieconsent_status=dismiss; continueCode=pphytRIns8UqHYurh8tMTmFkf4SBt5i9fnSLHWPu9MtrMTpni1ZfkYSVZHJDuE9hbnt1jcxqC9qSMBU4DTJZCqJspaiQMS7XtVVINMTDnCegs8li9Nf18cwOHJx; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MjIsInVzZXJuYW1lIjoiIiwiZW1haWwiOiJ0ZXN0ZWVlQGdtYWlsLmNvbSIsInBhc3N3b3JkIjoiZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2UiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoiMC4wLjAuMCIsInByb2ZpbGVJbWFnZSI6Ii9hc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHQuc3ZnIiwidG90cFNlY3JldCI6IiIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDIyLTExLTAzIDA2OjA4OjA0LjM5OSArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDIyLTExLTAzIDA2OjA4OjA0LjM5OSArMDA6MDAiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE2Njc0NTYzNTcsImV4cCI6MTY2NzQ3NDM1N30.ex1aL9OCnrGl_NhA_IzkSpwoaOgLcm0aj285E4QzdRuQ5Fmvv6oeivVqTLKBBB9oPove8F0TKlW2oyTZLNrnPw-WgYpTXxLgZQP3UN380GSbMtfRuvdVE3BtFU0-nzf4RtGUhyAgsvwKTjo0mky20urTjyWamX9OvEWjlVG9Rcw',
}
