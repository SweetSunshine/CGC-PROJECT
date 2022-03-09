print('''  __  __    __  ____  ____ ______     __  __ __ __  __  __  __  __ __ __  __  ____
 (( \ ||    || ||    ||    | || |    (( \ || || ||\ || (( \ ||  || || ||\ || ||   
  \\  \\ /\ // ||==  ||==    ||       \\  || || ||\\||  \\  ||==|| || ||\\|| ||== 
 \_))  \V/\V/  ||___ ||___   ||      \_)) \\_// || \|| \_)) ||  || || || \|| ||___ ''')
with open("website.log","r") as f:
    lines=f.readlines()
    with open("output.txt","w+") as nf:
        for a in lines:
            a=a.split(" ")
            nf.write(f"ip : {a[0]} \n date : {a[3]} \n method : {a[5]} \n path :{a[6]} \n path :{a[7]} ")