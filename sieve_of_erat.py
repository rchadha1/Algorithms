def createList(num: int):
    master = []
    for a in range(0, num+1): #num+1 due to python indexing 
        master.append(True)
    
    return master  #if num = 5, [True,True, True, True, True]

def sieve(num: int, master: []):
    counter = 0
    for n in range(2, len(master)): #start at 2 because 2 is the first prime number
        counter = n
        if master[n] == True: #if the number we're at hasnt already been checked 
            for b in range(counter, len(master)):
                counter+=n #increment counter by itself until we get to the end
                if (counter > num): #to make sure we dont go out of bounds
                    break
                master[counter] = False
    
    return master

def printPrimes(num: int, master: []):
    print("All of the primes before", num, "are:", end = " ")
    for c in range(2, len(master)): #ignore index 0,1 
        if master[c] == True:
            print(c, end = " ")
    


if __name__ == "__main__":
    x = int(input("Enter the ending number: "))
    masterList = createList(x)
    primeList = sieve(x, masterList)
    printPrimes(x, primeList)
