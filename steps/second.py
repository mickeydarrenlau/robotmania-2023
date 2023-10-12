import time

class second:
        def __init__(self, motor1, motor2, sonar, speed, turn_speed, slow_speed):
            self.motor1 = motor1
            self.motor2 = motor2
            self.sonar = sonar
            self.speed = speed
            self.turn_speed = turn_speed
            self.slow_speed = slow_speed

        def run(self):
            motor1 = self.motor1
            motor2 = self.motor2
            sonar = self.sonar
            speed = self.speed
            turn_speed = self.turn_speed
            slow_speed = self.slow_speed
            
            motor2.throttle = turn_speed # turn left
            time.sleep(0.6)
            motor2.throttle = 0.0

            time.sleep(2)

            motor1.throttle = slow_speed # move forward
            motor2.throttle = slow_speed

            time.sleep(2)

            while sonar.distance > 15:
                time.sleep(0.1)
                pass

            motor1.throttle = 0.0 # stop
            motor2.throttle = 0.0

