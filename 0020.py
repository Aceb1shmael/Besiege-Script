Start_Block=Besiege.GetBlock("4f6993eb-e483-4f6d-9618-5b6940abc306")
Front_left_Steer=Besiege.GetBlock("771a3086-7b1b-4e38-8022-2dce975b06eb")
Front_right_Steer=Besiege.GetBlock("10e26ec6-d349-4c3d-894a-0bf1bb402b8c")
Rear_left_Steer=Besiege.GetBlock("1af37dfa-5495-4321-9f9c-c3c1d2bf90a7")
Rear_right_Steeer=Besiege.GetBlock("591cdd8e-453b-461c-b454-a2c660bb2261")


Front_Landing_Gear=Besiege.GetBlock("3fc51cbd-d408-4e04-8752-14daf381ca66")

Front_Piston=Besiege.GetBlock("1f1548a2-e2fe-417e-9817-9000f0f817bb")

Rear_Left_1_Landing_Gear=Besiege.GetBlock("9e8af524-d244-4760-aeb8-01c24e4d5e89")
Rear_Left_2_Landing_Gear=Besiege.GetBlock("80a539c8-531d-47e0-891a-998fa6d2aef1")
Rear_Right_1_Landing_Gear=Besiege.GetBlock("5cb4acc8-6de0-49a8-9913-f7b46fe96429")
Rear_Right_2_Landing_Gear=Besiege.GetBlock("6335f9b7-9ebc-4426-84c3-6f948ef00bbc")

Rear_Left_1_Piston=Besiege.GetBlock("ec4b8542-0ec0-4a20-a784-19d589e1cf19")
Rear_Left_2_Piston=Besiege.GetBlock("4157d45f-7c53-4375-a467-8fcc5e40093c")
Rear_Right_1_Piston=Besiege.GetBlock("c6f3649a-1c62-49c4-8793-1d25080f4524")
Rear_Right_2_Piston=Besiege.GetBlock("43e04ee1-11d0-4c5e-b695-bbf9eeff21c9")

s=1

def FixedUpdate():
    global s
    v3=Start_Block.Velocity
    v1=(v3.x**2+v3.y**2+v3.z**2)**0.5

    pf=0
    pr=0

    if Input.GetKey(KeyCode.UpArrow):
        pr=25
    
    if Input.GetKey(KeyCode.DownArrow):
        pr=-25
    
    if Input.GetKey(KeyCode.LeftArrow):
        pf=15
    
    if Input.GetKey(KeyCode.RightArrow):
        pf=-15

    if Input.GetKey(KeyCode.Keypad0):
            s=1
    if Input.GetKey(KeyCode.KeypadPeriod):
        s=0
    
    if s==1:
        Front_Landing_Gear.SetAngle(90)
        Rear_Left_1_Landing_Gear.SetAngle(-55)
        Rear_Left_2_Landing_Gear.SetAngle(-60)
        Rear_Right_1_Landing_Gear.SetAngle(-55)
        Rear_Right_2_Landing_Gear.SetAngle(-60)
    if s==0:
        Front_Landing_Gear.SetAngle(0)
        Rear_Left_1_Landing_Gear.SetAngle(0)
        Rear_Left_2_Landing_Gear.SetAngle(0)
        Rear_Right_1_Landing_Gear.SetAngle(0)
        Rear_Right_2_Landing_Gear.SetAngle(0)


    Rear_left_Steer.SetAngle(pr)
    Rear_right_Steeer.SetAngle(pr)
    Front_left_Steer.SetAngle(pf)
    Front_right_Steer.SetAngle(pf)


    Front_Piston.SetPosition(-Front_Landing_Gear.GetAngle()/90)
    Rear_Left_1_Piston.SetPosition(-0.5*Rear_Left_1_Landing_Gear.GetAngle()/55)
    Rear_Left_2_Piston.SetPosition(-0.5*Rear_Left_2_Landing_Gear.GetAngle()/60)
    Rear_Right_1_Piston.SetPosition(0.5*Rear_Right_1_Landing_Gear.GetAngle()/55)
    Rear_Right_2_Piston.SetPosition(0.5*Rear_Right_2_Landing_Gear.GetAngle()/60)

    Besiege.Watch("SPEED",round(v1))
    Besiege.Watch("HRIGHT",round(Start_Block.Position.y))