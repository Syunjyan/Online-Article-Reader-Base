# 导入你需要的包，用到的包请注明在报告里
import socket

# 导入自定义的网络模块
from network import *

# 建立连接
# TODO


while True:
    # 接收用户输入的查询请求
    # TODO
    query = ''
    # 向服务器发送查询请求
    send_str(data=query)
    # 接收服务器返回的检索结果
    result = recv_str()
    # 将结果展示给用户
    print(result)
    # 用户选择浏览的文章，或者重新查询，或者退出
    # 请根据你的设计实现
    # TODO



# 关闭连接
# TODO