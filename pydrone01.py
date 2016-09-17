#Block ID
Start_Block=Besiege.GetBlock("8985fac4-d16a-43ce-882a-8f886ef4fbf8")
front_left_spinning=Besiege.GetBlock("146d674c-4fda-4100-83da-5ea5fe8ba41a")
front_right_spinning=Besiege.GetBlock("5c8bc29d-07a1-44a8-bb53-e220ad757b6c")
rear_left_spinning=Besiege.GetBlock("68cff0b3-d7bf-4c98-b9c8-2cd22fa47d02")
rear_right_spinning=Besiege.GetBlock("9e350d77-f9a8-4752-946e-dd51b2dc51cc")
wheel1=Besiege.GetBlock("f339c681-a7e8-414b-b360-d9d86e3578c8")
wheel2=Besiege.GetBlock("5ec5dd1b-577e-472c-81c7-4c93d2c93d95")
wheel3=Besiege.GetBlock("e7cfaf7a-598d-43f6-95ce-188919c2079d")
wheel4=Besiege.GetBlock("692fd7ba-1deb-4865-b62a-3bbf7c522795")
wheel5=Besiege.GetBlock("37b84a24-9d50-4981-a091-6c6eca693da4")
front_spinning=Besiege.GetBlock("fa0bcc18-4ef7-4998-8eb2-1ae17fe1ca70")
rear_spinning=Besiege.GetBlock("497ed3f5-76d9-41ad-9b51-5507f7dac909")
left_spinning=Besiege.GetBlock("24fd1f07-f3d4-445c-bf93-ac11dad60116")
right_spinning=Besiege.GetBlock("3d65f05f-859f-45a1-b630-dc27ef6850fc")



#Last
position=Start_Block.Position
rotation=Start_Block.EulerAngles
last_altitude=position.y
last_x=position.x
last_y=position.z
last_pitch=rotation.x
last_roll=rotation.z

#Target parameters
target_altitude=6
target_x=position.x
target_y=position.z
target_yaw=0

altitude_p_error=0
altitude_i_error=0
altitude_d_error=0

x_p_error=0
x_i_error=0
x_d_error=0

y_p_error=0
y_i_error=0
y_d_error=0

pitch_p_error=0
pitch_i_error=0
pitch_d_error=0

roll_p_error=0
roll_i_error=0
roll_d_error=0

yaw_p_error=0
yaw_i_error=0
yaw_d_error=0



#Hover speed
HOVER_SPEED=1.12


