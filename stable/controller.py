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
# 按鈕


# 設定停止後煞車
RD.stop_action = 'brake'
RT.stop_action = 'brake'
LD.stop_action = 'brake'
LT.stop_action = 'brake'

def RD_runto(a):
  while RD.degrees != a:
    RD.run_to_abs_pos( position_sp = a ,speed_sp = RD.degrees*-2)
    time.sleep(0.01)
  RD.stop

def LD_runto(a):
  while LD.degrees != a:
    LD.run_to_abs_pos( position_sp = a ,speed_sp = LD.degrees*-2)
    time.sleep(0.01)
  LD.stop

def LT_runto(a):
  while LT.degrees != a:
    LT.run_to_abs_pos( position_sp = a ,speed_sp = LT.degrees*-2)
    time.sleep(0.01)
  LT.stop

def RT_runto(a):
  while RT.degrees != a:
    RT.run_to_abs_pos( position_sp = a ,speed_sp = RT.degrees*-2)
    time.sleep(0.01)
  RT.stop



def resetALL():
  RD.reset()
  RT.reset()
  LD.reset()
  LT.reset()


def resetD():
  global RDmid ,LDmid ,RD ,LD
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

  RD_runto(RDmid)
  LD_runto(LDmid)
  time.sleep(2)
  #------------------------
def resetT():
  global RTmid ,LTmid ,RT ,LT
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

  RT_runto(RTmid)
  LT_runto(LTmid)
  time.sleep(2)
  #------------------------

def debug():
  print("set: {} --> real: {}".format(RDmid , RD.degrees))
  print("set: {} --> real: {}".format(LDmid , LD.degrees))
  print("set: {} --> real: {}".format(RTmid , RT.degrees))
  print("set: {} --> real: {}".format(LTmid , LT.degrees))

resetD()
resetT()
debug()
resetALL()

'''while True:
    #案
    if(Button().up):
      reset()
      debug() 
      resetALL()

    # controlMotor.area(LD, LT)

    # 返回原位
    if(abs(RD.degrees) > 2):
        RD.run_to_abs_pos( position_sp = 0 ,speed_sp = 80)
        # print("RD:",RD.degrees)
    if(abs(RT.degrees) > 2):
        RT.run_to_abs_pos( position_sp = 0 ,speed_sp = 80)
        # print("RT:",RT.degrees)
    if(abs(LD.degrees) > 2):
        LD.run_to_abs_pos( position_sp = 0 ,speed_sp = 80)
        # print("LD:",LD.degrees)
    if(abs(LT.degrees) > 2):
        LT.run_to_abs_pos( position_sp = 0 ,speed_sp = 80)
        # print("LT:",LT.degrees)
'''