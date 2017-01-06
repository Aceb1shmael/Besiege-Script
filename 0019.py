Start_Block=Besiege.GetBlock("73b197f0-19f7-486d-8985-9450c0ae6968")

Front_Left_Wheel=Besiege.GetBlock("17d0b001-eda1-47d6-a007-d4d2a67b092f")
Front_Right_Wheel=Besiege.GetBlock("8ce260af-ef38-46d4-8e58-b120c6d0f4aa")
Rear_Left_Wheel=Besiege.GetBlock("1d6c344f-c83d-46e5-b8cf-e0e778f6e88f")
Rear_Right_Wheel=Besiege.GetBlock("32616172-cedb-4ef0-bf16-c3ae56296605")

Left_Hinge=Besiege.GetBlock("420cc02f-0027-4a54-88ac-648b6518dccb")
Right_Hinge=Besiege.GetBlock("2d40ef47-118f-4e5c-964b-6df94961c87b")

def FixedUpdate():
    v3=Start_Block.Velocity
    v1=(v3.x**2+v3.y**2+v3.z**2)**0.5
    c=-0.00581728+0.0711999*v1+0.000212488*v1**2-3.84276*10**-6*v1**3+4.34906*10**-8*v1**4

    if c>2.5:
        c=2.5
    
    if Input.GetKey(KeyCode.DownArrow) and c>0:
        c=-c+3

    cd=2.5


    vfl=c+cd
    vfr=c+cd
    vrl=c+cd
    vrr=c+cd


    al=0
    ar=0
    vl=5
    vr=5

    if Input.GetKey(KeyCode.LeftArrow):
        al=45
        ar=32.2756
    if Input.GetKey(KeyCode.RightArrow):
        al=-32.2756
        ar=-45

    if Left_Hinge.GetAngle()>=0 and Right_Hinge.GetAngle()>=0:
        vl=2.15171
        vr=3
    if Left_Hinge.GetAngle()<=0 and Right_Hinge.GetAngle()<=0:
        vl=3
        vr=2.15171


    if Left_Hinge.GetAngle()>=0 and Right_Hinge.GetAngle()>=0 and Input.GetKey(KeyCode.RightArrow):
        vfl=vfl*1.18275
        vfr=vfr*0.893188
        vrl=vrl
        vrr=vrr*0.631579
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

    Besiege.Watch("Speed",round(v1*3.6,1))