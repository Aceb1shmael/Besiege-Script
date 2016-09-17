Front_Left_Wheel=Besiege.GetBlock("e9193b84-fc54-467c-b786-3228d4dfeeae")
Front_Right_Wheel=Besiege.GetBlock("38253f87-f8c8-4a3f-a904-0f97350f7cfd")
Back_Left_Wheel=Besiege.GetBlock("5b3a7e2a-9cd1-4dd6-8280-bb92b3fb2007")
Back_Right_Wheel=Besiege.GetBlock("10f51fdc-0016-4cd7-bfbe-e1a44a8415f5")
Start_Block=Besiege.GetBlock("0d394b53-66ee-41bd-9220-5e899fec0b2d")



def FixedUpdate():


	v3=Start_Block.Velocity
	v1=v=((v3.x)**2+(v3.z)**2+(v3.y)**2)**0.5
	v=round(v)
	c=v/15+0.6
	if c<4:
		v=c
	else:
		v=4
	v_Back_Left=v
	v_Back_Right=v
	v_Front_Left=v
	v_Front_Right=v
	



	Back_Left_Wheel.SetSliderValue("SPEED",v_Back_Left)
	Back_Right_Wheel.SetSliderValue("SPEED",v_Back_Right)
	Front_Left_Wheel.SetSliderValue("SPEED",v_Front_Left)
	Front_Right_Wheel.SetSliderValue("SPEED",v_Front_Right)
	c=(c-0.6)*10
	Besiege.Watch("Speed",v1)