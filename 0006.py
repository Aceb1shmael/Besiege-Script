Start_Block=Besiege.GetBlock("14e2c51f-a435-4de2-9314-4f1c4edc9931")

Very_Front_Left_Wheel=Besiege.GetBlock("5ec6975e-7092-4071-ab18-4ed97c4171e8")
Very_Front_Right_Wheel=Besiege.GetBlock("21f71d84-8905-45b3-8bbd-1aa87fb2c044")
Front_Left_Wheel=Besiege.GetBlock("cc7045fb-73d4-445b-8560-842f040692f5")
Front_Right_Wheel=Besiege.GetBlock("02f435e7-1251-43fd-b290-0ac29c3ffe31")
Rear_Left_Wheel=Besiege.GetBlock("82fab9c3-8a53-46b7-a91a-84570bf2dd1a")
Rear_Right_Wheel=Besiege.GetBlock("769a3d30-2d69-4b8b-ba78-c69c4d42bff2")
Very_Rear_Left_Wheel=Besiege.GetBlock("d6bfa01c-246e-4b29-ae21-d29f8957ae23")
Very_Rear_Right_Wheel=Besiege.GetBlock("ed945380-4e3f-42d4-8f84-beec17fe441c")


Front_Left_Hinge=Besiege.GetBlock("dac7f188-0c55-4ebf-8ffd-50541831bac2")
Front_Right_Hinge=Besiege.GetBlock("cdbe56c2-cb66-4b34-a576-ef4abaf3bf1f")
Left_Hinge=Besiege.GetBlock("38c7af84-4560-4f21-bded-28228408de03")
Right_Hinge=Besiege.GetBlock("18f2c329-3704-4a59-a65e-33d969844d32")

def FixedUpdate():
    v3=Start_Block.Velocity
    v1=(v3.x**2+v3.y**2+v3.z**2)**0.5
    c=-0.00581728+0.0711999*v1+0.000212488*v1**2-3.84276*10**-6*v1**3+4.34906*10**-8*v1**4

    if c>4:
        c=4

    if Input.GetKey(KeyCode.DownArrow) and c>0:
        c=-c+2
    

    cd=1

    vvfl=c+cd
    vvfr=c+cd
    vfl=c+cd
    vfr=c+cd
    vrl=c+cd
    vrr=c+cd
    vvrl=c+cd
    vvrr=c+cd


    al=0
    ar=0
    afl=0
    afr=0
    vl=5
    vr=5
    vhfl=5
    vhfr=5

    if Input.GetKey(KeyCode.LeftArrow):
        al=45
        ar=30
        afl=50
        afr=35
    if Input.GetKey(KeyCode.RightArrow):
        al=-30
        ar=-45
        afl=-35
        afr=-50

    if Left_Hinge.GetAngle()>=0 and Right_Hinge.GetAngle()>=0:
        vl=2
        vr=3
        vhfl=35/15
        vhfr=50/15
    if Left_Hinge.GetAngle()<=0 and Right_Hinge.GetAngle()<=0:
        vl=3
        vr=2
        vhfl=50/15
        vhfr=35/15


    if Left_Hinge.GetAngle()>=0 and Right_Hinge.GetAngle()>=0 and Input.GetKey(KeyCode.RightArrow):
        vfl=vfl*1.18275
        vvfl=vvfl*1.18275
        vfr=vfr*0.893188
        vvfr=vvfr*0.893188
        vrl=vrl*0.631579
        vvrl=vvrl*0.631579
        vrr=vrr
        vvrr=vvrr
    if Left_Hinge.GetAngle()<=0 and Right_Hinge.GetAngle()<=0 and Input.GetKey(KeyCode.LeftArrow):
        vfl=vfl*0.893188
        vvfl=vvfl*0.893188
        vfr=vfr*1.18275
        vvfr=vvfr*1.18275
        vrl=vrl*0.631579
        vvrl=vvrl*0.631579
        vrr=vrr
        vvrr=vvrr



    
    


    Front_Left_Wheel.SetSliderValue("SPEED",vfl)
    Very_Front_Left_Wheel.SetSliderValue("SPEED",vvfl)
    Front_Right_Wheel.SetSliderValue("SPEED",vfr)
    Very_Front_Right_Wheel.SetSliderValue("SPEED",vvfr)
    Rear_Left_Wheel.SetSliderValue("SPEED",vrl)
    Very_Rear_Left_Wheel.SetSliderValue("SPEED",vvrl)
    Rear_Right_Wheel.SetSliderValue("SPEED",vrr)
    Very_Rear_Right_Wheel.SetSliderValue("SPEED",vvrr)


    Left_Hinge.SetAngle(al)
    Right_Hinge.SetAngle(ar)
    Front_Left_Hinge.SetAngle(afl)
    Front_Right_Hinge.SetAngle(afr)

    Left_Hinge.SetSliderValue("ROTATION SPEED",vl)
    Right_Hinge.SetSliderValue("ROTATION SPEED",vr)
    Front_Left_Hinge.SetSliderValue("ROTATION SPEED",vhfl)
    Front_Right_Hinge.SetSliderValue("ROTATION SPEED",vhfr)

    Besiege.Watch("Speed",round(v1*3.6))