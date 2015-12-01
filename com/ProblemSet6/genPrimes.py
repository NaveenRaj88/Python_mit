__author__ = 'anandran'

def genPrimes():
    nextPrime = 2
    while True:
        yield nextPrime
        while True:
            nextPrime+=1
            isPrime=True
            for i in range(2,nextPrime):
                if nextPrime%i==0:
                    isPrime=False
                    break
            if(isPrime):
                break

        # while isPrime:
        #     nextPrime +=1
        #     for i in range(2,nextPrime):
        #         if nextPrime%i ==0:
        #             break

p=genPrimes()
for i in range(10):
    print p.next()

# print p.next()
#
# print p.next()

