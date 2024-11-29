# 我们自定义一个网络操作包，相关的网络操作函数都在这里定义
# client.py 和 server.py 都可以引用这个包，这样就可以避免重复定义网络操作函数
# 当然你也可以把这些函数在 client.py 和 server.py 里写两遍

import socket

# 请实现 send_str 和 recv_str 函数，分别用于发送和接收字符串
def send_str(client_socket = None, data = None):
    # 发送字符串
    # TODO
    pass

def recv_str(client_socket = None):
    # 接收字符串
    # TODO
    pass


# 我们不妨把客户端和服务器的连接操作也放到这个包里
# 当然你写在 client.py 和 server.py 里也是完全可以的
# 这些函数的参数请根据实际情况添加
def connect_server():
    # 建立连接
    # TODO
    pass

def close_server():
    # 关闭连接
    # TODO
    pass

def connect_client():
    # 建立连接
    # TODO
    pass

def close_client():
    # 关闭连接
    # TODO
    pass