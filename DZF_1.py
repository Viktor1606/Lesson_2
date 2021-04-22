def my_funct(a_1, a_2):
    try:
        sum_name = a_1 / a_2
    except ZeroDivisionError:
        print("Error")
        sum_name = 0
    print(f"Sub: {sum_name}")
my_funct(float(input("a_1: ")),float(input("a_2: ")))

