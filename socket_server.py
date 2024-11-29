import socket

# 创建Socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定地址和端口
port = 7890 # 端口号可自定义，但要与客户端一致
server_socket.bind(('localhost', port))

# 监听连接
server_socket.listen(5)
print("服务器正在监听...")

# 接受客户端连接
client_socket, client_address = server_socket.accept()
print(f"连接来自: {client_address}")

# 接收数据
data = client_socket.recv(1024)
print(f"收到数据: {data.decode()}")

# 发送数据
client_socket.send("欢迎连接服务器".encode())

# 关闭连接
client_socket.close()
server_socket.close()