

compressedData = "0100000000001000000000010100111000000000010000000000100000000001000000"

jump = 1
last = 0
r = [""]
func = lambda:compressedData[last*10:jump*10]
while func() != '':
    
    print([func()[i:i+10] for i in range(0, len(func()), 10)])
    num = func().count('1')
    last = jump
    jump += num