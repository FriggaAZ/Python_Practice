import socket

def main():
        # 创建一个UDP套接字
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # 绑定本地信息
        udp_socket.bind(("", 7890))

        while(True):
                # 从键盘获取数据
                send_data=input("请输入要发送的内容：")
                if send_data=="exit":
                        break
                # 使用套接字收发数据
                # udp_socket.sendto(b"hahahahahaha",("192.168.245.128", 8080) )
                udp_socket.sendto(send_data.encode("utf-8"),("192.168.245.128", 8080) )
                
        # 关闭套接字
        udp_socket.close()


if __name__ == "__main__":
        main()