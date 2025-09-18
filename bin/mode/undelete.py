import os
import json
import shutil

def run(roots,argv_list):
  Trash_Data = os.path.join(roots,"../TrashData/TrashList.json")
  with open(Trash_Data,encoding="utf-8") as json_data:
    json_data = json.load(json_data)
  length = len(json_data)
  for xh in argv_list[1:]:
    if 0 >= int(xh) or int(xh) > length:
      print(f"del: undelete: 序号[{xh}]不存在")
      continue
    path1,path2 = json_data[xh][-2::1]
    if os.path.exists(path1):
      if os.path.exists(os.path.dirname(path2)) == False:
        os.makedirs(os.path.dirname(path2),exist_ok=True)
      shutil.move(path1,path2)
      print(f"已恢复 -> {json_data[xh][0]}")
    else:
      print(f"{json_data[xh][0]}: 恢复失败")
    del json_data[xh]
  # 重新排列
  temp_dict = {}
  new_key = 1
  for old_key in json_data:
    value = json_data[old_key]
    temp_dict[new_key] = value
    new_key += 1

  # 重新写入
  with open(Trash_Data,"w",encoding="utf-8") as fdata:
    json.dump(temp_dict,fdata,ensure_ascii=False,indent=2)
