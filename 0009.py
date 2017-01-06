Start_Block=Besiege.GetBlock("192283d4-9b9e-4cb2-90d7-0ff9a51a501f")
Front_left_Steer=Besiege.GetBlock("9f920fa8-9b18-4d02-b3dd-909a39dc103c")
Front_right_Steer=Besiege.GetBlock("782c20c9-c6e5-4c2c-b6e0-347dc792b88c")
Rear_left_Steer=Besiege.GetBlock("a129ca96-608a-4fdd-8ca0-40f9e5d720ab")
Rear_right_Steeer=Besiege.GetBlock("87ddb122-6187-4a03-8d06-64e89c4dd027")


Front_Left_Landing_Gear=Besiege.GetBlock("c969f862-1a21-4849-bdbc-d39147908af8")
Front_Right_Landing_Gear=Besiege.GetBlock("5e0d19cb-a9bc-412c-991b-2b21ba6d81be")
Rear_Landing_Gear=Besiege.GetBlock("d197723e-4ca0-44e5-a0d1-95a459e316be")

Front_Left_Piston=Besiege.GetBlock("60622e64-4217-4395-be23-3c950f326212")
Front_Right_Piston=Besiege.GetBlock("5e19fb06-6bdd-4a65-93b7-1f21c3def7cb")

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
        Front_Left_Landing_Gear.SetAngle(0)
        Front_Right_Landing_Gear.SetAngle(0)
        Rear_Landing_Gear.SetAngle(0)
    if s==0:
        Front_Left_Landing_Gear.SetAngle(45)
        Front_Right_Landing_Gear.SetAngle(45)
        Rear_Landing_Gear.SetAngle(90)


    Rear_left_Steer.SetAngle(pr)
    Rear_right_Steeer.SetAngle(pr)
    Front_left_Steer.SetAngle(pf)
    Front_right_Steer.SetAngle(pf)


    Front_Left_Piston.SetPosition((45+Front_Left_Landing_Gear.GetAngle())/45)
    Front_Right_Piston.SetPosition((45-Front_Right_Landing_Gear.GetAngle())/45)

    Besiege.Watch("SPEED",round(v1))
    Besiege.Watch("HRIGHT",round(Start_Block.Position.y))