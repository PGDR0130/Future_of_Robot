#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent
from ev3dev2.led import Leds
import time

# 設定大馬達輸出孔
LD = LargeMotor(OUTPUT_B)
LT = LargeMotor(OUTPUT_A)
RD = LargeMotor(OUTPUT_C)
RT = LargeMotor(OUTPUT_D)

# 設定停止後煞車
RD.stop_action = 'brake'
RT.stop_action = 'brake'
LD.stop_action = 'brake'
LT.stop_action = 'brake'



#永遠執行 speed_sp --> 
RD.run_forever(speed_sp = 500 )  
LD.run_forever(speed_sp = 500 )
time.sleep(1)


RD.reset()
LD.reset()
# 取得馬達角度
print(RD.degrees)
print(LD.degrees)


RD.run_forever(speed_sp = -500 )  
LD.run_forever(speed_sp = -500 )
time.sleep(1)

print(RD.degrees)
print(LD.degrees)

RDmid = RD.degrees/2
LDmid = LD.degrees/2


RD.run_to_abs_pos( position_sp = RDmid ,speed_sp = 200)
LD.run_to_abs_pos( position_sp = LDmid ,speed_sp = 200)
time.sleep(1)

print(RT.degrees)
print(LT.degrees)


RT.run_forever( speed_sp = 500 )  
LT.run_forever( speed_sp = 500 )
time.sleep(1)


RT.reset()
LT.reset()
# 取得馬達角度
print(RT.degrees)
print(LT.degrees)


RT.run_forever( speed_sp = -500)
LT.run_forever( speed_sp = -500)
time.sleep(1)

print(RT.degrees)
print(LT.degrees)

RTmid = RT.degrees/2
LTmid = LT.degrees/2


RT.run_to_abs_pos( position_sp = RTmid ,speed_sp = 200)
LT.run_to_abs_pos( position_sp = LTmid ,speed_sp = 200)
time.sleep(1)


print(RT.degrees)
print(LT.degrees)

RD.reset()
RT.reset()
LD.reset()
LT.reset()

while True:
    if(abs(RD.degrees) > 2):
        RD.run_to_abs_pos( position_sp = 0 ,speed_sp = 10)
        print("RD:",RD.degrees)
    if(abs(RT.degrees) > 2):
        RT.run_to_abs_pos( position_sp = 0 ,speed_sp = 10)
        print("RT:",RT.degrees)
    if(abs(LD.degrees) > 2):
        LD.run_to_abs_pos( position_sp = 0 ,speed_sp = 10)
        print("LD:",LD.degrees)
    if(abs(LT.degrees) > 2):
        LT.run_to_abs_pos( position_sp = 0 ,speed_sp = 10)
        print("LT:",LT.degrees)
#取controller角度
      ''''
class Motor(port,positive_direction=Direction.CLOCKWISE, gears=None):
  while True:
    if(RT.degrees==0):
      run_until_stalled(speed, then=Stop.COAST, duty_limit=None)
      print("RT:",RT.degrees)
    elif(RT.degrees==30):
      run_until_stalled(speed, then=Stop.COAST, duty_limit=None)
      print("RT:",RT.degrees)
    elif(RD.degrees==0)
      run_until_stalled(speed, then=Stop.COAST, duty_limit=None)
      print("RD:",RD.degrees)
    elif(RD.degrees==30):
      run_until_stalled(speed, then=Stop.COAST, duty_limit=None)
      print("RD:",RD.degrees)
    if(LT.degrees==0):
      run_until_stalled(speed, then=Stop.COAST, duty_limit=None)
      print("LT:",LT.degrees)
    elif(LT.degrees==30):
      run_until_stalled(speed, then=Stop.COAST, duty_limit=None)
      print("LT:",LT.degrees)
    elif(LD.degrees==0)
      run_until_stalled(speed, then=Stop.COAST, duty_limit=None)
      print("LD:",LD.degrees)
    elif(LD.degrees==30):
      run_until_stalled(speed, then=Stop.COAST, duty_limit=None)
      print("LD:",LD.degrees)
    '''
     