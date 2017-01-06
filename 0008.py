Start_Block=Besiege.GetBlock("5c19343b-d7d5-4913-b78f-b1c5b63ba54b")

Front_Left_Wheel=Besiege.GetBlock("ef13b691-c552-45ac-a4aa-1cd578d3f440")
Front_Right_Wheel=Besiege.GetBlock("b2c35c71-a60f-4757-b9c8-a5f39fec1079")
Rear_Left_Wheel=Besiege.GetBlock("b2b8eda7-affb-4020-8294-3b1ccc1e811a")
Rear_Right_Wheel=Besiege.GetBlock("cc8c86f9-21cc-4950-9421-b21a151ad1d0")
Rear_Left_Wheel_1=Besiege.GetBlock("dd1677db-1594-45f7-80e5-33b38222be70")
Rear_Right_Wheel_1=Besiege.GetBlock("68f06512-0fb6-438b-906d-a47e0c1a1771")

Left_Hinge=Besiege.GetBlock("eaa31090-0c47-4e69-b9ef-4e3763c1f78f")
Right_Hinge=Besiege.GetBlock("6815a701-e291-424c-a8c4-fe41b79895ac")

Left_Momentum=Besiege.GetBlock("2bdbb7e4-478f-46c0-99bf-8638d59d872c")
Right_Momentum=Besiege.GetBlock("7f53b023-a9fc-40c3-a498-57226fac4d44")


cd=0
def FixedUpdate():
    global cd
    v3=Start_Block.Velocity
    v1=(v3.x**2+v3.y**2+v3.z**2)**0.5
    c=-0.00581728+0.0711999*v1+0.000212488*v1**2-3.84276*10**-6*v1**3+4.34906*10**-8*v1**4

    if c>4:
        c=4

    if Input.GetKey(KeyCode.DownArrow) and c>2.5:
        c=2.5
    
    if Input.GetKey(KeyCode.UpArrow):
        cd=1
    if Input.GetKey(KeyCode.DownArrow):
        cd=0.5-2*c


    vfl=c+cd
    vfr=c+cd
    vrl=c+cd
    vrr=c+cd


    al=0
    ar=0
    vl=5
    vr=5

    if Input.GetKey(KeyCode.LeftArrow):
        al=30
        ar=25
    if Input.GetKey(KeyCode.RightArrow):
        al=-25
        ar=-30

    if Left_Hinge.GetAngle()>=0 and Right_Hinge.GetAngle()>=0:
        vl=2.5
        vr=3
    if Left_Hinge.GetAngle()<=0 and Right_Hinge.GetAngle()<=0:
        vl=3
        vr=2.5


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
    Rear_Left_Wheel_1.SetSliderValue("SPEED",vrl)
    Rear_Right_Wheel.SetSliderValue("SPEED",vrr)
    Rear_Right_Wheel_1.SetSliderValue("SPEED",vrr)


    Left_Momentum.SetSliderValue("SPEED",c*1.5)
    Right_Momentum.SetSliderValue("SPEED",c*1.5)


    Left_Hinge.SetAngle(al)
    Right_Hinge.SetAngle(ar)

    Left_Hinge.SetSliderValue("ROTATION SPEED",vl)
    Right_Hinge.SetSliderValue("ROTATION SPEED",vr)

    Besiege.Watch("Speed",round(v1*3.6))