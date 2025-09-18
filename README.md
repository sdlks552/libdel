### del
---
一个带有回收站的文件删除命令，Linux中的rm命令误删后就很难找回，除非有数据恢复技术或一些其他工具强行找回。

del解决了文件删除后难找回的问题，它有自己的回收站，删除的文件会在回收站存储14天，14天后自动清除。

### termux配置
---
1. 先克隆仓库到home
3. cd 进入克隆的仓库目录
4. 输入以下命令一键配置
```bash
./install
```


### 其他
---
除termux外，其他的Linux都没有兼容一键配置，不过感兴趣的话可以自己配置一下

这个命令需要python10.0+版本的解释器，所以需要先安装python10.0+。

1. 克隆仓库
2. 在Linux的lib目录中直接把克隆的 libdel目录移过去
3. 进入libdel目录
4. 将README.sh与install文件都删了
5. 在libdel中进入一个叫bin的目录
6. 往Linux的bin目录下创建一个软链接
```bash
ln -s "./del" "Linux的bin目录/del"
```

最后输入 `del` 或 `del -help` 查看帮助
