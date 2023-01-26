#initially we take the starting sum to be 0
sum = 0

#this is to check the range from 1 to 1000
for i in range(1000):
    #this step verifies if the number is divisible by 3 or 5
    if(i % 3 == 0 or i % 5 == 0):
        #if number is divisible by 3 or 5, then it will add the number to the current value of sum
        sum = sum + i

print(sum)