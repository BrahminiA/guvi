def is_prime(a):
    if a < 2:
        return False
    elif a!=2 and a % 2 == 0:
        return False
    else:
        return all (a % i for i in range(3, int(a**0.5)+1) )
num=int(input())
if is_prime(num)==True:
    print ("yes")
else:
    print ("no")
