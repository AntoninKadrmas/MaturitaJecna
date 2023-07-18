import os, re, sys,pathlib
import pyperclip

if(sys.argv[1]==None): raise Exception("Path did not given")
path = pathlib.Path(__file__).parent.resolve().joinpath(sys.argv[1])
if(not os.path.exists(pathlib.Path(__file__).parent.resolve().joinpath(sys.argv[1]))): raise Exception("Entered folder does not exists")
dir_list = os.listdir(path)
dict = []
string= "### "+sys.argv[1]+'\n'
for index, x in enumerate(dir_list):
    match = re.match(r'^(.*)$',x)
    if x in sys.argv[0]:continue
    if(match[1]!=None):
        dict.append(match[1]) 
for x in dict:
    string +=f"- {x}\n"
pyperclip.copy(string)
print("copied")
