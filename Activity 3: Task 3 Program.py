import math
print("Select operation.")
print("1.Sine")
print("2.Cosine")
print("3.Tangent")
print("4.Exit")

while True:
    choice = input("Enter choice:")
    if choice in ['1', '2', '3']:
        angle = int(input("Enter the Angle in degrees: "))
        rad = math.radians(angle)
        if choice == '1':
            print("Sine {} ={}".format(angle, math.sin(rad)))
        elif choice == '2':
            print("Cosine {}={}".format(angle, math.cos(rad)))
        elif choice == '3':
            print("Tangent {}={}".format(angle, math.tan(rad)))
    elif choice == '4':
        print("Thank you")
        break
    else:
        print("Please enter a valid option.")
