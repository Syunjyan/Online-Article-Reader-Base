# 导入你需要的包，用到的包请注明在报告里
import socket

# 导入自定义的网络模块
from network import *


# 假设这是一个检索文章内容的函数
def search_articles(query):
    # 检索文章内容
    # TODO
    return '文章内容'



if __name__ == '__main__':

    # 建立连接
    # TODO




    while True:
        # 接收客户端的查询请求
        query = recv_str()
        # 解析查询请求，检索文章内容列表
        result = search_articles(query)
        # 将检索结果返回给客户端
        send_str(data=result)
        

    # 关闭连接
    # TODO