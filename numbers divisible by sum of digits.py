sum = 0
for n in range(1, 100):
    digit_num1 = n%10
    digit_num2 = n//10
    sum =digit_num1 + digit_num2 
    if n%sum == 0:
        print(n)