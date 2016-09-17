import datetime

Start_Block=Besiege.GetBlock("4c402dac-56a6-42e6-9c54-008b1db0a649")
Back_Left_Wheel=Besiege.GetBlock("268a5cde-7b9a-4ce1-aa16-9ffd6c7da157")
Back_Right_Wheel=Besiege.GetBlock("198f7ade-2b4a-447d-bab7-3d29a1ff8dfd")
Front_Left_Wheel=Besiege.GetBlock("b964e802-c948-4868-8a59-905448881834")
Front_Right_Wheel=Besiege.GetBlock("b970735f-edd4-447b-9bfa-2a89abd518a0")
time1=datetime.datetime.now()
time2=datetime.datetime.now()
t=0
a=0
def FixedUpdate():
	global t
	global a
	global time1
	global time2
	v3=Start_Block.Velocity
	v=v1=(v3.x**2+v3.y**2+v3.z**2)**0.5
	time2=datetime.datetime.now()
	Besiege.Watch("Speed",round(v*3.6,2))


	if Input.GetKey(KeyCode.L):
		time1=datetime.datetime.now()
		t=1
	

	if t and v1*3.6 >=100 and a==0:
		Besiege.Watch("Time",time2-time1)
		a=1


	c=v1/10+2
	if c>=3:
    		c=3
	Front_Left_Wheel.SetSliderValue("SPEED",c)
	Front_Right_Wheel.SetSliderValue("SPEED",c)
	Back_Left_Wheel.SetSliderValue("SPEED",c)
	Back_Right_Wheel.SetSliderValue("SPEED",c)