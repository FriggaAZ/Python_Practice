import socket
import time

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind(("", 7890))
tcp_server_socket.listen(128)
tcp_server_socket.setblocking(False)

client_socket_list = list()


while True:

    time.sleep(1)

    try:
        new_socket, new_addr = tcp_server_socket.accept()
    except Exception as ret:
        print("---没有新的客户端到来---")
    else:
        print("---只要没有产生异常，那么也就意味着来了一个新的客户端---")
        new_socket.setblocking(False)
        client_socket_list.append(new_socket)
    
    for client_socket in client_socket_list:
        try:
            recv_data = client_socket.recv(1024)
        except Exception as ret:
            print("---这个客户端没有发送来数据---")
        else:
            if recv_data:
                print("---客户端发送过来了数据---")
            else:
                # 对方调用了close
                client_socket_list.remove(client_socket)
                client_socket.close()
                print("---客户端已经关闭---")
