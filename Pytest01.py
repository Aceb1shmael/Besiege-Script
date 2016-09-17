Suspension=Besiege.GetBlock("b6ddba4b-c1e1-441a-a951-8ac6af106944")
ss=0.5
def Update():
    	global ss
	if Input.GetKey(KeyCode.Keypad1):
		ss=1
	if Input.GetKey(KeyCode.Keypad2):
		ss=2
	Suspension.SetSliderValue("SPRING",ss)