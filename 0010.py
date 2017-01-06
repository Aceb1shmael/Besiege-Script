Start_Block=Besiege.GetBlock("32da514f-59d9-43b6-80c4-7cc9309d5233")

Front_Left_Wheel=Besiege.GetBlock("c387ce17-67d1-434c-aa31-6f7e9b7472eb")
Front_Right_Wheel=Besiege.GetBlock("805984f8-3b79-43c3-9de6-931e7b772035")
Rear_Left_Wheel=Besiege.GetBlock("bc39ff67-0f43-4f93-a49c-20938eff01c0")
Rear_Right_Wheel=Besiege.GetBlock("c2eda511-0993-495d-8142-5748c2dcb466")

Left_Hinge=Besiege.GetBlock("836f40a2-b7d1-4607-8f64-5f5dcd114b78")
Right_Hinge=Besiege.GetBlock("37f33832-e91a-4d09-8ef0-d2a465f48f6c")

def FixedUpdate():
    v3=Start_Block.Velocity
    v1=(v3.x**2+v3.y**2+v3.z**2)**0.5
    c=0.073455*v1

    if c>5.5:
        c=5.5

    if Input.GetKey(KeyCode.DownArrow) and c>2.5:
        c=2.5

    cd=1.5


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
        if c>2:
            al=30
            ar=25
    if Input.GetKey(KeyCode.RightArrow):
        al=-32.2756
        ar=-45
        if c>2:
            al=-25
            ar=-30

    if Left_Hinge.GetAngle()>=0 and Right_Hinge.GetAngle()>=0:
        vl=2.15171
        vr=3
        if c>2:
            vl=2.5
            vr=3
    if Left_Hinge.GetAngle()<=0 and Right_Hinge.GetAngle()<=0:
        vl=3
        vr=2.15171
        if c>2:
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
    Rear_Right_Wheel.SetSliderValue("SPEED",vrr)


    Left_Hinge.SetAngle(al)
    Right_Hinge.SetAngle(ar)

    Left_Hinge.SetSliderValue("ROTATION SPEED",vl)
    Right_Hinge.SetSliderValue("ROTATION SPEED",vr)

    Besiege.Watch("Speed",round(v1*3.6))
    Besiege.Watch("C",c)
    Besiege.Watch("al",Left_Hinge.GetAngle())
    Besiege.Watch("ar",Right_Hinge.GetAngle())