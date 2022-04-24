# 分區
def area(LD, LT):
    """
    input -> degrees : ev3dev2.motor class
    分八區
    LD -> 左邊馬達、控制前後
    LT -> 左邊馬達、控制轉向
    """
    LD_d, LT_d = LD.degrees, LT.degrees
    # 八個方向 --> 沒有單直線或轉彎
    if(abs(LD_d)>3 and abs(LT_d)>3):
        # 左上
        if(LD_d > 0 and LT_d > 0):
            # 右上上
            if(abs(LD_d) > abs(LT_d)):
                pass
            # 右右上
            elif(abs(LD_d) < abs(LT_d)):
                pass
        # 左右
        elif(LD_d > 0 and LT_d < 0):
            # 左上上
            if(abs(LD_d) > abs(LT_d)):
                pass
            # 左左上
            elif(abs(LD_d) < abs(LT_d)):
                pass
        # 右下
        elif(LD_d < 0 and LT_d > 0):
            # 右右下
            if(abs(LD_d) > abs(LT_d)):
                pass
            # 右下下
            if(abs(LD_d) < abs(LT_d)):
                pass
        # 左下
        elif(LD_d < 0 and LT_d < 0):
            # 左左下
            if(abs(LD_d) > abs(LT_d)):
                pass
            #  左下下
            if(abs(LD_d) < abs(LT_d)):
                pass

    # 單直線(前進、後退)
    elif(abs(LD_d) > 3 and abs(LT_d) < 3):
         pass
        
    # 單轉彎(左轉、右轉)
    elif(abs(LD_d) < 3 and abs(LT_d) > 3):
        pass 