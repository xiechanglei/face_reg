install

```bash
mkdir /home/xie/sdk/python-env
python3 -m venv /home/xie/sdk/python-env
source /home/xie/sdk/python-env/bin/activate
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip install dlib
pip install face_recognition
pip install setuptools
``` 

run

```bash
python3 xxxx.py
```