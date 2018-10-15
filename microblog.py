'''
开启调试模式需设置环境变量 FLASK_DEBUG，如下
linux export FLASK_DEBUG=1 && python -m flask run 
windows set FLASK_DEBUG=1 & python -m flask run
在Pycharm 2018中，开启DEBUG模式需要在pycharm右上角运行按钮左边的项目名称下，选择Edit Configurations，打开编辑界面后，把FLASK_DEBU勾选上。
'''

from app import app