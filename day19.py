def covert():
    user = input("enter conversion type")
    

    if user == "distance":
        print("available type km and mile")

        from_unit = input("from unit")
        to_unit = input("to unit")

        number = int(input("Enter a value"))

        if from_unit == "km" and to_unit == 'mile':
            value = number * 0.621371
            print(f"Converted from km to mile is {value}")
        elif from_unit == "mile" and to_unit == 'km':
            value1 = number * 1.60934
            print(f"Converted from mile to km is {value1}")
covert()