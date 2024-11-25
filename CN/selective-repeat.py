import time
import random

# Get the number of frames (packets) from the user and calculate window size
total_frames = int(input("Enter number of frames: "))
window_size = total_frames // 2

# Track which packets have been sent and acknowledged
ack = [False] * total_frames
sent = [False] * total_frames

ack_received = 0
frames_send = 0

# Main loop for sending packets until all have been acknowledged
while ack_received < total_frames:
    # Send packets within the current window
    for i in range(frames_send, min(frames_send + window_size, total_frames)):
        if not sent[i]:
            print(f"Sending packet: {i}")
            sent[i] = True
            time.sleep(1)

    # Simulate receiving ACKs or packet loss
    for i in range(frames_send, min(frames_send + window_size, total_frames)):
        if sent[i] and not ack[i]:
            if random.random() > 0.7:  # Simulate packet loss
                print(f"Packet lost: {i}")
                sent[i] = False
                time.sleep(1)
            else:
                print(f"Acknowledgment received: {i}")
                ack_received += 1
                ack[i] = True
                time.sleep(1)

    # Move the send window forward as ACKs are received
    while frames_send < total_frames and ack[frames_send]:
        frames_send += 1