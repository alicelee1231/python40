import itertools
import zipfile

pwd_string="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

zFile = zipfile.ZipFile(r'6.압축파일암호푸는프로그램/pwd1234.zip')

for len in range(1,4):
    to_attempt = itertools.product(pwd_string,repeat=len)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        print(passwd)
        try:
            zFile.extractall(pwd=passwd.encode())
            print(f"password is {passwd}")
            break
        except:
            pass