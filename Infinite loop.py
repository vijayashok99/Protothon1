a=[]
import time
while(1):
    try:
        a.append("1")
        time.sleep(0.1)
        print(a)
    except KeyboardInterrupt:
        break
