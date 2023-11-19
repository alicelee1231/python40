import os

proj_dir = "/Users/isaemmi/Desktop/pyProject/19.이미지에서글자추출"
filename = os.path.join(proj_dir,"txt파일로변환.txt")
filename2 = os.path.join(proj_dir,"after.txt")

lines = []
with open(filename,"r",encoding='utf-8') as bf:
        for line in bf:
                if not line.isspace():
                    lines.append(line.lstrip())


with open(filename2,"w")as df:
        for line in lines:
            df.write(line)
            print(line)

print("blank lines are deleted")