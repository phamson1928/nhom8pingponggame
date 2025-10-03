#!/usr/bin/env python3
import socket, threading, json, time

class GameServer:
    def __init__(self):
        self.paddles = {0:250, 1:250}
        self.ball = {"x":400, "y":300}
    def run(self):
        s = socket.socket()
        s.bind(("localhost",8080))
        s.listen(2)
        conn, _ = s.accept()
        while True:
            state = json.dumps({"paddles": self.paddles, "ball": self.ball}) + "\\n"
            conn.sendall(state.encode())
            time.sleep(0.1)

if __name__ == "__main__":
    GameServer().run()
