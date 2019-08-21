import socket

def main():
        # 创建一个UDP套接字
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 从键盘获取数据
        send_data=input("请输入要发送的内容：")
        # 使用套接字收发数据
        udp_socket.sendto(send_data.encode("utf-8"),("127.0.0.1",7788) )
                
        # 关闭套接字
        udp_socket.close()


if __name__ == "__main__":
        main()
