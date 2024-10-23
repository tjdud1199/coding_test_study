t = int(input())

for i in range(1, t+1):
    n = int(input())
    cmds = [list(map(int, input().split())) for _ in range(n)]
    spd = 0
    dist = 0
    for cmd in cmds:
        if cmd[0] == 0:
            dist += spd
        elif cmd[0] == 1:
            spd += cmd[1]
            dist += spd
        else:
            spd -= cmd[1]
            if spd < 0:
                spd = 0
            dist += spd
    print('#'+str(i), dist)