print("Insert the start")
init = raw_input()
print("Insert the limit")
limit = raw_input()

for i in range(int(init), int(limit) + 1):
    if pow(2, i - 1) % i == 1:
        print(i);

