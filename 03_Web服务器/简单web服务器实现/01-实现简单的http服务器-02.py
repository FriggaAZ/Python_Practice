import socket


def service_client(new_client_socket):
    # 接收浏览器发过来的http请求
    # GET / HTTP/1.1
    request = new_client_socket.recv(1024)
    print(request)

    # 2.返回http格式的数据给浏览器
    # 浏览器需要将\r\n理解为换行符
    # 2.1 Headers
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"

    # 2.2 Body
    response += "<h1>HI～这是浏览器返回的内容</h1>"
    new_client_socket.send(response.encode("GBK"))


def main():

    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind
    tcp_server_socket.bind(("", 7890))

    # listen
    tcp_server_socket.listen(128)

    while True:
        # accept等待链接
        new_client_socket, client_addr = tcp_server_socket.accept()

        # 让套接字为客户端服务
        service_client(new_client_socket)

    tcp_server_socket.close()


if __name__ == "__main__":
    main()
