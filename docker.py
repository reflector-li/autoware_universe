import os
# 使用 rocker 创建镜像，使得 docker 内的 GUI 可以在 host上看到，但退出之后重新进入会创建新的容器。
# os.system("rocker --nvidia --x11  --nocleanup --user --volume $HOME/autoware.docker/autoware --volume $HOME/autoware.docker/autoware_map -- ghcr.io/autowarefoundation/autoware-universe:humble-latest-prebuilt-amd64")

# 使用 docker 创建容器，并且可以使用 gpu 等host设备信息。最后的是镜像ID，但这样的方式每次都会创建一个新的容器。
os.system("docker run -it  --gpus all -v /home/linkx/autoware.docker/autoware:/home/linkx/autoware.docker/autoware -v /home/linkx/autoware.docker/autoware_map:/home/linkx/autoware.docker/autoware_map  -e DISPLAY -e TERM   -e QT_X11_NO_MITSHM=1   -e XAUTHORITY=/tmp/.docker9dx1qg9g.xauth -v /tmp/.docker9dx1qg9g.xauth:/tmp/.docker9dx1qg9g.xauth   -v /tmp/.X11-unix:/tmp/.X11-unix   -v /etc/localtime:/etc/localtime:ro  f3aee06a17fb")


