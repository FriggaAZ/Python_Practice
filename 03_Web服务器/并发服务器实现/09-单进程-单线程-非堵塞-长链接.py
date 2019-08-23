import socket
import re


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

    client_socket_list = list()
    while True:
        # accept
        try:
            new_client, client_addr = tcp_service_socket.accept()
        except Exception as ret:
            pass
        else:
            new_client.setblocking(False)
            client_socket_list.append(new_client)

        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024).decode("utf-8")
            except Exception as ret:
                pass
            else:
                if recv_data:
                    # 开始服务
                    service_client(client_socket, recv_data)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)

    tcp_service_socket.close()


if __name__ == "__main__":
    main()
