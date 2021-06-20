import
# not working
d = audiere.open_device()
t = d.create_tone(17000) # 17 KHz
t.play() # non-blocking call
import time
time.sleep(5)
t.stop()