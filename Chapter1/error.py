

n = input("Enter a number: ")

try:
    n = int(n)
    if n % 2 == 0:
        print(f"you have entered number, {n}")
except Exception as e:
    print(f"you have entered wrong number, {n}", e)

print("thank you for using our program")

