import sys
import os
import pathlib
import mode

def check_argv(argv_lists):
  for value in argv_lists:
    try:
      int(value)
    except ValueError:
      return False
  return True

num = 0
roots = pathlib.Path(__file__).resolve().parent
roots = os.path.dirname(os.path.realpath(__file__))
argv_list = sys.argv
if len(argv_list) == 1:
  with open(f"{roots}/../TrashData/help","r") as helptxt:
    helptxt = helptxt.read()
  print(helptxt)
  sys.exit(0)

options = "-none"
if argv_list[1].startswith("-"):
  options = argv_list.pop(1)
else:
  pwdpath = os.getcwd()
  mode.remove.run(roots,pwdpath,argv_list,True)

match options:
  case "-help":
    with open(f"{roots}/../TrashData/help","r") as helptxt:
      helptxt = helptxt.read()
    print(helptxt)
  case "-none":
    pass # 这里给默认值留个分支
  case "-l":
    mode.trashList.run(roots)
  case "-f":
    pwdpath = os.getcwd()
    mode.remove.run(roots,pwdpath,argv_list,False)
  case "-u":
    length = len(argv_list[1:])
    if length == 0:
      print("del: error: 没有输入序号")
      sys.exit(3)
    argv_list = list(dict.fromkeys(argv_list))
    check = check_argv(argv_list[1:])
    if check:
      mode.undelete.run(roots,argv_list)
    else:
      print("del: error: 指定序号错误")
      num = 2
  case "-c":
    argvn = None
    if len(argv_list[1:]) > 0:
      argvn = list(dict.fromkeys(argv_list))
    else:
      pass
    check = check_argv(argv_list[1:])
    if check:
      mode.clear.run(roots,argvn)
    else:
      print("del: clear: 指定序号错误！")
      num = 2
  case _:
    print("del: error: 没有这个参数，输入 del -help 查看帮助")
    num = 1

sys.exit(num)
