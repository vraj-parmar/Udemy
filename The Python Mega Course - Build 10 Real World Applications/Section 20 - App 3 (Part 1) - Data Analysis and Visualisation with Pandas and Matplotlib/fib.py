def fib():
    x = 1
    seq = []
    for n in range(0, 10):
        if n == 0 or n == 1:
            seq.append(1)
        else:
            seq.append(seq[n-1] + seq[n-2])
    
    return(seq)
            
print(fib())