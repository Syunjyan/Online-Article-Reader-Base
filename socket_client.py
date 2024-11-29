import socket

# 创建Socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
port = 7890 # 自定义端口号应在 1024-65535 之间，且与服务器一致
client_socket.connect(('localhost', port))

# 发送数据
# TODO
client_socket.send("你好，服务器".encode())

# 接收数据
data = client_socket.recv(1024)
print(f"收到数据: {data.decode()}")

# 关闭连接
client_socket.close()