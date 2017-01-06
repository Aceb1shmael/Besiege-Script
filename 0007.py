Start_Block=Besiege.GetBlock("8063fa89-0b62-45af-b8b0-45f01ac1218d")

Front_Left_Wheel=Besiege.GetBlock("9256d552-ce43-4500-8304-c896b778d2b6")
Front_Right_Wheel=Besiege.GetBlock("66c2eff8-efeb-4eec-998a-b100fd1f0deb")
Rear_Left_Wheel=Besiege.GetBlock("993f1eab-bf8e-4143-8410-00bf2f611481")
Rear_Right_Wheel=Besiege.GetBlock("61af14ac-120b-4f3c-8687-a6836ec8a9f1")

Left_Hinge=Besiege.GetBlock("dfc69b66-ebd5-49e3-881f-ce1f3ee98e57")
Right_Hinge=Besiege.GetBlock("6789451a-43f0-4de4-8a13-a9d69dfb5a72")





Steer_3=Besiege.GetBlock("d62e7561-df4a-47a8-95c9-65a00f2ef870")

Steer_4=Besiege.GetBlock("531dff62-f315-46c9-9d18-8ecee3134243")
Steer_5=Besiege.GetBlock("4feffcff-e67b-455f-be75-4cddc03ce9f1")


vs=0
vm=0


p1=0



def FixedUpdate():
    global vs
    global vm


    global p1


    v3=Start_Block.Velocity
    v1=(v3.x**2+v3.y**2+v3.z**2)**0.5
    c=-0.816402+0.413349*v1-0.0407205*v1**2+0.00235286*v1**3-0.0000604009*v1**4+5.68135*10**-7*v1**5

    if c>4.5:
        c=4.5

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





    if Input.GetKey(KeyCode.F):
        vs=0
        vm=0
    if Input.GetKey(KeyCode.H):
        vs=0.02
        vm=0.02
    if Input.GetKey(KeyCode.G):
        vs=0.3
        vm=0.3
    if Input.GetKey(KeyCode.J):
        vs=0.005
        vm=0.005


    if Input.GetKey(KeyCode.Keypad0):
        Steer_3.SetAngle(90)
        vs=2
        vm=2
        p1=1


    if p1==1 and round(Steer_3.GetAngle())==90:
        Steer_4.SetAngle(-90)
        Steer_5.SetAngle(-90)
        vs=0
        vm=0

    if Input.GetKey(KeyCode.KeypadPeriod):
        Steer_4.SetAngle(0)
        Steer_5.SetAngle(0)
        p1=0

    if p1==0 and round(Steer_4.GetAngle())==0 and round(Steer_5.GetAngle())==0:
        Steer_3.SetAngle(45)
        



    
    
    Front_Left_Wheel.SetSliderValue("SPEED",vfl)
    Front_Right_Wheel.SetSliderValue("SPEED",vfr)
    Rear_Left_Wheel.SetSliderValue("SPEED",vrl)
    Rear_Right_Wheel.SetSliderValue("SPEED",vrr)


    Left_Hinge.SetAngle(al)
    Right_Hinge.SetAngle(ar)

    Left_Hinge.SetSliderValue("ROTATION SPEED",vl)
    Right_Hinge.SetSliderValue("ROTATION SPEED",vr)


    Besiege.Watch("Speed",round(v1))