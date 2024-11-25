def character_count():

    frame=int(input("Enter no. of frames:"))
    transmitted_message=''

    for i in range(0,frame):
        data=input(f"Enter string {i+1}:")
        char_count=str(len(data)+1)+data
        transmitted_message+=char_count

    return transmitted_message


def byte_stuffing():
    
    message=input("Enter the message:")
    start_flag=input("Enter start flag:")
    end_flag=input("Enter end flag:")
    escape=input("Enter the escape character:")
    transmitted_message=""

    for i in range(0,len(message)):
        if(message[i]==start_flag or message[i]==end_flag):
            transmitted_message+=escape+message[i]
        else:
            transmitted_message+=message[i]

    return start_flag+transmitted_message+end_flag



def bit_stuffing():
    data = list(input("Enter data: "))
    flag = input("enter start,end flag: ")
    c = 0
    i = 0

    while i < len(data):
        if data[i] == '1':  
            c += 1
        else:
            c = 0                           # Reset the counter if the current bit is not '1'

        if c == 6:  
            # If six consecutive '1's are found
            
            data.insert(i, '0')             # Insert '0' before the 6th '1'
            c = 0                           # Reset the counter after stuffing
            i += 1                          # Skip the inserted '0' to avoid infinite loop
        
        i += 1                              # Move to the next bit

    return flag+''.join(data)+flag                    # Join the list to form a string



# print("character count:")
# transmitted_message_character_count=character_count()
# print("transmitted message character count:"+transmitted_message_character_count)


# print("byte stuffing:")
# transmitted_message_byte_stuffing=byte_stuffing()
# print("transmitted message byte stuffing:"+transmitted_message_byte_stuffing)


print("bit stuffing:")
transmitted_message_bit_stuffing=bit_stuffing()
print("transmitted message bit stuffing:"+transmitted_message_bit_stuffing)


