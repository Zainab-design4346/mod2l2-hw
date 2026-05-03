def myfunction(n):
    for i in range(0,n+1):
        print('First loop')

    j=1
    while(j<=n+1):
        print("Second loop ",j)
        j=j*2

    for i in range(0,100):
        print("Third loop")

print("Function above will take time :")
print(" 0(N) + 0(log N) + 0(1)")