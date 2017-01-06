Start_Block=Besiege.GetBlock("9bbded59-9744-43e0-8256-670b988de35b")

Front_Left_Wheel=Besiege.GetBlock("dc0502b0-a880-414b-a20c-d270e22f6133")
Front_Right_Wheel=Besiege.GetBlock("a19e8df1-82f9-4586-9789-d25336d81353")
Rear_Left_Wheel=Besiege.GetBlock("648d53e9-011c-4cb8-b975-1134b293db87")
Rear_Right_Wheel=Besiege.GetBlock("84ac16a7-efd0-4adb-b43c-653e1141f0f2")

Left_Hinge=Besiege.GetBlock("e4da0088-ad20-4087-b7b1-1493236b6e4e")
Right_Hinge=Besiege.GetBlock("c4cc74ff-5d1f-4e7d-b4bf-d6e8d20a0bf0")

def FixedUpdate():
    v3=Start_Block.Velocity
    v1=(v3.x**2+v3.y**2+v3.z**2)**0.5
    c=0.026593356789252537+0.06941790435518061*v1+0.00029127266951679457*v1**2

    if c>5:
        c=5

    if Input.GetKey(KeyCode.DownArrow) and c>0:
        c=-c+3.5


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
        ar=28.2843
    if Input.GetKey(KeyCode.RightArrow):
        al=-28.2843
        ar=-40

    if Left_Hinge.GetAngle()>=0 and Right_Hinge.GetAngle()>=0:
        vl=2.82843
        vr=4
    if Left_Hinge.GetAngle()<=0 and Right_Hinge.GetAngle()<=0:
        vl=4
        vr=2.82843


    if Left_Hinge.GetAngle()>=0 and Right_Hinge.GetAngle()>=0 and Input.GetKey(KeyCode.RightArrow):
        vfl=vfl*1.13558
        vfr=vfr*0.83712
        vrl=vrl
        vrr=vrr*0.641273
    if Left_Hinge.GetAngle()<=0 and Right_Hinge.GetAngle()<=0 and Input.GetKey(KeyCode.LeftArrow):
        vfl=vfl*0.83712
        vfr=vfr*1.13558
        vrl=vrl*0.641273
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
    Besiege.Watch("C",c)