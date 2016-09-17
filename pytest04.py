Front_Left_Wheel=Besiege.GetBlock("3e18b6da-49a8-4dfd-bbeb-8cc31225b740")
Front_Right_Wheel=Besiege.GetBlock("d9cd90c7-5337-4eca-aabc-3359f94ecce1")
Back_Left_Wheel=Besiege.GetBlock("b1e9bf5a-65f5-4fd9-b391-51dd3bb45590")
Back_Right_Wheel=Besiege.GetBlock("23723274-b39e-4be0-9d5b-9cec9fe30c84")
Start_Block=Besiege.GetBlock("4feac78a-6e40-47c5-b84c-cc6290e5a98a")
Left_Hinge=Besiege.GetBlock("36fa501f-ee28-4661-b09c-21aa76cacd35")
Right_Hinge=Besiege.GetBlock("a7faa72e-92e0-4347-9a56-2d79f7f7d787")



svl=0
svr=0
vd=0.5
vc=0.2


def FixedUpdate():
    

    angle=0
    al=0
    ar=0
    v3=Start_Block.Velocity
    v1=v=((v3.x)**2+(v3.z)**2+(v3.y)**2)**0.5
    v=round(v)
    c=v/10+0.6
    if c<4:
        v=c
    else:
        v=4
    v_Back_Left=v+0.3
    v_Back_Right=v+0.3
    v_Front_Left=v+0.5
    v_Front_Right=v+0.5
    vd=v/3



    if Input.GetKey(KeyCode.LeftArrow):
        angle=-45
        ar=angle+15
        al=angle
        vd=vd*abs(Left_Hinge.GetAngle())/45
        v_Back_Left-=2*vd
        v_Front_Left-=vd
        v_Front_Right+=vd
    if Input.GetKey(KeyCode.RightArrow):
        angle=45
        al=angle-15
        ar=angle
        vd=vd*abs(Right_Hinge.GetAngle())/45
        v_Back_Right-=2*vd
        v_Front_Right-=vd
        v_Front_Left+=vd
	


    if Left_Hinge.GetAngle()<0:
        svl=1
        svr=1.5
    else:
        svl=1.5
        svr=1


    Left_Hinge.SetSliderValue("ROTATION SPEED",svl)
    Right_Hinge.SetSliderValue("ROTATION SPEED",svr)

    Besiege.Watch("Speed",round(v1*3.6))
    Back_Left_Wheel.SetSliderValue("SPEED",v_Back_Left)
    Back_Right_Wheel.SetSliderValue("SPEED",v_Back_Right)
    Front_Left_Wheel.SetSliderValue("SPEED",v_Front_Left)
    Front_Right_Wheel.SetSliderValue("SPEED",v_Front_Right)
    Left_Hinge.SetAngle(al)
    Right_Hinge.SetAngle(ar)