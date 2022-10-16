



class number:
    def __init__(self, num = "0000000000"):
        self.numericRange = num

    def Set(self, number):
        try:
            numericRange = list(self.numericRange)
            numericRange[number] = '1'
            self.numericRange = ''.join(numericRange)
        except:
            print("you can't do this")
    
    def NumberOf1(self):
        return [num for num in range(10) if self.numericRange[num] == '1']


inp = "92389"

numbers = []
for n in inp:
    numbers.append(number())
    numbers[-1].Set(int(n))


print(numbers)