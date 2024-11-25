def xor(a,b):
    c=[]
    for i,j in zip(a,b):
        if(i!=j):
            c.append('1')
        else:
            c.append('0')
    return c

def division(divisor,dividend):
    n=len(divisor)
    m=len(dividend)

    i=n-1
    current_target=dividend[0:n]
    quotient=[]


    #division loop
    while(i!=m):
        current_target_string=''.join(current_target[-n:])
        divisor_string=''.join(divisor)

        
        if divisor_string <= current_target_string:
            quotient.append('1')
            result=xor(divisor,current_target[-n:])
        else:
            quotient.append('0')
            result=xor(['0']*n,current_target[-n:])    

            
        i+=1                               # go to next digit of dividend

        if(i==m):                          # stop if i reached end of dividend ,m->length of dividend
            break

        # carry next digit down
        next_digit=dividend[i]                          
        current_target=result+list(str(next_digit))


    remainder=result
    return quotient,remainder 



def encode_message(data,divisor):
    n=len(divisor)-1

    temp_processed_data=data+n*[0]
    quotient,remainder=division(divisor,temp_processed_data)

    transmitted_message=data+remainder[-n:]
    return transmitted_message


def decode_message(received_data,divisor):
    n=len(divisor)
    quotient,remainder=division(divisor,received_data)
    decoding_result=int(''.join(remainder))
    if(decoding_result==0):
        print("You got the correct message 🥳!!!!")
    else:
        print("message has been manipulated 💀👽!!!!!")
        print(f"quotient:{quotient},remainder:{remainder}")


def crc():
    data=list(input("Enter data:"))
    divisor_sender=list(input("Enter divisor:").lstrip('0'))

    
    transmitted_message=encode_message(data,divisor_sender)
    print(f'transmitted message: {transmitted_message}')

    received_message=list(input("Enter the received message:"))
    divisor_receiver=list(input("Enter divisor:").lstrip('0'))
    decode_message(received_message,divisor_receiver)


crc()