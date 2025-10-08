New_list = [1, 2, 3, 4, 5]

def couplOff(New_list):
    total = 0

    # Outer loop → runs n times
    for num1 in New_list:
        # Inner loop → also runs n times for each outer iteration
        for num2 in New_list:
            print(f"{num1} : {num2}")   # executes n × n times
            total = total + 1           # executes n × n times

    return f"The total is : {total}"

print(couplOff(New_list))
