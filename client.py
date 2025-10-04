#!/usr/bin/env python3
import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 8080))
    print("Connected to server")
    s.close()

if __name__ == "__main__":
    main()
