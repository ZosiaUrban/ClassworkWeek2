a= "female"
b="male"

print("if you are a female type a and if you are male type b")
gender=input()

hemlvl=int(input("what is your hemoglobin level?"))

if gender== a and 117 <= hemlvl <= 155:
    print("You have normal Hemoglobin levels")
elif gender== b and 135 <= hemlvl <= 167:
    print("You have normal Hemoglobin levels")
else:
 print("you dont have normal Hemoglobin levels")