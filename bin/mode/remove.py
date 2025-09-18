import json
import time
from datetime import date
import os
import shutil

def rm_rf(paths):
  try:
    if os.path.isfile(paths):
      os.remove(paths)
    else:
      shutil.rmtree(paths)
  except Exception as e:
    print(f"error: {paths}删除失败: {e}")

def run(roots,pwdpath,argv_list,Trash):
  if Trash == False:
    for t in argv_list[1:]:
      print(t)
    print("确认强制永久删除以上内容：")
    time.sleep(3)
    check = input("Y/y 确定 N/n 取消操作：")
    if check == "Y" or check == "y":
      pass
    else:
      print("操作取消！")
      return 0
  if os.path.exists(f"{roots}/../TrashData/TrashList.json"):
    with open(f"{roots}/../TrashData/TrashList.json",encoding="utf-8") as text:
      TrashList=json.load(text)
      length = len(TrashList)
  else:
      TrashList = {}
      length = 0
  dictnum = length + 1
  Trashpath = f"{roots}/../Trash/"
  for files in argv_list[1:]:
    now,timems = str(time.time()).split(".")
    now = now + timems
    today = str(date.today())
    filename = os.path.basename(str(files))
    if files.startswith("/"):
      filepath = files
    else:
      filepath = os.path.join(pwdpath,files)
      filepath = os.path.normpath(filepath)
    if os.path.exists(filepath) == False:
      print(f"{filename}: 该文件或目录不存在！")
      continue
    if Trash:
      shutil.move(filepath,f"{Trashpath}{filename}{now}")
      filelist = [filename,today,f"{Trashpath}{filename}{now}",filepath]
      TrashList[dictnum] = filelist
      print(f"删除 --> {filename}")
    else:
      rm_rf(filepath)
    dictnum += 1

  with open(f"{roots}/../TrashData/TrashList.json","w",encoding="utf-8") as text:
      json.dump(TrashList,text,ensure_ascii=False,indent=2)

