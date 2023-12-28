def sum_of_div(n) :
    sum = 0
    for i in range(1, n//2+2) :
        if n%i == 0 :
            sum += i
    return sum
    

def sum_of_div2(n) :
    result = "1"
    if n == 1:
        return result
    else :
        for i in range(2, n//2+2) :
            if n%i == 0 :
                result+=" + "
                result+=str(i)
        return result


while True :
    n = int(input())
    if n== -1 : 
        break
    elif n == sum_of_div(n) :
        print("%d =" %n,sum_of_div2(n))
    else : 
        print("%d is NOT perfect." %n)