import math
l = 0.5
time_int = 0.001
ang = 20*3.1415926/180
ang_v = 0
ang_a = 9.81*math.sin(ang)
angles = [ang]
for i in range(int(10/time_int)):
    ang_a = (-9.81)*(math.sin(ang)/l)
    ang_v = ang_v + ang_a*time_int
    ang = ang + ang_v*time_int + 0.5*ang_a*(time_int**2)
    angles.append(ang)

for i in range(int(10/time_int)):
    if angles[i] > angles[i-1] and angles[i] > angles[i+1]:
        print(i*time_int)
