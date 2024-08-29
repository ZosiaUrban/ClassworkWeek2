

gender=input("if you are a female type a and if you are male type b")

hemlvl=int(input("what is your hemoglobin level?"))

if gender == "a":
    if hemlvl < 117:
        print(" low hemoglobin levels")
    elif hemlvl >  155:
        print(" high hemoglobin levels")
    elif hemlvl <= 155 and hemlvl >= 117:
        print("You have normal Hemoglobin levels")

elif gender== "b":
    if hemlvl >=167:
        print("high hemoglobin levels")

    elif hemlvl <= 167 and hemlvl >= 135:
     print("You have normal Hemoglobin levels")


    else:
        print("low hemoglobin levels")




