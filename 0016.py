Start_Block=Besiege.GetBlock("bd5da400-fba7-4b0d-979b-7defad9e0608")

Front_Left_Wheel=Besiege.GetBlock("0145ab53-04a8-4c52-a5e8-8d0003dfd38e")
Front_Right_Wheel=Besiege.GetBlock("66a11cd9-8f87-4cad-b50f-f005fb507f36")
Rear_Left_Wheel=Besiege.GetBlock("5b8d3460-4bc0-40f7-872b-5233840906b7")
Rear_Right_Wheel=Besiege.GetBlock("55465d82-c516-445b-a82b-d90394e0dc0a")

Left_Hinge=Besiege.GetBlock("e3d36801-184f-43ff-a288-feb7084587e2")
Right_Hinge=Besiege.GetBlock("cc712d9f-8f61-4836-8ef8-427fb991d1fb")

def FixedUpdate():
    v3=Start_Block.Velocity
    v1=(v3.x**2+v3.y**2+v3.z**2)**0.5
    c=-0.026117+0.082638*v1-0.000190405*v1**2+1.29754*10**-6*v1**3+5.97362*10**-8*v1**4

    if c>5:
        c=5

    if Input.GetKey(KeyCode.DownArrow) and c>0:
        c=-c+2.5
    


    vfl=c+2
    vfr=c+2
    vrl=c+2
    vrr=c+2


    al=0
    ar=0
    vl=5
    vr=5

    if Input.GetKey(KeyCode.LeftArrow):
        al=40
        ar=35
    if Input.GetKey(KeyCode.RightArrow):
        al=-35
        ar=-40

    if Left_Hinge.GetAngle()>=0 and Right_Hinge.GetAngle()>=0:
        vl=3.5
        vr=4
    if Left_Hinge.GetAngle()<=0 and Right_Hinge.GetAngle()<=0:
        vl=4
        vr=3.5


    if Left_Hinge.GetAngle()>=0 and Right_Hinge.GetAngle()>=0 and Input.GetKey(KeyCode.RightArrow):
        vfl=vfl*1.18275
        vfr=vfr*0.893188
        vrl=vrl*0.631579
        vrr=vrr
    if Left_Hinge.GetAngle()<=0 and Right_Hinge.GetAngle()<=0 and Input.GetKey(KeyCode.LeftArrow):
        vfl=vfl*0.893188
        vfr=vfr*1.18275
        vrl=vrl
        vrr=vrr*0.631579



    
    


    Front_Left_Wheel.SetSliderValue("SPEED",vfl)
    Front_Right_Wheel.SetSliderValue("SPEED",vfr)
    Rear_Left_Wheel.SetSliderValue("SPEED",vrl)
    Rear_Right_Wheel.SetSliderValue("SPEED",vrr)


    Left_Hinge.SetAngle(al)
    Right_Hinge.SetAngle(ar)

    Left_Hinge.SetSliderValue("ROTATION SPEED",vl)
    Right_Hinge.SetSliderValue("ROTATION SPEED",vr)

    Besiege.Watch("Speed",round(v1))
    Besiege.Watch("C",c)