import socket
import re
import select


def service_client(new_client, request):
    # 1. 接受浏览器发送的http请求
    # request = new_client.recv(1024).decode("utf-8")
    # print(">>" * 20)
    # print(request)
    request_lines = request.splitlines()
    print("")
    print(">>" * 20)
    print(request_lines)

    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        # print("*" * 30, file_name)
        if file_name == "/":
            file_name = "/index.html"

    # 2. 返回http格式的数据给浏览器

    try:
        f = open("./html" + file_name, "rb")

    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "-----file not found"
        new_client.send(response.encode("utf-8"))

    else:
        html_content = f.read()
        f.close()
        response_body = html_content
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"
        response = response_header.encode("utf-8") + response_body

        new_client.send(response)

    # new_client.close()


def main():
    tcp_service_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind
    tcp_service_socket.bind(("", 9090))

    # listen
    tcp_service_socket.listen(128)
    # 变成非堵塞
    tcp_service_socket.setblocking(False)

    # 创建一个epoll对象（对应一个共享内存
    epl = select.epoll()

    # 将监听套接字对应的fd注册到epoll中
    epl.register(tcp_service_socket.fileno(), select.EPOLLIN)

    fd_event_dict = dict()

    while True:
        # 默认会堵塞， 直到OS检测到数据到来，
        # 通过事件通知方式告诉程序，此时程序才会解堵塞
        fd_event_list = epl.poll()

        # [(fd, event), (套接字对应的文件描述符，
        # 这个fd到底是什么事件 例如 可以调用recv接收等)]
        for fd, event in fd_event_list:
            # 等待新的客户端链接
            if fd == tcp_service_socket.fileno():
                new_client, client_addr = tcp_service_socket.accept()
                epl.register(new_client.fileno(), select.EPOLLIN)
                fd_event_dict[new_client.fileno()] = new_client
            elif event == select.EPOLLIN:
                # 判断已经链接的客户端是否有数据发送过来
                recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
                if recv_data:
                    # 开始服务
                    service_client(fd_event_dict[fd], recv_data)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]

    tcp_service_socket.close()


if __name__ == "__main__":
    main()
