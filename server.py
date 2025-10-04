#!/usr/bin/env python3
import socket, threading, random, time

WIDTH, HEIGHT = 800, 600

class GameServer:
    def __init__(self):
        self.paddles = {0: 250, 1: 250}
        self.ball = {"x": WIDTH//2, "y": HEIGHT//2}

def main():
    gs = GameServer()
    print("Initial state:", gs.ball)

if __name__ == "__main__":
    main()
