Start_Block=Besiege.GetBlock("4e25d5fe-ad66-44f7-b879-f798034567bb")

Front_Left_Wheel=Besiege.GetBlock("bec81514-7df2-42a7-8d8b-a790f24b50b6")
Front_Right_Wheel=Besiege.GetBlock("dd7aa37d-2379-4852-86c9-0dadcd585c8c")
Rear_Left_Wheel=Besiege.GetBlock("17de19b4-c6a7-4546-b1fe-34d062f16a15")
Rear_Right_Wheel=Besiege.GetBlock("67b1bd0b-1b18-4dcd-8e8f-1edf84a9063d")

Left_Hinge=Besiege.GetBlock("f7a681af-370e-4605-875b-a4c79282196c")
Right_Hinge=Besiege.GetBlock("1243dc7b-ebaf-4e6a-89f3-7af463e03720")


def FixedUpdate():



    v3=Start_Block.Velocity
    v1=(v3.x**2+v3.y**2+v3.z**2)**0.5
    c=-0.0108973+0.0839296*v1-0.00144851*v1**2+0.0000581239*v1**3-6.45194*10**-7*v1**4

    if c>4:
        c=4

    if Input.GetKey(KeyCode.DownArrow) and c>2.5:
        c=2.5
    

    cd=1


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


    Besiege.Watch("Speed",round(v1))