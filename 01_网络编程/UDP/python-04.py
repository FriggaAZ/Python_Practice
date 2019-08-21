import socket

def send_msg(udp_socket):
    dest_ip = input("请输入对方的IP地址")
    dest_port = int(input("请输入端口号"))
    send_data = input("请输入要发送的信息")
    udp_socket.sendto(send_data.encode("utf-8"),(dest_ip, dest_port))


def recv_msg(udp_socket):
    recv_data = udp_socket.recvfrom(1024)
    print("%s: %s" % (str(recv_data[1]), recv_data[0].decode("utf-8")))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 7788))
    while True:

        print("XXX聊天")
        print("1.发送消息")
        print("2.接收消息")
        print("0.退出")
        op=input("请输入功能")
        # send
        if op == "0":
            break
        elif op == "1":
            send_msg(udp_socket)
        # recv and display
        elif op == "2":
            recv_msg(udp_socket)
        else:
            continue

if __name__ == "__main__":
    main()