#LOOP
def FixedUpdate():
    global target_altitude
    global target_x
    global target_y
    global target_yaw
    global rotation
    global last_altitude
    global last_x
    global last_y
    global last_pitch
    global last_roll
    global altitude_d_error
    global altitude_i_error
    global altitude_p_error
    global x_p_error
    global x_i_error
    global x_d_error
    global y_p_error
    global y_i_error
    global y_d_error
    global pitch_d_error
    global pitch_i_error
    global pitch_p_error
    global roll_d_error
    global roll_i_error
    global roll_p_error
    global yaw_d_error
    global yaw_i_error
    global yaw_p_error
    global HOVER_SPEED



    target_pitch=0
    if Input.GetKey(KeyCode.UpArrow):
        target_pitch=15
    if Input.GetKey(KeyCode.DownArrow):
        target_pitch=-15
    

    target_roll=0
    if Input.GetKey(KeyCode.LeftArrow):
        target_roll=15
    if Input.GetKey(KeyCode.RightArrow):
        target_roll=-15


    if Input.GetKey(KeyCode.I):
        target_altitude=target_altitude+20*Time.fixedDeltaTime
    if Input.GetKey(KeyCode.K):
        target_altitude=target_altitude-20*Time.fixedDeltaTime


    if Input.GetKey(KeyCode.Keypad6):
        x_v=5
    if Input.GetKey(KeyCode.Keypad4):
        x_v=-5

    if Input.GetKey(KeyCode.Keypad8):
        y_v=5
    if Input.GetKey(KeyCode.Keypad5):
        y_v=-5



    #machine's parameters
    position=Start_Block.Position
    rotation=Start_Block.EulerAngles

    #Altitude
    machine_altitude=position.y
    vertical_velocity=(machine_altitude-last_altitude)/Time.fixedDeltaTime

    #X
    machine_x=position.x
    x_velocity=(machine_x-last_x)/Time.fixedDeltaTime

    #Y
    machine_y=position.y
    y_velocity=(machine_y-last_y)/Time.fixedDeltaTime

    #Pitch
    machine_pitch=rotation.x
    pitch_velocity=Mathf.DeltaAngle(machine_pitch,last_pitch)/Time.fixedDeltaTime

    #Roll
    machine_roll=rotation.z
    roll_velocity=Mathf.DeltaAngle(machine_roll,last_roll)/Time.fixedDeltaTime

    #Yaw
    machine_yaw=rotation.y
    yaw_velocity=Mathf.DeltaAngle(machine_yaw,target_yaw)/Time.fixedDeltaTime

    #Last
    last_altitude=machine_altitude
    last_x=machine_x
    last_y=machine_y
    last_pitch=machine_pitch
    last_roll=machine_roll

    #Altitude error
    altitude_p_error=target_altitude-machine_altitude
    altitude_i_error=altitude_i_error+altitude_p_error*Time.fixedDeltaTime
    altitude_d_error=vertical_velocity

    #Altitude gain
    altitude_p_gain=4.5
    altitude_i_gain=0.5
    altitude_d_gain=0

    #Altitude output
    altitude_adjustment=(   altitude_p_error*altitude_p_gain+
                            altitude_i_error*altitude_i_gain+
                            altitude_d_error*altitude_d_gain)/20
    
    #X error
    x_p_error=target_x-machine_x
    x_i_error=x_i_error+x_p_error*Time.fixedDeltaTime
    x_d_error=x_velocity

    #X gain
    x_p_gain=5
    x_i_gain=0
    x_d_gain=0

    #X output
    x_adjustment=(  x_p_error*x_p_gain+
                    x_i_error*x_i_gain+
                    x_d_error*x_d_gain)/20
    
    #Y error
    y_p_error=target_y-machine_y
    y_i_error=y_i_error+y_p_error*Time.fixedDeltaTime
    y_d_error=y_velocity

    #Y gain
    y_p_gain=2
    y_i_gain=0
    y_d_gain=0

    #Y output
    y_adjustment=(  y_p_error*y_p_gain+
                    y_i_error*y_i_gain+
                    y_d_error*y_d_gain)/20
    
    #Pitch error
    pitch_p_error=Mathf.DeltaAngle(machine_pitch,target_pitch)
    pitch_i_error=pitch_i_error+pitch_p_error*Time.fixedDeltaTime
    pitch_d_error=pitch_velocity

    #Pitch gain
    pitch_p_gain=1
    pitch_i_gain=0.1
    pitch_d_gain=0.5

    #Pitch output
    pitch_adjustment=(  pitch_p_error*pitch_p_gain+
                        pitch_i_error*pitch_i_gain+
                        pitch_d_error*pitch_d_gain)/20

    #Roll error
    roll_p_error=Mathf.DeltaAngle(machine_roll,target_roll)
    roll_i_error=roll_i_error+roll_p_error*Time.fixedDeltaTime
    roll_d_error=roll_velocity

    #Roll gain
    roll_p_gain=1
    roll_i_gain=0.1
    roll_d_gain=0.5

    #Roll output
    roll_adjustment=(   roll_p_error*roll_p_gain+
                        roll_i_error*roll_i_gain+
                        roll_d_error*roll_i_gain)/20
    
    #Yaw error
    yaw_p_error=Mathf.DeltaAngle(machine_yaw,target_yaw)
    yaw_i_error=yaw_i_error+yaw_p_error*Time.fixedDeltaTime
    yaw_d_error=yaw_velocity

    #Yaw gain
    yaw_p_gain=1
    yaw_i_gain=0
    yaw_d_gain=0

    #Yaw output
    yaw_adjustment=(    yaw_p_error*yaw_p_gain+
                        yaw_i_error*yaw_i_gain+
                        yaw_d_error*yaw_d_gain)/20
    


    front_left_speed=HOVER_SPEED+HOVER_SPEED*(altitude_adjustment-pitch_adjustment-roll_adjustment)
    front_right_speed=HOVER_SPEED+HOVER_SPEED*(altitude_adjustment-pitch_adjustment+roll_adjustment)
    rear_left_speed=HOVER_SPEED+HOVER_SPEED*(altitude_adjustment+pitch_adjustment-roll_adjustment)
    rear_right_speed=HOVER_SPEED+HOVER_SPEED*(altitude_adjustment+pitch_adjustment+roll_adjustment)
    wheel1_speed=-0.5*yaw_adjustment
    wheel2_speed=-0.5*yaw_adjustment
    wheel3_speed=-0.5*yaw_adjustment
    wheel4_speed=-0.5*yaw_adjustment
    wheel5_speed=-0.5*yaw_adjustment
    front_spinning_speed=2*HOVER_SPEED*y_adjustment
    rear_spinning_speed=2*HOVER_SPEED*y_adjustment
    right_spinning_speed=2*HOVER_SPEED*x_adjustment
    left_spinning_speed=2*HOVER_SPEED*x_adjustment
    front_left_spinning.SetSliderValue("SPEED",front_left_speed)
    front_right_spinning.SetSliderValue("SPEED",front_right_speed)
    rear_left_spinning.SetSliderValue("SPEED",rear_left_speed)
    rear_right_spinning.SetSliderValue("SPEED",rear_right_speed)
    wheel1.SetSliderValue("SPEED",wheel1_speed)
    wheel2.SetSliderValue("SPEED",wheel2_speed)
    wheel3.SetSliderValue("SPEED",wheel3_speed)
    wheel4.SetSliderValue("SPEED",wheel4_speed)
    wheel5.SetSliderValue("SPEED",wheel5_speed)
    if not (Input.GetKey(KeyCode.Keypad6) or Input.GetKey(KeyCode.Keypad4)):
        x_v=-10*x_velocity
        y_v=-10*y_velocity



    left_spinning.SetSliderValue("FLYING SPEED",x_v)
    right_spinning.SetSliderValue("FLYING SPEED",x_v)
    front_spinning.SetSliderValue("FLYING SPEED",y_v)
    rear_spinning.SetSliderValue("FLYING SPEED",y_v)
    
    
    Besiege.Watch("target_altitude",target_altitude)
    Besiege.Watch("machine_altitude",machine_altitude)
    Besiege.Watch("x_velocity",round(x_velocity,3))
    Besiege.Watch("y_velocity",round(y_velocity,3))
    Besiege.Watch("x_v",round(x_v,3))
    Besiege.Watch("y_v",round(y_v,3))