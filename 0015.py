Start_Block=Besiege.GetBlock("24373482-5a16-4dba-875a-5ab1dd2daa16")

Left_Wheel_1=Besiege.GetBlock("aff66dbb-ab01-41b0-a2dd-30f2f86f84bd")
Left_wheel_2=Besiege.GetBlock("5cae7542-b57f-44b2-82c8-663e1de1d087")
Left_Wheel_3=Besiege.GetBlock("fb2fbf11-50a7-42e2-b0f1-3558894b54ba")
Left_Wheel_4=Besiege.GetBlock("fd57e6ac-199d-403b-9ee1-9633951e88b9")
Left_Wheel_5=Besiege.GetBlock("79b0d834-b44d-4b5d-95a4-39d4ddfa30d1")
Left_Wheel_6=Besiege.GetBlock("f1e64994-2b7d-4905-9cc3-010ee83f6e6d")
Left_Wheel_7=Besiege.GetBlock("6e5bf04c-11ca-4398-8bc1-5aedfb994350")

Right_Wheel_1=Besiege.GetBlock("42de5645-ec08-4807-8995-748cdc8a4df9")
Right_Wheel_2=Besiege.GetBlock("fdf61b6c-41f8-4966-8436-44e7ae51d265")
Right_Wheel_3=Besiege.GetBlock("5770441b-ba6c-4b2e-afb8-e4315f47a11a")
Right_Wheel_4=Besiege.GetBlock("7005ab0b-640b-49b4-8723-a7faa377e292")
Right_Wheel_5=Besiege.GetBlock("fbd53f2e-9818-4891-bc5b-846e41aa3434")
Right_Wheel_6=Besiege.GetBlock("18327aa2-df19-49a4-87ad-b46301d0a429")
Right_Wheel_7=Besiege.GetBlock("d1f64404-2ea8-4013-9557-ddfd82f9f779")


def FixedUpdate():
    v3=Start_Block.Velocity
    v1=(v3.x**2+v3.y**2+v3.z**2)**0.5
    c=v1/7.0
    
    
    if c>6:
        c=6

    if Input.GetKey(KeyCode.DownArrow) and c>0:
        c=-c+1.8

    vl=c+2
    vr=c+2

    if Input.GetKey(KeyCode.LeftArrow):
        vl=vl-1.5
        vr=vr+1.5

    if Input.GetKey(KeyCode.RightArrow):
        vl=vl+1.5
        vr=vr-1.5

    if vr>5:
        vr=5
    if vl>5:
        vl=5


    Left_Wheel_1.SetSliderValue("SPEED",vl)
    Left_wheel_2.SetSliderValue("SPEED",vl*1.1)
    Left_Wheel_3.SetSliderValue("SPEED",vl*1.2)
    Left_Wheel_4.SetSliderValue("SPEED",vl*1.2)
    Left_Wheel_5.SetSliderValue("SPEED",vl*1.2)
    Left_Wheel_6.SetSliderValue("SPEED",vl*1.2)
    Left_Wheel_7.SetSliderValue("SPEED",vl)

    Right_Wheel_1.SetSliderValue("SPEED",vr)
    Right_Wheel_2.SetSliderValue("SPEED",vr*1.1)
    Right_Wheel_3.SetSliderValue("SPEED",vr*1.2)
    Right_Wheel_4.SetSliderValue("SPEED",vr*1.2)
    Right_Wheel_5.SetSliderValue("SPEED",vr*1.2)
    Right_Wheel_6.SetSliderValue("SPEED",vr*1.2)
    Right_Wheel_7.SetSliderValue("SPEED",vr)

    Besiege.Watch("SPEED",round(v1))
    Besiege.Watch("C",round(c))