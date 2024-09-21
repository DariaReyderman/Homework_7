good_result: int = 0
sum_of_good_results: int = 0
world_record: float = 6.23
current_champion: str = "Armand Duplantis"
new_champion: str = None
new_record: float = None
max_height: float = 5.80
min_height: float = 6.23

for i in range(7):
    height: float = float(input("Enter a height of your jump: "))
    if height < 5.80:
        print("Try harder next time...")
        continue
    else:
        if height >= 5.80:
            good_result += 1
        if height > world_record:
            print("CONGRATULATIONS! You're a new world champion!!!")
            new_champion: str = input("Enter the name of a new champion: ")
            if new_record is None or height > new_record:
                new_record = height
            if new_champion is None or new_champion != current_champion:
                current_champion = new_champion
        if height > max_height:
            max_height = height
        if height < min_height:
            min_height = height

        sum_of_good_results += height

avg: float = sum_of_good_results / good_result
print(f"Total quantity of good results is {good_result} and their average is {avg:.2f}")
print(f"The highest jump is {max_height}")
print(f"New world record is {new_record} made by {new_champion}")
