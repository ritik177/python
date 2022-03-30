def pattern (n):
    for row in range (n ):
        for col in range (n):
            if((row==0 and col!=0 and col!= n-1))or
            ((row == n-1 and col!=0 and col!= n-1 ))
            