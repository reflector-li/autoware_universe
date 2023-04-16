# Autoware.universe 
使用docker版本进行安装，直接运行 autoware_docker.py 即可拉取镜像并进入容器

## 注意事项：
1. 在创建好容器后退出，重新使用 autoware_docker.py 进入时会报错：
```shell
linkx@user-MS-7D25:~/autoware.docker$ python3 autoware_docker.py 
Error response from daemon: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: error during container init: error mounting "/tmp/.dockerl_1e8w1g.xauth" to rootfs at "/tmp/.dockerl_1e8w1g.xauth": mount /tmp/.dockerl_1e8w1g.xauth:/tmp/.dockerl_1e8w1g.xauth (via /proc/self/fd/7), flags: 0x5000: not a directory: unknown: Are you trying to mount a directory onto a file (or vice-versa)? Check if the specified host path exists and is the expected type
Error: failed to start containers: 48179123b6a0
```
原因在于使用 rocker 第一次创建容器时将host的文件夹 `/tmp/.dockerl_1e8w1g.xauth` 挂载到了容器内部的文件上，也就是说 `/tmp/.dockerl_1e8w1g.xauth` 在容器中是文件，从而报错。

**修改方式**：
在 host 主机下查找docker中该路径，将其删除并创建为文件夹
```shell
root@user-MS-7D25:/var/lib/docker/overlay2/b9db4ec5f0f6cd96fff9549ac8b719a4e7ec49151ad4ce1fb56c9d3868c94921/diff/tmp# ls -a
.  ..  .docker0bn8d121.xauth  runtime-linkx  .X11-unix
```
在本机中进入docker文件夹需要 root权限，即 `sudo su` 方式进入。