Start_Block=Besiege.GetBlock("e9bc3b89-1a72-440f-839b-24a1beb08184")

Front_Left_Wheel=Besiege.GetBlock("ac339e1b-4e25-4fda-a6e9-c3242ecea043")
Front_Right_Wheel=Besiege.GetBlock("b42783e9-0647-4663-997b-2ebdbfcc9714")
Rear_Left_Wheel=Besiege.GetBlock("1e0e8e21-5381-4015-982d-4f1836c4335e")
Rear_Right_Wheel=Besiege.GetBlock("0c696aa2-b9d9-4fa4-aca9-0621d16b50fc")

Left_Hinge=Besiege.GetBlock("312501b1-6d1b-4425-8b6e-365160106ee5")
Right_Hinge=Besiege.GetBlock("94e43b12-34c0-4c06-a483-3b66cb39d0d2")

def FixedUpdate():
    v3=Start_Block.Velocity
    v1=(v3.x**2+v3.y**2+v3.z**2)**0.5
    c=-0.00581728+0.0711999*v1+0.000212488*v1**2-3.84276*10**-6*v1**3+4.34906*10**-8*v1**4

    if c>4.5:
        c=4.5
    
    if Input.GetKey(KeyCode.DownArrow) and c>0:
        c=-c+3

    cd=2.5


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
        vrl=vrl
        vrr=vrr*0.631579
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
    Besiege.Watch("C",c)