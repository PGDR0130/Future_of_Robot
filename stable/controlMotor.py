# 分區
def area(LD, LT):
    """
    input -> degrees : ev3dev2.motor class
    分八區
    LD -> 左邊馬達、控制前後
    LT -> 左邊馬達、控制轉向
    """
    if(abs(LD.degrees)>3 or abs(LT.degrees)>3):
        # 左上
        if(LD > 0 and LT > 0):
            # 右上上
            if(abs(LD) > abs(LT)):
                pass
            # 右右上
            elif(abs(LD) < abs(LT)):
                pass
        # 左右
        elif(LD > 0 and LT < 0):
            # 左上上
            if(abs(LD) > abs(LT)):
                pass
            # 左左上
            elif(abs(LD) < abs(LT)):
                pass
        # 右下
        elif(LD < 0 and LT > 0):
            # 右右下
            if(abs(LD) > abs(LT)):
                pass
            # 右下下
            if(abs(LD) < abs(LT)):
                pass
        # 左下
        elif(LD < 0 and LT < 0):
            # 左左下
            if(abs(LD) > abs(LT)):
                pass
            #  左下下
            if(abs(LD) < abs(LT)):
                pass