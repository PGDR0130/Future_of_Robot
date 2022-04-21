#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent
from ev3dev2.led import Leds
from ev3dev2.auto import Button
# import controlMotor
import time

#初始設定
# 設定大馬達輸出孔
LD = LargeMotor(OUTPUT_B)
LT = LargeMotor(OUTPUT_A)
RD = LargeMotor(OUTPUT_C)
RT = LargeMotor(OUTPUT_D)
RDmid = 0
LDmid = 0
RTmid = 0
LTmid = 0
# 按鈕


# 設定停止後煞車
RD.stop_action = 'brake'
RT.stop_action = 'brake'
LD.stop_action = 'brake'
LT.stop_action = 'brake'

def resetALL():
  RD.reset()
  RT.reset()
  LD.reset()
  LT.reset()


def reset():
  global LD, LT, RD, RT, RDmid, LDmid, RTmid, LTmid
  # 前後-------------------
  RD.run_forever(speed_sp = 500 )  
  LD.run_forever(speed_sp = 500 )
  time.sleep(1)
  RD.reset()
  LD.reset()
  RD.run_forever(speed_sp = -500 )  
  LD.run_forever(speed_sp = -500 )
  time.sleep(1)
  RD.stop()
  LD.stop()

  RDmid = RD.degrees/2
  LDmid = LD.degrees/2
  #------------------------

  # 左右-------------------
  RT.run_forever( speed_sp = 500 )  
  LT.run_forever( speed_sp = 500 )
  time.sleep(1)
  RT.reset()
  LT.reset()
  RT.run_forever( speed_sp = -500)
  LT.run_forever( speed_sp = -500)
  time.sleep(1)
  RTmid = RT.degrees/2
  LTmid = LT.degrees/2
  #------------------------

def debug():
  RD.run_to_abs_pos( position_sp = RDmid ,speed_sp = 100)
  LD.run_to_abs_pos( position_sp = LDmid ,speed_sp = 100)
  RT.run_to_abs_pos( position_sp = RTmid ,speed_sp = 100)
  LT.run_to_abs_pos( position_sp = LTmid ,speed_sp = 100)
  time.sleep(2)
  print("set: {} --> real: {}".format(RDmid , RD.degrees))
  print("set: {} --> real: {}".format(LDmid , LD.degrees))
  print("set: {} --> real: {}".format(RTmid , RT.degrees))
  print("set: {} --> real: {}".format(LTmid , LT.degrees))

reset()
debug()
resetALL()

while True:
    #案
    if(Button().up):
      reset()
      debug() 
      resetALL()

    # controlMotor.area(LD, LT)

    # 返回原位
    if(abs(RD.degrees) > 2):
        RD.run_to_abs_pos( position_sp = 0 ,speed_sp = 20)
        # print("RD:",RD.degrees)
    if(abs(RT.degrees) > 2):
        RT.run_to_abs_pos( position_sp = 0 ,speed_sp = 20)
        # print("RT:",RT.degrees)
    if(abs(LD.degrees) > 2):
        LD.run_to_abs_pos( position_sp = 0 ,speed_sp = 20)
        # print("LD:",LD.degrees)
    if(abs(LT.degrees) > 2):
        LT.run_to_abs_pos( position_sp = 0 ,speed_sp = 20)
        # print("LT:",LT.degrees)
    