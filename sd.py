import sys
import os
import base64
import importlib.util
from IPython.display import clear_output
from google.colab import drive

# 授权并挂载Google云盘
drive.mount('/content/drive')

# 解码变量
w = base64.b64decode("d2VidWk=").decode('ascii') # webui
sdw = base64.b64decode("c3RhYmxlLWRpZmZ1c2lvbi13ZWJ1aQ==").decode('ascii') # sdw
gwebui_dir = f'/content/drive/MyDrive/{sdw}'

# 切换到/content目录
%cd /content

# 部署 ubuntu3 环境
%env TF_CPP_MIN_LOG_LEVEL=1

!apt-get -y install -qq aria2
!apt -y update -qq
!wget http://launchpadlibrarian.net/367274644/libgoogle-perftools-dev_2.5-2.2ubuntu3_amd64.deb
!wget https://launchpad.net/ubuntu/+source/google-perftools/2.5-2.2ubuntu3/+build/14795286/+files/google-perftools_2.5-2.2ubuntu3_all.deb
!wget https://launchpad.net/ubuntu/+source/google-perftools/2.5-2.2ubuntu3/+build/14795286/+files/libtcmalloc-minimal4_2.5-2.2ubuntu3_amd64.deb
!wget https://launchpad.net/ubuntu/+source/google-perftools/2.5-2.2ubuntu3/+build/14795286/+files/libgoogle-perftools4_2.5-2.2ubuntu3_amd64.deb
!apt install -qq libunwind8-dev
!dpkg -i *.deb
%env LD_PRELOAD=libtcmalloc.so
!rm *.deb

# 部署 GPU 环境
!apt -y install -qq aria2 libcairo2-dev pkg-config python3-dev
!pip install -q torch==2.0.0+cu118 torchvision==0.15.1+cu118 torchaudio==2.0.1+cu118 torchtext==0.15.1 torchdata==0.6.0 --extra-index-url https://download.pytorch.org/whl/cu118 -U
!pip install -q xformers==0.0.18 triton==2.0.0 -U

clear_output()

# 切换到指定目录并执行Python脚本
%cd {gwebui_dir}-V2.2
!python launch.py --listen --enable-insecure-extension-access --theme dark --gradio-queue --multiple --opt-sdp-attention
