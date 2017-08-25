import socket
import threading


def parse_header(data):
    headers = data.decode('utf-8').split('\r\n')

    # ignoring requset line
    header = dict()
    for item in headers[1:]:
        print("Processing=============")
        splited = item.split(':')
        header[splited[0]] = splited[1:]

    # host = host_line.split(':')[1].strip()
    # print("host is {}".format(host))
    # return host

    host_addr = header['Host'][0].strip()
    port = 80 if len(header['Host']) == 1 else int(header['Host'][1])

    print("====================================")
    print(host_addr, port)
    return host_addr, port

    # PRINT DICTIONARY
    # for key in header.keys():
    #     print ("{:<20}\t\t{}".format(key, header[key]))



def handle_tcp(sock, addr):
    print("connection from {}".format(addr))
    # sock.send('Welcome!'.encode())

    # create a client socket that connects to the server 

    client_socket = socket.socket()

    request = b''

    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break

            print("=======Getting request==========")
            request += data
            print(request)
        except:
            break


        # sock.send('Hello, %s!{}\n'.format(data).encode())
        # print(data)


    print(request)
    host_addr, port = parse_header(request)
    print("|{}|".format(host_addr), port, type(host_addr))

    # parse_header(data)
    host_ip = socket.gethostbyname(host_addr)

    # connect
    client_socket.connect((host_ip, port))
    client_socket.settimeout(1)

    # receive
    while True:
        try:
            data = client_socket.recv(2048)

            print(data)

            if not data:
                break
            sock.send(data)
        except:
            break


    print("=====closing=====")
    sock.close()
    client_socket.close()


def main():
    server_socket = socket.socket()

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind(('127.0.0.1', 8888))
    server_socket.listen(5)

    while True:
        client_socket, addr = server_socket.accept()
        client_socket.settimeout(1)

        handle_thread = threading.Thread(
            target=handle_tcp, args=(client_socket, addr))

        handle_thread.start()

        # while 1:
        #     data = client_socket.recv(1)
        #     if not data:
        #         break
        #     print(data)
        # client_socket.close()


if __name__ == "__main__":
    main()
