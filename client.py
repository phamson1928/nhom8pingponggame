#!/usr/bin/env python3
import socket, json

def main():
    s = socket.socket()
    s.connect(("localhost",8080))
    buffer = ""
    while True:
        data = s.recv(1024).decode()
        buffer += data
        if "\\n" in buffer:
            packet, buffer = buffer.split("\\n", 1)
            print("Received:", packet)

if __name__ == "__main__":
    main()
