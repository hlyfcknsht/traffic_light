import sys
import time

M = int(sys.argv[1])  # Длительность зеленого света
N = int(sys.argv[2])  # Длительность красного света
T = int(sys.argv[3])  # Время, в которое нужно определить состояние светофора

# Определяем цикл светофора
cycle_duration = M + N

# Определяем момент времени внутри текущего цикла
current_time_in_cycle = T % cycle_duration

if M > N:
    if current_time_in_cycle <= M:
        print("Green")
    else:
        print("Red")
elif N > M:
    if current_time_in_cycle >= M:
        print("Green")
    else:
        print("Red")
else:
    print('Yellow')


