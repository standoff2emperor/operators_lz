
b=int(input("введите пожалуйста значение первого элемента"))
q=int(input("введите, пожалуйста, значение множителя прогрессии"))
n=int(input("введите, пожалуйста, номер последнего элемента"))
if -10000<=b and b<= 10000: 
    if 1 < q and q <= 50: 
        if 2 <= n and n <= 100: 
            print ((b*(q**n-1))//(q-1))
        else: print ("ошибка")
    elif q == 1:
        if 2 <= n and n <= 100: 
            print(b*n)
        else: print ("ошибка")
    else: print ("ошибка")
else: print ("ошибка")