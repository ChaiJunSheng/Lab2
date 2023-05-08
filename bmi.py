def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi=weight/height**2
    print("BMI=" + str(bmi))
    if bmi <18.5:
        print("You are underweight bitch")
        return -1
    elif bmi >25.0:
        print("You are fat")
        return 1
    else:
        print("You are normal")
        return 0





calculate_bmi(weight=62, height=1.72)

