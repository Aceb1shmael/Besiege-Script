Start_Block=Besiege.GetBlock("708f8883-f18b-46c1-a76f-f6d189b634dd")
Front_left_Steer=Besiege.GetBlock("8b42bbb5-61b6-4f8f-a5db-e962d5679441")
Front_right_Steer=Besiege.GetBlock("ad98cd8a-b56e-4296-97f5-f6f5da068082")
Rear_left_Steer=Besiege.GetBlock("14d26028-f0a7-41f2-a31b-aee3f6f53bf9")
Rear_right_Steeer=Besiege.GetBlock("7b53384c-a0d7-4c4c-bb69-ccc50b56faf1")


Front_Landing_Gear=Besiege.GetBlock("8e57d8b6-ecc7-42b0-82a5-5d1d62eb5488")

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
        Front_Landing_Gear.SetAngle(0)
    if s==0:
        Front_Landing_Gear.SetAngle(90)


    Rear_left_Steer.SetAngle(pr)
    Rear_right_Steeer.SetAngle(pr)
    Front_left_Steer.SetAngle(pf)
    Front_right_Steer.SetAngle(pf)


    Besiege.Watch("SPEED",round(v1))
    Besiege.Watch("HRIGHT",round(Start_Block.Position.y))