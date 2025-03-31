def is_even(n):
    if n % 2 == 0: 
        return True
    else: 
        return False

num = int(input("Enter an integer: "))  
if is_even(num): 
    print(f"{num} is even")   
else: 
    print(f"{num} is odd")
