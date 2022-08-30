t = int(input("Enter number of test cases \n"))
for i in range(t):
    no = int(input("Natural number \n"))
    mul_3, mul_5, mul_15 = 0, 0, 0
    mul_3, mul_5, mul_15 = (no-1)//3, (no-1)//5, (no-1)//15
    sum_mul_3 = (3*mul_3*(mul_3+1)//2) +(5*mul_5*(mul_5+1)//2)-15*mul_15*(mul_15+1)//2
    print(sum_mul_3)
