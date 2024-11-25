import math

hamming_bit=9


def is_power_of_two_algebraic(n):
    log_result = math.log2(n)
    return log_result.is_integer()  # Check if log_result is a whole number

def get_parity_positions(posn):
    n = hamming_bit
    final_list = []
    i = posn  # Start with the first element
    
    while i <= n:
        # Add 'posn' elements starting from i
        for j in range(i, min(i + posn, n + 1)):  # Ensure we don't go out of bounds
            final_list.append(j)
        
        # Move i forward by posn + posn (to skip posn elements)
        i = i + posn + posn
    
    final_list=[i-1 for i in final_list]
    return final_list



def insert_data(data,result):
    for i in data:
        for j in range(0,hamming_bit):
            if not is_power_of_two_algebraic(j+1) and result[j]=='-':
                result[j]=i
                break  
    return result 


def insert_parity(parity_type,result):
    for i in range(hamming_bit):
        if(result[i]=="-"):
            posn_list=get_parity_positions(i+1)
            data_list=[result[p] for p in posn_list]
            parity_sum=sum(data_list[1:])
            
            result[i]=0 if (parity_sum+parity_type)%2==0 else 1
            #if we get odd sum in odd parity and even sum in even parity add 0 else 1
    return result


def encode(data,parity_type):
    # while encoding only data needs to be reversed as data is feed from D7 backwards
    result=['-']*hamming_bit
    data_processed = [int(d) for d in list(data)[::-1]]
    result=insert_data(data_processed,result)
    print(result[::-1])                                     #reverse just for display from D7 to P1
    insert_parity(parity_type,result)
    
    return result[::-1]                                     #reverse just for display from D7 to P1



def detect_error(data,parity_type):
    error_posn_list=[]         
    
    for i in range(hamming_bit):
        if(is_power_of_two_algebraic(i+1)):
            p_sum=sum(data[i] for i in get_parity_positions(i+1))
            
            p_value=0 if (p_sum+parity_type)%2==0 else 1        # return 0 if sum=even and type=even or sum=odd and type=odd else 1
            error_posn_list.append(p_value)
    
    error_posn_list=error_posn_list[::-1]                       # we want p4,p2 and p1 hence need to reverse
    error_posn_value=int(''.join(map(str, error_posn_list)), 2)
    
    return error_posn_value


def correct_error(processed_data,error_posn):
    processed_data[error_posn-1]=1-processed_data[error_posn-1]
    return processed_data[::-1]




def decode(value_to_be_checked,parity_type):

    processed_data=[int(d) for d in list(value_to_be_checked)[::-1]]          #p1 to D7 format

    error_posn=detect_error(processed_data,parity_type)
    if(error_posn==0):
        return "no error found"
    else:
        print(f"error found at D{error_posn}")
        corrected=correct_error(processed_data,error_posn)
        return f"corrected :{corrected}"




data=input("enter data:")                         #data entered D7 to P1
parity_type=int(input("enter 0 for even parity and 1 for odd parity:"))
encoded_data=encode(data,parity_type)
print(f"final encoded data: {encoded_data}")                  

value_to_be_checked=input("Enter data to be checked:")        # data entered from D7 to P1
result=decode(value_to_be_checked,parity_type)
print(result)



# note: data is always enter in D7 to P1 format . always convert to P1 to D7 format for simplicity ,perform all operations and return result back as D7 to P1 format