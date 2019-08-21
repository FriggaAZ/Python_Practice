import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind
    tcp_socket.bind(("", 8080))

    # listen
    tcp_socket.listen(128)

    # 循环接受客户端消息
    while True:
        # accept
        new_client_socket, client_addr = tcp_socket.accept()

        # recv
        print(client_addr)
        # send
        recv_data = new_client_socket.recv(1024)
        print(recv_data.decode("utf-8"))

        new_client_socket.send(
            "HTTP/1.1 200 OK\r\n\r\n<h1>hahah</h1>".encode("utf-8"))
        # client_socket.close()
        new_client_socket.close()
    # server_socket.close()
    tcp_socket.close()


if __name__ == "__main__":
    main()
