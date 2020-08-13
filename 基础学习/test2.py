import requests
import json
def get_fanyi_data(word=None):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    from_data = {'i': 'word',
                 'from': 'AUTO',
                  'to': 'AUTO',
                   'smartresult': 'dict',
                   'client': 'fanyideskweb',
                   'salt': '15935023986742',
                   'sign': '4ba82c1a62da4ae4b711134e5b1e008e',
                   'ts': '1593502398674',
                   'bv': '656f750600466990f874a839d9f5ad23',
                   'doctype': 'json',
                   'version': '2.1',
                   'keyfrom': 'fanyi.web',
                   'action': 'FY_BY_CLICKBUTTION',
                    'typoResult' : 'false'
                 }
    response = requests.post(url,data=from_data)
    connent = json.loads(response.text)
    print(connent)
if __name__ == '__main__':
    get_fanyi_data('我爱中国')