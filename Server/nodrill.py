import time
from Led import *
from servo import *
from Ultrasonic import *
from Buzzer import *

class nodrill:
    def run(self):
        try:
            buzzer = Buzzer()
            ultrasonic = Ultrasonic()
            pwm = Servo()
            led=Led()

            pwm.setServoPwm('1', 120)
            time.sleep(3)
            while True:
                data = ultrasonic.get_distance()
                if data > 30:
                    for i in range(0, 200, 4):
                        data = ultrasonic.get_distance()
                        print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Distance: " + str(data) + "cm")
                        time.sleep(0.01)
                        if data > 30:
                            pwm.setServoPwm('0', i)
                            #time.sleep(0.01)
                        else:
                            break
                    for i in range(200, 0, -4):
                        data = ultrasonic.get_distance()
                        print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Distance: " + str(data) + "cm")
                        time.sleep(0.01)
                        if data > 30:
                            pwm.setServoPwm('0', i)
                            #time.sleep(0.01)
                        else:
                            break
                else:
                    print "\nHostile AC-130 Above"
                    buzzer.run('1')
                    led.ledIndex(0x01,255,0,0)      #buzzer on turn Red led
                    led.ledIndex(0x02,255,0,0)
                    led.ledIndex(0x04,255,0,0)
                    led.ledIndex(0x08,255,0,0)
                    led.ledIndex(0x10,255,0,0)
                    led.ledIndex(0x20,255,0,0)
                    led.ledIndex(0x40,255,0,0)
                    led.ledIndex(0x80,255,0,0)
                    time.sleep(1)                   #wait for three seconds
                    buzzer.run('0')
                    
                    time.sleep(1)                   #silence interval
                    
                    buzzer.run('1')
                    time.sleep(1)
                    buzzer.run('0')
                    
                    time.sleep(1)
                    buzzer.run('1')
                    
                    time.sleep(1)
                    buzzer.run('0')
                    
                    led.colorWipe(led.strip, Color(0,0,0))  #turn off all the light
                    print "\n\n\nFriendly AA tank deployed"
                    pwm.setServoPwm('0',90)
                    pwm.setServoPwm('1',90)
                    break
                
        except KeyboardInterrupt:
            led.colorWipe(led.strip, Color(0,0,0))  #turn off the light
            pwm.setServoPwm('0',90)
            pwm.setServoPwm('1',90)
            buzzer.run('0')
            
if __name__=='__main__':
    print ('Scanning surrounding area...')
    AA_nodrill = nodrill()
    AA_nodrill.run()
    

    
        