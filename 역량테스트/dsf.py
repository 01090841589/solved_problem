import socket
import time
import math

# User and Game Server Information
NICKNAME = '당신'
HOST = '127.0.0.1'
PORT = 1447 # Do not modify

# predefined variables(Do not modify these values)
TABLE_WIDTH = 254
TABLE_HEIGHT = 124
NUMBER_OF_BALLS = 5
HOLES = [ [0, 0], [130, 0], [260, 0], [0, 130], [130, 130], [260, 130] ]

class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: ' + HOST + ':' + str(PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: ' + HOST + ':' + str(PORT))
        send_data = '9901/' + NICKNAME
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play.\n--------------------')
    def request(self):
        self.sock.send('9902/9902'.encode())
        print('Received Data has been currupted, Resend Requested.')
    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: ' + recv_data)
        return recv_data
    def send(self, angle, power):
        merged_data = '%d/%d' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: ' + merged_data)
    def close(self):
        self.sock.close()

class GameData:
    def __init__(self):
        self.reset()
    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]
    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = int(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)
    def show(self):
        print('=== Arrays ===')
        for i in range(NUMBER_OF_BALLS):
            print('Ball%d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print()

# 자신의 차례가 되어 게임을 진행해야 할 때 호출되는 Method
def play(conn, gameData):
    angle = 0
    power = 150
    ret = 9999
    ballcnt = 1
    while (gameData.balls[ballcnt][0] == 0 and gameData.balls[ballcnt][1] == 0):
        ballcnt += 1
    ch = 0
    for i, xy in enumerate(HOLES):
        tmp = abs(gameData.balls[ballcnt][0] - xy[0]) + abs(gameData.balls[ballcnt][1] - xy[1])
        if ret > tmp:
            ret = tmp
            ch = i

    dy = gameData.balls[ballcnt][1] -gameData.balls[0][1]
    dx = gameData.balls[ballcnt][0] -gameData.balls[0][0]
    cy = HOLES[ch][1] - gameData.balls[ballcnt][1]
    cx = HOLES[ch][0] - gameData.balls[ballcnt][0]

    print(cx)
    print(cy)

    if gameData.balls[ballcnt][0] == gameData.balls[0][0]:
        ts = math.atan(dy / (dx - 1))
    else:
        ts = math.atan(dy / dx)
    cts = math.degrees((math.atan(cy/cx)))
    rts = math.degrees(ts)

    dist = math.sqrt(dy ** 2 + dx ** 2)

    if dy < 0 and dx < 0:
        rts += 180
    if dy > 0 and dx < 0:
        rts += 180


    if abs(cts - rts) < 5:
        angle = (90 - rts)
    if cts - rts > 0:
        if dist > 150:
            angle = (90 - rts) + 1
        elif dist > 200:
            angle = (90 - rts)
        else:
            angle =  (90 - rts) + 3
    else:
        if dist > 150:
            angle = (90 - rts) - 1
        elif dist > 200:
            angle = (90 - rts)
        else:
            angle = (90 - rts) - 3
    # if gameData.balls[ballcnt][1] == gameData.balls[0][1]:
    #     angle -= 2
    print(dist)
    power = max(120, (dist - 10))
    conn.send(angle, power)

def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        gameData.show()
        if gameData.balls[0][0] == 9909:
            break
        play(conn, gameData)
    conn.close()
    print('Connection Closed')

if __name__ == '__main__':
    main()
