import socket

def main():
    # 1.买个手机（创建套接字 socket）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.插入手机卡（绑定本地信息 bind）
    tcp_server_socket.bind(("", 7890))
    # 3.将手机设置为响铃（让默认的套接字由主动变被动 listen）
    tcp_server_socket.listen(128)

    # 循环接收客户端请求
    while True:

        print("等待一个新的客户端到来")
        # 4.等待别人的电话（等待客户端链接 sccept）
        new_client_socket, client_addr = tcp_server_socket.accept()

        print("lei了lei了~")
        print(client_addr)
        while True:
            # 接收客户端发送的消息
            recv_data = new_client_socket.recv(1024)
            print(recv_data.decode("utf-8"))
            if recv_data:
                new_client_socket.send("hahahahahha".encode("utf-8"))
            else:
                break
        # 关闭套接字
        print("服务完毕")
        new_client_socket.close()
    tcp_server_socket.close()

if __name__ == "__main__":
    main()
