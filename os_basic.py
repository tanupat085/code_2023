import os
import random
import shutil
import time
path = r'D:\new_code\trojan_test'
folder_list = os.listdir(path)

result_file = []
result_folder = []

file_dict = {}


print(folder_list)
for i in folder_list:
    check = i.split('.')
    if len(check) > 1:
        print('file: ',i)
        result_file.append(i)
    else :
        print('folder :', i)
        result_folder.append(i)
print('folder :',result_folder)
print('file: ',result_file)

for f in result_file:
    select = random.choice(result_folder)
    folderpath = os.path.join(path,select)
    filepath = os.path.join(folderpath,f)
    current = os.path.join(path,f)

    print(f,'------>',filepath)
    file_dict[f] = {'current' : current,'next':filepath}
print('file_dict',file_dict)

while True :
    for f1,f2 in file_dict.items():
        current = f2['current']
        nextpath = f2['next']
        shutil.move(current,nextpath)
        
        select = random.choice(result_folder)
        folderpath = os.path.join(path,select)
        file_next = os.path.join(folderpath,f1)
        file_dict[f1]['current'] = nextpath
        file_dict[f1]['next'] = file_next
    time.sleep(2)





