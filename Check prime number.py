def add_aval(m):
    prime = True
    for i in range(2,int(m**0.5)+1):
        if m % i == 0:
            prime = False
            break
    return(prime)


prime_number_cuont=0
LastPrimeNum=0
for i in range(1,1001):
    if add_aval(i):
        prime_number_cuont = prime_number_cuont+1
        LastPrimeNum=i

print(" last prime num = ", LastPrimeNum)
print("prime num cun = ", prime_number_cuont)
print("\n \n")
print("say Hello in master branch")