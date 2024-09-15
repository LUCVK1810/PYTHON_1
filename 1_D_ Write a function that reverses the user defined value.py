num = int(input("Enter the number: ")) 
Revr_num = 0 
def Recur_reverse(num):
    global Revr_num # We can use it out of the function
    if (num > 0):
        Reminder = num % 10
        Revr_num = (Revr_num * 10) + Reminder
        Recur_reverse(num // 10)
        return Revr_num 
Revr_num =Recur_reverse(num) 
print("n Reverse of entered number is = %d" %Revr_num)
