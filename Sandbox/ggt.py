def Primfactor(a):
    primes = []
    while a > 1:
        for n in range(2, a+1):
            if a % n == 0:
                a = a / n;
                primes.append(n);
                break;
    return set(primes);

def ggt(*numbers):
    primes = [];

    for number in numbers:
        primes.append(Primfactor(number));

    ggt_primes = [];

    for n in range(len(primes)-1):
        if primes[n] & primes[n + 1]:
            for x in (primes[n] & primes[n + 1]):
                if not x in ggt_primes:
                    ggt_primes.append(x);

    try:
        return reduce(lambda x, y: x * y, ggt_primes);
    except:
        return [];

if __name__ == "__main__":
    print ggt(33, 22, 11);