import os
import sys
import subprocess
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
file_handler = logging.FileHandler('./log/docker.log')
file_handler.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - docker - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# subprocess.Popen() 运行命令
run = lambda x: subprocess.Popen([x],stdout=subprocess.PIPE,shell=True).communicate()

class AutowareDocker:
  def __init__(self) -> None:
     # 原始镜像名
     self.ori_image_ = "ghcr.io/autowarefoundation/autoware-universe:latest-cuda"
     # 运行 rocker 后镜像
     self.image_ = "ann-image:v1"
     # 运行 rocker 后容器名
     self.container_ = "autoware_universe"
     self.check_image()
     self.container_id_ = self.get_running_container_id()
     if(self.container_id_ != ""):
      os.system("docker exec -it %s /bin/bash"%self.container_id_)
     else:
      self.container_id_ = self.get_container_id()
      if(self.container_id_ != ""):
        print("111")
        os.system("docker start %s"%(self.container_id_))
        os.system("docker exec -it %s /bin/bash"%self.container_id_)
      else:
        os.system("rocker --nvidia --x11  --nocleanup --user \
        --name %s \
        --image-name %s \
        --volume $HOME/autoware.docker/autoware \
        --volume $HOME/autoware.docker/autoware_map \
        -- %s"%(self.container_,self.image_,self.ori_image_))
        

  def check_image(self):
    images = str( run('docker inspect %s'%self.image_) )
    if 'sha256' not in images :
        logger.warn('images not found, try pull image')
        os.system("docker pull %s"%self.ori_image_)
  
  def get_container_id(self):
    result = run("docker ps -a")
    if self.image_ not in result[0].decode():
      return ""
    else:
      return (result[0].decode().split(self.image_)[0].split()[-1])

  def get_running_container_id(self):
    result = run("docker ps")
    if self.image_ not in result[0].decode():
      return ""
    else:
      return (result[0].decode().split(self.image_)[0].split()[-1])

  

if __name__ == "__main__":
  autoware_docker = AutowareDocker()
