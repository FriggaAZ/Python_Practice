import socket

def main():
    # 1.创建套接字
    tcp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.获取服务器IP/Port
    dest_ip = input("请输入IP：")
    dest_port = int(input("请输入Port："))

    # 3.链接服务器
    tcp_socket_client.connect((dest_ip, dest_port))

    # 4.获取下载文件的名字
    download_file_name = input("请输入要下载的文件名")
    # 5.将文件名字发送到服务器
    tcp_socket_client.send(download_file_name.encode("utf-8"))
    # 6.接收文件中的数据
    recv_data = tcp_socket_client.recv(1024)  # 1024*1024 ---> 1k * 1024 = 1M 1024^3 ---> 1G

    if recv_data:
        # 7.保存接收到的数据到一个文件中
        with open("附件" + download_file_name, "wb") as f:
            f.write(recv_data)
    # 8.关闭套接字
    tcp_socket_client.close()

if __name__ == "__main__":
    main()
