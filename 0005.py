Start_Block=Besiege.GetBlock("c3045dda-97a3-4db7-a364-8906ea78ae7f")

Front_Left_Wheel=Besiege.GetBlock("fa426e93-9368-46d0-84f3-8c2e9ab90ae4")
Front_Right_Wheel=Besiege.GetBlock("893b9ecf-6c2c-464a-9b5e-d0d45a5845b9")
Rear_Left_Wheel=Besiege.GetBlock("39b8b32c-2ed2-4214-8584-081755fe6790")
Rear_Right_Wheel=Besiege.GetBlock("4b1387d6-8a49-42cb-9480-a10a45c29679")

Left_Hinge=Besiege.GetBlock("24092ee6-4a9c-4106-8d74-cf422b2c8849")
Right_Hinge=Besiege.GetBlock("2dca19f3-c46e-4724-8a11-b37491288a07")

def FixedUpdate():
    v3=Start_Block.Velocity
    v1=(v3.x**2+v3.y**2+v3.z**2)**0.5
    c=0.073455*v1

    if c>3.5:
        c=3.5

    if Input.GetKey(KeyCode.DownArrow) and c>2.5:
        c=2.5


    vfl=c+1
    vfr=c+1
    vrl=c+1
    vrr=c+1


    al=0
    ar=0
    vl=5
    vr=5

    if Input.GetKey(KeyCode.LeftArrow):
        al=35
        ar=20
    if Input.GetKey(KeyCode.RightArrow):
        al=-20
        ar=-35

    if Left_Hinge.GetAngle()>=0 and Right_Hinge.GetAngle()>=0:
        vl=2
        vr=3.5
    if Left_Hinge.GetAngle()<=0 and Right_Hinge.GetAngle()<=0:
        vl=3.5
        vr=2


    if Left_Hinge.GetAngle()>=0 and Right_Hinge.GetAngle()>=0 and Input.GetKey(KeyCode.RightArrow):
        vfl=vfl*1.18275
        vfr=vfr*0.893188
        vrl=vrl*0.631579
        vrr=vrr
    if Left_Hinge.GetAngle()<=0 and Right_Hinge.GetAngle()<=0 and Input.GetKey(KeyCode.LeftArrow):
        vfl=vfl*0.893188
        vfr=vfr*1.18275
        vrl=vrl*0.631579
        vrr=vrr



    
    


    Front_Left_Wheel.SetSliderValue("SPEED",vfl)
    Front_Right_Wheel.SetSliderValue("SPEED",vfr)
    Rear_Left_Wheel.SetSliderValue("SPEED",vrl)
    Rear_Right_Wheel.SetSliderValue("SPEED",vrr)


    Left_Hinge.SetAngle(al)
    Right_Hinge.SetAngle(ar)

    Left_Hinge.SetSliderValue("ROTATION SPEED",vl)
    Right_Hinge.SetSliderValue("ROTATION SPEED",vr)

    Besiege.Watch("Speed",round(v1*3.6))
    Besiege.Watch("C",c)
    Besiege.Watch("al",Left_Hinge.GetAngle())
    Besiege.Watch("ar",Right_Hinge.GetAngle())