
def fab(n):
    sequences = []
    a,b = 0,1

    while len(sequences) < n:
            sequences.append(a)
            a,b = b, a+b
    return sequences

user = float(input('Enter a Number : '))
fabi_ser = fab(user)

print(fabi_ser)


'''
def fibonacci(n):
    sequence = []
    a, b = 0, 1

    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b

    return sequence

fib_sequence = fibonacci(20)
print(fib_sequence)
'''