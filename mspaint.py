import RPi.GPIO as GPIO
import time

ledPin = 10
buttonPin = 8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(ledPin, GPIO.LOW)

print("Here we go! Press CTRL+C to exit")
try:
  while 1:
    if GPIO.input(buttonPin):
      GPIO.output(ledPin, GPIO.LOW)
      print(GPIO.input(buttonPin))
    else:
      GPIO.output(ledPin, GPIO.HIGH)
      print(GPIO.input(buttonPin))
except KeyboardInterrupt:
  GPIO.cleanup()
