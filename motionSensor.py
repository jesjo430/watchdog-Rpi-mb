from gpiozero import MotionSensor
from time import sleep
from datetime import timedelta, datetime
from mbRequest import send

MOTION_SENSOR_PORT = 4
TIMEOUT = timedelta(minutes=5)
HAS_MOTION = False
last_visit = datetime.today()

msens = MotionSensor(MOTION_SENSOR_PORT)
#msens.when_motion() = motion()
#msens.when_no_motion() = no_motion()

def when_motion():
    last_visit = datetime.today()
    if not HAS_MOTION:
        HAS_MOTION = True
        send("Kontoret", True)

def when_no_motion():
    if last_visit + TIMEOUT < timedelta.today():
        HAS_MOTION = False
        send("Kontoret", False)