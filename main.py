inp = int(input("Enter Number: "))
times_to_do = int(input("How many times would you like it to be multiplied?"))


for i in range(1, times_to_do):
    print(f"{inp} * {i} = {inp*i}")
