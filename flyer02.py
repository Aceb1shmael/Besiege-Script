Start_Block=Besiege.GetBlock("12fd8ba3-8d48-43db-9e3c-df13df9ae3f7")

def FixedUpdate():
    v3=Start_Block.Velocity
    v1=(v3.x**2+v3.y**2+v3.z**2)**0.5
    h=Start_Block.Position.y
    Besiege.Watch("Speed",round(v1*3.6))
    Besiege.Watch("Height",round(h,2))