import socket


def service_client(new_client_socket):
    request = new_client_socket.recv(1024)
    print(request)

    # 返回内容
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"
    # response += "HI~"

    f = open("./index.html", "rb")
    html_content = f.read()
    f.close()

    new_client_socket.send(response.encode("utf-8"))
    new_client_socket.send(html_content)
    # 关闭套接字
    new_client_socket.close()


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind
    tcp_socket.bind(("", 7890))

    # listen
    tcp_socket.listen(128)

    while True:
        # accept
        new_client_socket, client_addr = tcp_socket.accept()

        # 为客户端服务
        service_client(new_client_socket)

    tcp_socket.close()


if __name__ == "__main__":
    main()
