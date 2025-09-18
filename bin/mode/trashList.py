from ntpath import isfile
import sys
import json
import os
from datetime import date
import mode

def colorize():
  if sys.stdout.isatty() and os.getenv("TERM") not in (None,"dumb"):
    color1 = "\033[0m"
    color2 = "\033[33m"
    color3 = "\033[36m"
  else:
    color1 = ""
    color2 = ""
    color3 = ""
  return (color1,color2,color3)

def size(filesize):
  if filesize == "directory":
    return filesize
  else:
    bit = "B"
    if filesize > 1024 :
      filesize = filesize / 1024
      bit = "KB"
    if filesize > 1024**2:
      filesize = filesize / 1024
      bit = "MB"
    if filesize > 1024**3:
      filesize = filesize / 1024
      bit = "GB"
    if filesize > 1024**4:
      filesize = filesize / 1024
      bit = "TB"
    return f"{round(filesize,2)}{bit}"

def run(roots):
  trashList_path = os.path.join(roots,f"../TrashData/TrashList.json")
  color1,color2,color3 = colorize()
  if os.path.exists(trashList_path) == False:
      print("Trash: 回收站里没有任何东西！")
      return

  with open(trashList_path,encoding="utf-8") as f:
      tlist = json.load(f)

  if len(tlist) == 0:
      print("Trash: 回收站里没有任何东西！")
      exit(0)
  today = date.today()
  new_tlist = {}
  lenth = 1
  sum_size = 0
  for trash in tlist:
      filename,filetime,path1,path2 = tlist[trash]
      y,m,s = filetime.split("-")
      dtime = date(int(y),int(m),int(s))
      newday = 14 - (today - dtime).days
      if newday <= 0:
        mode.remove.rm_rf(path1)
        continue
      days = f"{newday}天后被彻底删除"
      if os.path.isfile(path1):
        file_size = os.path.getsize(path1)
        sum_size += file_size
      else:
        file_size = "directory"
      file_size = size(file_size)
      print(f" {color3}[{lenth}]  {color1}{filename}: {file_size} 删除于-> {filetime}  {color2}{days}")
      file_trash = [filename,filetime,path1,path2]
      new_tlist[lenth] = file_trash
      lenth += 1
  sum_size = size(sum_size)
  print(f"{color3}总计：{sum_size}{color1}")

  with open(trashList_path,"w",encoding="utf-8") as text:
    json.dump(new_tlist,text,ensure_ascii=False,indent=2)
