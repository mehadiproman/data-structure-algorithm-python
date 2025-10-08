New_list = [1, 2, 3, 4, 5]



def couplOff(New_list):
    total = 0

    for num1 in New_list:
        for num2 in New_list:
            print(f"{num1} : {num2}")
            total = total + 1

    return f"The total is : {total}" 

print(couplOff(New_list))