import socket
import re
import multiprocessing
import time
import mini_frame


class WSGIServer(object):
    def __init__(self):
        self.tcp_service_socket = socket.socket(socket.AF_INET,
                                                socket.SOCK_STREAM)
        self.tcp_service_socket.setsockopt(socket.SOL_SOCKET,
                                           socket.SO_REUSEADDR, 1)

        self.tcp_service_socket.bind(("", 9090))

        self.tcp_service_socket.listen(128)

    def service_client(self, new_client):
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
        # 2.1 如果检测到不是以.py结尾，就是请求的静态资源（html/css/js/png, jpg等）
        if not file_name.endswith(".py"):
            try:
                f = open("../html" + file_name, "rb")

            except Exception as e:
                print(e)
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
        else:
            # 以.py结尾，那么就认为是动态资源的请求


            env = dict()
            body = mini_frame.application(env, self.set_response_header)

            header = "http/1.1 %s\r\n" % self.status

            for temp in self.headers:
                header += "%s:%s\r\n" % (temp[0], temp[1])

            header += "\r\n"

            response = header + body
            new_client.send(response.encode("utf-8"))

        new_client.close()

    def set_response_header(self, status, headers):
        self.status = status
        self.headers = [('Server', 'Mini-Web V8.1.3')]
        self.headers += headers

    def run_forever(self):

        while True:
            # accept
            new_client, client_addr = self.tcp_service_socket.accept()

            # service
            p = multiprocessing.Process(target=self.service_client,
                                        args=(new_client, ))
            p.start()

            new_client.close()

        self.tcp_service_socket.close()


def main():
    """控制整体，创建一个web服务器对象，然后调用服务器对象的run_forever方法运行"""
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()


if __name__ == "__main__":
    main()
