import sys

N = int(sys.argv[1])
M = int(sys.argv[2])
T = int(sys.argv[3])


cycle_length = N + M  # Длина полного цикла
time_in_cycle = T % cycle_length  # Время в текущем цикле

if time_in_cycle < N:
    print("green")
else:
    print("red")


