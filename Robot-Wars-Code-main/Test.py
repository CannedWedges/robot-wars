from machine import Pin,ADC,PWM
from time import sleep
import utime

fan = Pin(16, Pin.OUT)  
motionSensorOne	= Pin(18, Pin.IN)
motionSensorTwo = Pin(20,Pin.IN)
distanceMeasure = Pin(16,Pin.IN)


servoOne = PWM(Pin(27))
servoTwo = PWM(Pin(28))
servoValOne = 0
servoValTwo = 0


def moveServo(servo, angle):
    servo.duty_u16(int(angle / 360 * 65535))


try:
    while True:
        
        print(str(distanceMeasure.value()) + "Distance Measure")
        utime.sleep_ms(1)
        if motionSensorOne.value() == 1:
            while servoValOne < 360:
                servoValOne += 10
                print(str(servoValOne))
                utime.sleep_ms(10)
                #servoOne.duty_u16(servoValOne)
                moveServo(servoOne, servoValOne)
            while servoValOne > 0:
                servoValOne -= 5
                utime.sleep_ms(100)
                #servoOne.duty_u16(servoValOne)
                moveServo(servoOne, servoValOne)
                
                
    #     if motionSensorTwo.value() == 1:
    #         while servoValTwo < 65535:
    #             servoValTwo += 1000
    #             utime.sleep_ms(1)
    #             servoTwo.duty_u16(servoValTwo)
    #         
    #         while servoValTwo > 0: 
    #             servoValTwo -= 50
    #             utime.sleep_ms(1)
    #             servoTwo.duty_u16(servoValTwo)
except KeyboardInterrupt:
    miniFun = Pin(16, Pin.OUT)  
    miniPir = Pin(18, Pin.IN)  

    pwm_Servo=PWM(Pin(27))
    pwm_Servo.freq(500)
    Servo_Val = 0  
    miniFun.value(0)
    pwm_Servo.duty_u16(0)
