def armstrong(num):
    sum=0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num,"is an Armstrong number")
    else:
        print(num,"is not an Armstrong number")
        
def palindrome(num):
    n = num
    rev = 0
    while num != 0:
        rev = rev * 10
        rev = rev + int(num%10)
        num = int(num / 10)
    if n == rev:
        print(n,"is palindrome number")
    else:
        print(n,"is not a palin") 
# take input from the user 
num = int(input("Enter a number to chk it is armstrong or not: ")) 
armstrong(num) 
# take input from the user 
num = int(input("Enter a number to chk it is palindrome or not: ")) 
palindrome(num)
