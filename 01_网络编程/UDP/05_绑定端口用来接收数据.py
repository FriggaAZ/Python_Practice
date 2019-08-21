import socket

def main():
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.绑定一个本地信息（元组），必须绑定自己电脑的ip以及port，其他的不行
    localaddr = ("", 7788)  # 自己的ip可以使用空字符串代替
    udp_socket.bind(localaddr)
    
    # 3.接收数据
    recv_data = udp_socket.recvfrom(1024)
    # recv_data 这个变量中存储的三一个元组（接收到的数据，（发送方的IP，port））
    recv_message = recv_data[0]  # 数据
    send_addr = recv_data[1][0]  # 地址
    send_port = recv_data[1][1]  # 端口
    # 4.打印接收数据
    # print("%s:%s:%s" % (send_addr, send_port, recv_message.decode("utf-8")))  # Windows默认编码GBK，所以使用utf-8解码会错误
    print("%s:%s:%s" % (send_addr, send_port, recv_message.decode("utf-8")))  # 使用GBK解码没有问题
    # 5.关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
