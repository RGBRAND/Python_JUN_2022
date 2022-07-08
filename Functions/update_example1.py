
def simple_interest(p:int, r:int, t:int):
    return (p*r*t) / 100

def compound_interest(p, r, t):
    return p * (1 + r / 100)**t

if __name__ == "__main__":
# simple use
    p = 10000
    r = 5
    t = 3
    si = simple_interest(p, r, t)
    ci = compound_interest(p, r, t)
    print(f'simple interest is {si}')
    print(f'compound interest is {ci}')

    # sample use 2
    p = float(input("Enter the principle: "))
    r = float(input("Enter the rate of interest: "))
    t = float(input("Enter the time: "))
    si = simple_interest(p, r, t)
    ci = compound_interest(p, r, t)
    print(f'simple Interest is {si}')
    print(f'Compoud Interest is {ci}')