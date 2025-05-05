def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height*height)
    print ("Your BMI is " + str(bmi))
    return bmi

def check_bmi(bmi_value):
    if (bmi_value > 25.0):
        print("you are over weight")
        print("1")
    if (bmi_value >= 18.5 and bmi_value <= 25.0):
        print("you are very healthy")
        print("0")
    if (bmi_value < 18.5):
        print("you are under weight")
        print("-1")

def main():
    h =float(input("Enter your height : "))
    w =float(input("Enter your weight : "))
    bmi_value = calculate_bmi(h, w)
    check_bmi(bmi_value)

if __name__ =="__main__":
    main()