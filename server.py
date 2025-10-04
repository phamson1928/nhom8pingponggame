#!/usr/bin/env python3
import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", 8080))
    s.listen(2)
    print("Server listening on port 8080")
    conn, addr = s.accept()
    print("Client connected:", addr)
    conn.close()

if __name__ == "__main__":
    main()
