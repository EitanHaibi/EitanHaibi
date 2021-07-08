def angle():

gyro.resert_angle(0)
while gyro.angle() != 60:
 left_motor(speed)
 right_motor(-speed)
left_motor.stop()
right_motor.stop()   

