#!/usr/bin/env python3
import socket, time

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 8080))
    print("Connected to server, sending test data")
    s.sendall(b"hello")
    time.sleep(1)
    s.close()

if __name__ == "__main__":
    main()
