
import struct
import io
import binascii

#with open("0.000xv0.dat", "r") as file:
#    data = file.read()
    #newdata = struct.unpack("f", range(128))
    #print(newdata)

with open("0.000xv0.dat", 'rb') as f:
    lines = [x.strip() for x in f.readlines()]

for line in lines:
    tmp = line.strip().lower()
    if b'some-pattern' in tmp: continue


i = 0
number = "01234567890123456789012345678901"
test_number = "00000000000000000000000000000001"
testing = "00111110001000000000000000000000"
list_1 = ["00111110001000000000000000000000", "00000000000000000000000000000001"]

def convert(a):
    integerPart = 0
    e = 0
    decimalPart = 0
    mySum = 0
    length = len(a)
    sign = (-1)**int(a[0])
    for i in range(1,9):
        e = e + int(a[i])*(2**(8-i))
        integerPart = 2**(e-127)
    for i in range(9,32):
        mySum = mySum + int(a[i])*2**((-1)*(i-8))
        decimalPart = 1 + mySum
    total = sign*decimalPart*integerPart
    print(total)
        
for i in range(2):
    convert(list_1[i])

for line in data:
    strline = str(line)
    length = len(strline)
    list2 = []
    for i in range(6):
        list2.append(strline[i]+strline[i+1]+strline[i+2])
    print(list2)




