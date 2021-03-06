#
# See the notes for the other physics sample
#


from pyfrc.physics import drivetrains


class PhysicsEngine(object):
    '''
       Simulates a 4-wheel mecanum robot using Tank Drive joystick control 
    '''
    
    def __init__(self, physics_controller):
        '''
            :param physics_controller: `pyfrc.physics.core.Physics` object
                                       to communicate simulation effects to
        '''
        
        self.physics_controller = physics_controller
        self.physics_controller.add_device_gyro_channel('navxmxp_i2c_1_angle')
        self.physics_controller.add_device_gyro_channel('navxmxp_spi_4_angle')
        self.physics_controller.add_analog_gyro_channel(1)
        
            
    def update_sim(self, hal_data, now, tm_diff):
        '''
            Called when the simulation parameters for the program need to be
            updated.
            
            :param now: The current time as a float
            :param tm_diff: The amount of time that has passed since the last
                            time that this function was called
        '''
        
        # Simulate the drivetrain
        rb_motor = hal_data['CAN'][1]['value']
        lb_motor = hal_data['CAN'][13]['value']
        rf_motor = hal_data['CAN'][17]['value']
        lf_motor = hal_data['CAN'][15]['value']
        
        speed, rotation = drivetrains.four_motor_drivetrain(
                lb_motor, rb_motor, lf_motor, rf_motor, speed=10)
        self.physics_controller.drive(speed, rotation, tm_diff)

