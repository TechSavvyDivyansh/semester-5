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
    pass


# transmitted_message_character_count=character_count()
transmitted_message_byte_stuffing=byte_stuffing()

# print(data_transmitted)
print(transmitted_message_byte_stuffing)