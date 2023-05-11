import os, re, sys,pathlib
import pyperclip

if(sys.argv[1]==None): raise Exception("Path did not given")
path = pathlib.Path(__file__).parent.resolve().joinpath(sys.argv[1])
if(not os.path.exists(pathlib.Path(__file__).parent.resolve().joinpath(sys.argv[1]))): raise Exception("Entered folder does not exists")
dir_list = os.listdir(path)
dict = []
new_index = 100
string= ""
for index, x in enumerate(dir_list):
    match = re.match(r'^([0-9]+)*(.+)$',x)
    if x in sys.argv[0]:continue
    if(match[1]==None):
        dict.append((new_index,x)) 
        new_index+=1
    else:
        dict.append((int(match[1]),x)) 
dict.sort(key=lambda tup: tup[0]) 
for index, x in enumerate(dict):
    string +=f"- [x] {x[1]}\n"
pyperclip.copy(string)
print("copied")