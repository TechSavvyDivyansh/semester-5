def crc():
    data=list(input("Enter the data:"))
    divisor=list(input("Enter the divisor:"))
    
    received_data_word=list(input("Enter the data word received:"))
    transmitted_data_word=''

    new_data_word=data+(len(divisor)-1)*[0]

    c=0
    n=len(new_data_word)
    templist=new_data_word[0:len(divisor)]
    while(n!=0):
        # print(string(templist))
        c+=len(divisor)
        n-=len(divisor)



    


crc()