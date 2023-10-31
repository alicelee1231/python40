import itertools
import zipfile

def un_zip(pwd_string, min_len, max_len, zFile):
    for len in range(min_len,max_len+1):
        to_attempt = itertools.product(pwd_string, repeat=len)
        for attempt in to_attempt:
            passwd=''.join(attempt)
            print(passwd)
            try:
                zFile.extractall(pwd=passwd.encode())
                print(f"password is that {passwd}")
                return 1
            except:
                pass
pwd_string="0123456789"
zFile = zipfile.ZipFile(r'6.압축파일암호푸는프로그램/pwd1234.zip')

min_len = 1
max_len = 4

unzip_result = un_zip(pwd_string, min_len, max_len, zFile)

if unzip_result ==1 :
    print("you find the pwd succesfully")
else :
    print("you haven't find the pwd yet, try again")

