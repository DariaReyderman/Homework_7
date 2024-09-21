pos_num: int = 0
neg_num: int = 0
zero: int = 0
seven: int = 0
last_positive = None
last_negative = None

for _ in range(10):
    num: int = int(input("Enter a number: "))
    if num < -1000 or num > 1000:
        print("Illegal number, try again")
        continue
    if num == -9999:
        break
    else:
        if num > 0:
            pos_num += 1
            print(num)
            if num % 7 == 0:
                seven += 1
            if last_positive is None or pos_num != neg_num:
                last_positive = num
        elif num < 0:
            neg_num += 1
            print(num)
            if num % 7 == 0:
                seven += 1
            if last_negative is None or neg_num != pos_num:
                last_negative = num
        elif num == 0:
            zero += 1
            print(num)

print()
print(f"Total quantity of positive numbers: {pos_num}")
print(f"Total quantity of negative numbers: {neg_num}")
print(f"Total quantity of 'zero's': {zero}")
print(f"Total quantity of numbers divided by 7: {seven}")
print(f"The last entered positive number was {last_positive}")
print(f"The last entered negative number was {last_negative}")
