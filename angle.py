from numberes import *
def angle():
    gyro.resert_angle(gyro_reset)
    while gyro.angle() != gyro_angle:
        left_motor(speed)
        right_motor(-speed)
    left_motor.stop()
    right_motor.stop()   

