Front_Left_Wheel=Besiege.GetBlock("0145ab53-04a8-4c52-a5e8-8d0003dfd38e")
Front_Right_Wheel=Besiege.GetBlock("5b8d3460-4bc0-40f7-872b-5233840906b7")
Back_Left_Wheel=Besiege.GetBlock("66a11cd9-8f87-4cad-b50f-f005fb507f36")
Back_Right_Wheel=Besiege.GetBlock("55465d82-c516-445b-a82b-d90394e0dc0a")
Start_Block=Besiege.GetBlock("bd5da400-fba7-4b0d-979b-7defad9e0608")
Left_Hinge=Besiege.GetBlock("e3d36801-184f-43ff-a288-feb7084587e2")
Right_Hinge=Besiege.GetBlock("cc712d9f-8f61-4836-8ef8-427fb991d1fb")
Front_Left_Suspension=Besiege.GetBlock("c0751583-d9b6-4461-9923-31917055a014")
Front_Right_Suspension=Besiege.GetBlock("4e428b68-7a5c-47ef-ab5c-a8dcc0a5a4ee")
Back_Left_Suspension=Besiege.GetBlock("5ae77b09-07ce-47ef-b132-2dcf43c66da4")
Back_Right_Suspension=Besiege.GetBlock("0e61979b-830d-45f4-8a35-9b3139ae775f")
Flying_Spiral=Besiege.GetBlock("f176a242-2c7a-4193-9f4c-5fd198ee2b59")

Radar=Besiege.GetBlock("4fc1305e-62c3-44b8-8efd-0c94b6691113")
Rocket_1=Besiege.GetBlock("22565c0c-9ded-48ba-9926-e15293fdf261")
Rocket_2=Besiege.GetBlock("948457a7-1f94-452c-b0f7-d943e8b331c9")
Rocket_3=Besiege.GetBlock("c5aea007-2a1c-4e30-9073-646010abfd49")


v=0
v_Front_Left=0
v_Front_Right=0
v_Back_Left=0
v_Back_Right=0
svl=0
svr=0
vl=3
vd=1.5
tl="Road"
vfs=0
ss=3
dfi=170**0.5/10.5-1
dfo=317**0.5/10.5-1
dri=7/10.5-1
dro=14/10.5-1
hit=(0,0,0)
t=0
y=0
u=0

def L(block1,hit):
	x=block1.Position.x-hit.x
	y=block1.Position.y-hit.y
	z=block1.Position.z-hit.z
	return (x**2+y**2+z**2)**0.5


def FixedUpdate():
	global v
	global c
	global v_Front_Left
	global v_Front_Right
	global v_Back_Left
	global v_Back_Right
	global svl
	global svr
	global vl
	global vd
	global tl
	global vfs
	global ss
	global dfi
	global dfo
	global dri
	global dro
	global hit
	global t
	global y
	global u
	al=0
	ar=0
	v3=Start_Block.Velocity
	v=((v3.x)**2+(v3.z)**2+(v3.y)**2)**0.5
	v1=v
	c=(v-1.46825)/12.4237
	if c<vl:
		v=c
	else:
		v=vl
	v=v+vd
	v_Front_Left=v
	v_Front_Right=v
	v_Back_Left=v
	v_Back_Right=v

	if Input.GetKey(KeyCode.Keypad1):
    		vl=1
		vd=1.5
		tl="Climb"
		vfs=10
		ss=3
		dri=-0.5
		dro=0.5
		dfi=1
		dfo=1.5

	
	if Input.GetKey(KeyCode.Keypad2):
    		vl=2
		vd=1.5
		tl="OffRoad"
		vfs=1
		ss=0.5
		dfi=170**0.5/10.5-1
		dfo=317**0.5/10.5-1
		dri=7/10.5-1
		dro=14/10.5-1

	if Input.GetKey(KeyCode.Keypad3):
    		vl=3.5
		vd=1.5
		tl="Road"
		vfs=0
		ss=2
		dfi=170**0.5/10.5-1
		dfo=317**0.5/10.5-1
		dri=7/10.5-1
		dro=14/10.5-1
	
	
	if Input.GetKey(KeyCode.LeftArrow):
		ar=-30
		al=-45
	if Input.GetKey(KeyCode.RightArrow):
		al=30
		ar=45

	if Left_Hinge.GetAngle()<0 and Input.GetKey(KeyCode.LeftArrow):

		t=Left_Hinge.GetAngle()/(-45)
		svl=2
		svr=1.5
		v_Back_Right=(1+t*(dro))*v
		v_Back_Left=(1+t*(dri))*v
		v_Front_Left=(1+t*(dfi))*v
		v_Front_Right=(1+t*(dfo))*v
	elif Input.GetKey(KeyCode.RightArrow):
		svl=1.5
		svr=2
		t=Left_Hinge.GetAngle()/(30)
		v_Back_Left=(1+t*(dro))*v
		v_Back_Right=(1+t*(dri))*v
		v_Front_Right=(1+t*(dfi))*v
		v_Front_Left=(1+t*(dfo))*v


	
	Left_Hinge.SetSliderValue("ROTATION SPEED",svl)
	Right_Hinge.SetSliderValue("ROTATION SPEED",svr)
	Left_Hinge.SetAngle(al)
	Right_Hinge.SetAngle(ar)
	Back_Left_Wheel.SetSliderValue("SPEED",v_Back_Left)
	Back_Right_Wheel.SetSliderValue("SPEED",v_Back_Right)
	Front_Left_Wheel.SetSliderValue("SPEED",v_Front_Left)
	Front_Right_Wheel.SetSliderValue("SPEED",v_Front_Right)
	Flying_Spiral.SetSliderValue("FLYING SPEED",vfs)
	Front_Left_Suspension.SetSliderValue("SPRING",ss)
	Front_Right_Suspension.SetSliderValue("SPRING",ss)
	Back_Left_Suspension.SetSliderValue("SPRING",ss)
	Back_Right_Suspension.SetSliderValue("SPRING",ss)



	origin=Radar.Position+Radar.Forward
	direction=Radar.Forward
	try:
		hit=Besiege.GetRaycastHit(origin,direction)
	except Exception as e:
		print e
	if Input.GetKey(KeyCode.T):
    		t=1
	if Input.GetKey(KeyCode.Y):
    		y=1
	if Input.GetKey(KeyCode.U):
    		u=1


	if t and L(Rocket_1,hit)<5:
    		Rocket_1.SetSliderValue("FLIGHT DURATION",0)
	if u and L(Rocket_2,hit)<5:
    		Rocket_2.SetSliderValue("FLIGHT DURATION",0)
	if y and L(Rocket_3,hit)<5:
    		Rocket_3.SetSliderValue("FLIGHT DURATION",0)
			
	
	Besiege.Watch("Speed",round(v1*3.6))
	Besiege.Watch("Mode",tl)
	Besiege.Watch("Hit",hit)
	Besiege.Watch("LR1",L(Rocket_1,hit))
	Besiege.Watch("LR2",L(Rocket_2,hit))
	Besiege.Watch("LR3",L(Rocket_3,hit))