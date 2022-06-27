print("Welcome Aliens")

try:
    print("Source Opened")
    # a = int(input("Enter 1st number : "))
    # b = int(input("Enter 2nd number : "))
    # result = a / b

    n = int(input("Enter a number : "))
    print(n)

except ZeroDivisionError as e:
    print("You can't divide a number by Zero -", e)

except ValueError as e:
    print("Invalid input-", e)

except Exception as e:
    print("Some Error Occurred -", e)

finally:
    print("Source Closed")
