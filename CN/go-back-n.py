import time
import random

total_frames=int(input("Enter total number of frames:"))
window_size=total_frames//2

sent=0
ack=0

while ack<total_frames:
    for i in range(window_size):
        if sent<total_frames:
            print(f"Sending frames :{sent}")
            sent=sent+1
            time.sleep(1)

    for i in range(window_size):
        if ack<total_frames:
            if random.choice([True,False]):
                print(f"Acknowledge sent :{ack}")
                ack=ack+1
                time.sleep(1)
            else:
                print(f"Lost packet :{ack}")
                sent=ack
                break
        else:
            break