height = float(input("your height"))
weight = float(input("your weight"))

sum = weight/height*height 
if sum < 18.4 :
    print(sum,"you are under weight ")
elif sum > 18.4 and sum < 24.9 :
    print(sum,"you are normal")
elif sum > 25 and   sum < 29.9 :
     print(sum,"you are over weight")  
     