def countDigit(digit,count):
    if digit==0:
        # print(count)
        return count
    digit=digit//10
    count+=1
    y=countDigit(digit,count)
    return y
digit=int(input())
count=0
print(countDigit(digit,count))