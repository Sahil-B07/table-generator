"""        Tables        """


def tak_num():
    print("-------------------------------------")
    num = int(input("Enter a number to get it's table : "))
    print(f"\n***** Table of {num} *****")
    print("    ________________")
    # for iteration
    for i in range(1, 11):
        product = num*i
        if (num < 10):
            print(f"    |{num} x {i:>2} : {product:>2} |")
        elif (num < 100):
            print(f"    |{num} x {i:>2} : {product:>3} |")
        elif (num < 1000):
            print(f"    |{num} x {i:>2} : {product:>4} |")
        else:
            print(f"    |{num} x {i:>2} : {product:>5} |")


# Driver code
if __name__ == '__main__':
    tak_num()
    print("    ----------------")
    while True:
        choice = input("Press Y to continue and n to exit: ").lower()
        if (choice == 'y'):
            tak_num()
            print("    ----------------")
        elif (choice == 'n'):
            print("\n***** Thank you for using our application..! *****\n")
            break
        else:
            print("Invalid Input. Try Again..!")
