import os
import shutil
import time
import json

def run(roots,argv_list):
  Trash_path = os.path.join(roots,"../Trash/")
  Trash_Data = os.path.join(roots,"../TrashData/TrashList.json")
  if argv_list == None:
    print("是否要清空回收站！")
    time.sleep(3)
    check = input("Y/y 确定 N/n 取消操作")
    if check == "Y" or check == "y":
      if os.path.exists(Trash_Data):
        os.remove(Trash_Data)
      if os.path.exists(Trash_path):
        shutil.rmtree(Trash_path)
        os.mkdir(Trash_path)
    else:
      print("操作取消！")
  else:
    if os.path.exists(Trash_Data):
      with open(Trash_Data,encoding="utf-8") as jsondata:
        datadict = json.load(jsondata)
    else:
      print("error: 回收站为空！")
      return
    length = len(datadict)
    for key in argv_list[1:]:
      if int(key) < length:
        print(datadict[key][0])
    print("是否删除以上内容！")
    time.sleep(3)
    check = input("Y/y 确定 N/n 取消操作")
    if check == "Y" or check == "y":
      for key in argv_list[1:]:
        if int(key) > length:
          print(f"error: 没有[{key}]这个序号")
          break
        filepath = datadict[key][-2]
        if os.path.exists(filepath):
          os.remove(filepath)
        del datadict[key]
    else:
      print("操作取消")
    # 重新排列顺序
    newdata = {}
    key_num = 1
    for new_key in datadict:
      files = datadict[new_key]
      newdata[key_num] = files
      key_num += 1

    with open(Trash_Data,"w",encoding="utf-8") as new:
      json.dump(newdata,new,ensure_ascii=False,indent=2)
