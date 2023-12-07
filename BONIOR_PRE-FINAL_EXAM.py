def A_prime(num):
    #A function to check if a number is a prime
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def B_primes(start, end):
    #to generate a list of prime numbers in the given range
    primes = [num for num in range(start, end + 1) if A_prime(num)]
    return primes


# Main program
while True:
    start = int(input("Enter a number [start] (Note: if you enter 0, it will terminate the program):\n"))

    if start == 0:
        print("Program terminated.")
        break

    if start < 0:
        print("Enter a non-negative number.")
        continue

    while True:
        end = int(input("Enter a number [end]:\n"))
        if end > start:
            break
        print("Enter a number greater than", start)

    result_primes = B_primes(start, end)

    print(f"Prime numbers between {start} and {end} are:\n{', '.join(map(str, result_primes))}")
