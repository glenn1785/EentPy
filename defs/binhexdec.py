class dec:
    def __init__(self, mself):
        self.input = int(mself.input)

        mself.output1 = self.dec_to_bin()
        mself.output2 = self.dec_to_hex()

    def dec_to_bin(self):
        print("dec_to_bin")
        return bin(self.input)

    def dec_to_hex(self):
        print("dec_to_hex")
        return hex(self.input)


class Hex:
    def __init__(self, mself):
        self.input = str(mself.input)
        self.h = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.output = 0
        self.mself = mself


        self.mself.output1 = self.hex_to_dec()
        self.mself.output2 = self.hex_to_bin()

    def power(self, input2, power):
        print(f"power {power}")
        if power == 0:
            return input2
        else:
            return int(input2 * 16 ** power)

    def hex_to_dec(self):
        print("hex_to_dec")
        # uitfilteren 0x
        input = ""
        for place in range(2, len(self.input)):
            input = input + self.input[int(place)]

        # omdraaien caracters
        input2 = ""
        for place in range(int(len(input) - 1), -1, -1):
            input2 = input2 + input[place]

        print(input2)  # debugging

        if len(input2) > 32:
            self.output = "OUT OF RANGE, MAX DIGITS:32"
        else:

            for place in range(0, len(input2)):
                for number in range(0, 10):
                    if input2[place] == "a":
                        self.h[place] = self.power(10, place)
                        break

                    elif input2[place] == "b":
                        self.h[place] = self.power(11, place)
                        break

                    elif input2[place] == "c":
                        self.h[place] = self.power(12, place)
                        break

                    elif input2[place] == "d":
                        self.h[place] = self.power(13, place)
                        break

                    elif input2[place] == "e":
                        self.h[place] = self.power(14, place)
                        break

                    elif input2[place] == "f":
                        self.h[place] = self.power(15, place)
                        break

                    elif input2[place] == str(number):
                        self.h[place] = self.power(number, place)
                        break

                    self.output = "SYNTAX ERROR"
                    return self.output

            for i in range(0, len(input2)):
                self.output += self.h[i]

        return self.output


    def hex_to_bin(self):
        print("hex_to_bin")
        try:
            return bin(self.output)
        except TypeError:
            return ""

class Bin:
    def __init__(self, mself):
        self.mself = mself
        self.input = str(mself.input)
        self.output = 0
        mself.output1 = self.bin_to_dec()
        mself.output2 = self.bin_to_hex()


    def bin_to_dec(self):
        print("bin_to_dec")

        # uitfilteren 0b
        input = ""
        for place in range(2, len(self.input)):
            input = input + self.input[int(place)]

        # omdraaien caracters
        input2 = ""
        for place in range(int(len(input) - 1), -1, -1):
            input2 = input2 + input[place]

        print(input2)  # debugging

        for place in range(0, len(input2)):
            if input2[place] != 1 or input2[place] != 0:
                self.output += int(input2[int(place)]) * int(2 ** place)
            else:
                print("err")
                self.output = "SYNTAX ERROR, ONLY USE 1 AND 0"
                return self.output

        return self.output

    def bin_to_hex(self):
        return hex(int(self.output))
