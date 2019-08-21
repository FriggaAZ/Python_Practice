import socket
import threading


def recv_data(udp_socket):
    # 接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


def send_data(dest_ip, dest_port, udp_socket):
    # 发送数据
    while True:
        send_data = input("请输入要发送的数据")
        udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def main():
    """完成UDP聊天器的整体控制"""

    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地信息
    udp_socket.bind(("", 7890))

    # 获取对方IP
    dest_ip = input("请输入对方IP：")
    dest_port = int(input("请输入对方Port："))

    t_recv_data = threading.Thread(target=recv_data, args=(udp_socket,))
    t_send_data = threading.Thread(target=send_data, args=(dest_ip, dest_port, udp_socket))

    t_recv_data.start()
    t_send_data.start()


if __name__ == "__main__":
    main()
