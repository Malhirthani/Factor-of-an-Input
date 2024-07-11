input_number = int(input("Please Enter Number"))

factor_set = []

n = 0
for n in range (1, input_number+1) :

    if input_number%n == 0:
        
        factor_set.append(n)
    
    n += 1
   
print(f"Factors for {input_number} are {factor_set}")
