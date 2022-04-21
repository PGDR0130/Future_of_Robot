#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent
from ev3dev2.motor import MediumMotor, OUTPUT_A
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
import time

# 設定大馬達輸出孔
B = LargeMotor(OUTPUT_B)
A = MediumMotor(OUTPUT_A)
C = LargeMotor(OUTPUT_C)
D = LargeMotor(OUTPUT_D)
T = TouchSensor()

def turnto( a){
    A.run_to_abs_pos( position_sp = a,speed_sp = 1000)
    while A.degrees != a:
        B.run_forever(speed_sp = 500) # ya
        C.run_forever(speed_sp = 500)
        D.run_forever(speed_sp = 500)
        time.sleep(0.1)
        A.run_forever(speed_sp = -500)
        B.run_forever(speed_sp = -500)
        C.run_forever(speed_sp = -500)
        D.run_forever(speed_sp = -500)
        time.sleep(0.1)  
}

# 設定停止後煞車
A.stop_action = 'brake'
B.stop_action = 'brake'
C.stop_action = 'brake'
D.stop_action = 'brake'

A.reset()
B.reset()
C.reset()
D.reset()

"""
for i in range(10):
    A.run_forever(speed_sp = -500)
    B.run_forever(speed_sp = 500)
    C.run_forever(speed_sp = 500)
    D.run_forever(speed_sp = 500)
    time.sleep(0.2)
    A.run_forever(speed_sp = -500)
    B.run_forever(speed_sp = -500)
    C.run_forever(speed_sp = -500)
    D.run_forever(speed_sp = -500)
    time.sleep(0.2)   
A.reset()
B.reset()
C.reset()
D.reset()
"""


while not(T.is_pressed):
    A.run_forever(speed_sp = 1000)
    B.run_forever(speed_sp = 500)
    C.run_forever(speed_sp = 500)
    D.run_forever(speed_sp = 500)
    time.sleep(0.2)
    B.run_forever(speed_sp = -500)
    C.run_forever(speed_sp = -500)
    D.run_forever(speed_sp = -500)
    time.sleep(0.2)
A.reset()
B.reset()
C.reset()
D.reset()
