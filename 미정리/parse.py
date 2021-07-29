import requests
import json

def sendApi(path, method):

    API_HOST = 'https://httpbin.org/'
    url = API_HOST + path
    headers = {'ConTent-Type':'application/json', 'charset':'UTF-8', 'Accept':'*/*'}
    body = {
    }


    try:
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
        print("response status %r" % response.status_code)
        print("response text %r" % response.text)
    except Exception as ex:
        print(ex)
sendApi("post", "POST")


# parameters = {
#     id : 1
# }
# url1 = 'https://httpbin.org/'
# url2 = 'https://nghttp2.org/httpbin/'
# response = requests.get(url2+'get')
# print(response.status_code)
# print(response.content)
# response = requests.post(url2+'post')
# print(response)
# print(response.status_code)
# print(response.content)