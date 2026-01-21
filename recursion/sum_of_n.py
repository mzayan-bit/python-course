a=int(input("Enter a number: "))

def sum_of_n(a):
    if a==0 or a==1:
        return a
    else:
        return a+sum_of_n(a-1)
    
print(sum_of_n(a))