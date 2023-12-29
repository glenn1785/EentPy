def split1(inpuT, placeOpp):
    output = ""
    for i in range(0, placeOpp):
        output += str(inpuT[i])

    return output

def split2(inpuT, placeOpp):
    output = ""
    for i in range(int(placeOpp) + 1, len(inpuT)):
        output += str(inpuT[i])

    return output

def calculate(inpuT):
    calc = False
    output = 0
    opperators = ["*", "/", "-", "+"]
    for opp in range(0, len(opperators)):
        for place in range(0, len(str(inpuT))):

            if str(inpuT[place]) == opperators[opp]:
                calc = True

                split_1 = float(calculate(split1(inpuT, place)))
                split_2 = float(calculate(split2(inpuT, place)))
                print(f"split1 {split_1} split2 {split_2}")

                if opperators[opp] == "*":

                    output = float(split_1) * float(split_2)
                    print(f"calculate(*) place({place})")

                elif opperators[opp] == "/":

                    output = float(split_1) / float(split_2)
                    print(f"calculate(/) place({place})")

                elif opperators[opp] == "-":

                    output = float(split_1) - float(split_2)
                    print(f"calculate(-) place({place})")

                elif opperators[opp] == "+":

                    output = float(split_1) + float(split_2)
                    print(f"calculate(+) place({place})")

    if not calc:
        output = inpuT

    print(f"return {output}")
    return output
