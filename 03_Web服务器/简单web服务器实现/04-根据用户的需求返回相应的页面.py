import socket
import re


def service_client(new_client):
    # 1. 接受浏览器发送的http请求
    request = new_client.recv(1024).decode("utf-8")
    print(">>" * 20)
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
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        new_client.send(response.encode("utf-8"))
        new_client.send(html_content)


def main():
    tcp_service_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind
    tcp_service_socket.bind(("", 9090))

    # listen
    tcp_service_socket.listen(128)

    while True:
        # accept
        new_client, client_addr = tcp_service_socket.accept()

        # service
        service_client(new_client)

    tcp_service_socket.close()


if __name__ == "__main__":
    main()
