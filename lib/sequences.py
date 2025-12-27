#!/usr/bin/env python3

#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    
    # Start with the first two numbers
    fib_sequence = [0, 1]
    
    # Generate the rest of the sequence
    while len(fib_sequence) < length:
        # Add the sum of the last two numbers
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    
    print(fib_sequence)