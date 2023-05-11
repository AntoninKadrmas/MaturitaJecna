
import os
import re
import sys 
import pyperclip

dir_list = os.listdir("./")
actual_file = sys.argv[0]
dict = []
new_index = 100
for index, x in enumerate(dir_list):
    match = re.match(r'^([0-9]+)*(.+)$',x)
    if x in actual_file:continue
    if(match[1]==None):
        dict.append((new_index,x)) 
        new_index+=1
    else:
        dict.append((int(match[1]),x)) 

dict.sort(key=lambda tup: tup[0]) 
string= ""
for index, x in enumerate(dict):
    string +=f"- [x] {x[1]}\n"
pyperclip.copy(string)
print("copied")