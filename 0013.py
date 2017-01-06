Start_Block=Besiege.GetBlock("dc5f54ae-f120-4458-8d53-de8c7c3f625d")
Front_left_Steer=Besiege.GetBlock("0a8f5dc0-d104-4606-8ee2-6818076c05bc")
Front_right_Steer=Besiege.GetBlock("a9d290d3-d06f-4571-8b0d-67b61c63b47a")
Rear_left_Steer=Besiege.GetBlock("b2905128-7f33-4d15-b70a-7a3940ee89a3")
Rear_right_Steeer=Besiege.GetBlock("43a9c88d-34e0-4474-ba1e-6c3fc5eec7b1")

Front_Left_Landing_Gear=Besiege.GetBlock("b8d61dfd-2657-4b00-af20-01f69b004627")
Front_Right_Landing_Gear=Besiege.GetBlock("235a003f-e4e0-40b1-b970-5040b9f9c025")
Rear_Landing_Gear=Besiege.GetBlock("737c730e-cfbc-4733-951e-e3eb7862d5e1")

Front_Left_Piston=Besiege.GetBlock("99abc45f-b851-4d0e-abe0-92f1e6a0d094")
Front_Right_Piston=Besiege.GetBlock("446458ae-0278-4a6a-bd2d-e61634ea152b")
Rear_Piston=Besiege.GetBlock("2e1f9e09-9fcd-48d1-b2ca-8aac631c01af")

Left_Wheel=Besiege.GetBlock("8b436653-d0aa-4046-95ba-5982fe0b4426")
Right_Wheel=Besiege.GetBlock("32a1ea31-dd4e-4683-bf88-cb6ec8349a40")


s=1
vl=1
vr=1


def FixedUpdate():
    global s
    global vl
    global vr
    v3=Start_Block.Velocity
    v1=(v3.x**2+v3.y**2+v3.z**2)**0.5

    pf=0
    pr=0

    if Input.GetKey(KeyCode.UpArrow):
        pr=25
    
    if Input.GetKey(KeyCode.DownArrow):
        pr=-25
    
    if Input.GetKey(KeyCode.LeftArrow):
        pf=25
    
    if Input.GetKey(KeyCode.RightArrow):
        pf=-25


    if Input.GetKey(KeyCode.Keypad0):
        s=1
    if Input.GetKey(KeyCode.KeypadPeriod):
        s=0
    
    if s==1:
        Front_Left_Landing_Gear.SetAngle(0)
        Front_Right_Landing_Gear.SetAngle(0)
        Rear_Landing_Gear.SetAngle(0)
    if s==0:
        Front_Left_Landing_Gear.SetAngle(-90)
        Front_Right_Landing_Gear.SetAngle(-90)
        Rear_Landing_Gear.SetAngle(-60)


    if Input.GetKey(KeyCode.Keypad1):
        vl=vl-0.1
        vr=vr-0.1
    
    if Input.GetKey(KeyCode.Keypad2):
        vl=vl+0.1
        vr=vr+0.1

    if vl>=15:
        vl=15
    if vr>=15:
        vr=15
    if vl<=1:
        vl=1
    if vr<=1:
        vr=1



    Rear_left_Steer.SetAngle(pr)
    Rear_right_Steeer.SetAngle(pr)
    Front_left_Steer.SetAngle(pf)
    Front_right_Steer.SetAngle(pf)

    Front_Left_Piston.SetPosition((90-Front_Left_Landing_Gear.GetAngle())/90)
    Front_Right_Piston.SetPosition((90+Front_Right_Landing_Gear.GetAngle())/90)
    Rear_Piston.SetPosition((60+Rear_Landing_Gear.GetAngle())/60)


    Left_Wheel.SetSliderValue("SPEED",vl)
    Right_Wheel.SetSliderValue("SPEED",vr)


    Besiege.Watch("SPEED",round(v1))
    Besiege.Watch("HRIGHT",round(Start_Block.Position.y))