sum = 0
for i in range (1, 100):
    
    digit_num1 = i%10
    
    digit_num2 = i//10
    
    sum = digit_num1 + digit_num2
    
    square_of_sum = sum**2
    
    if (i == square_of_sum):
        print(i)