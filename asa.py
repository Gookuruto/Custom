import binascii
from zlib import crc32

'''
x="01101010 10011101 01010010 10100110 00000100 10110111 00010110 01000001 01100001 00111111 01011100 01010111 11110000 01100100 01000010 10000111 01110101 10100101 00001100 10110100 11000010 11100110 10100110 11110101 11110110 01011111 11011001 11100000 11011000 01011100 01111100 00111101 01011010 01010100 01111100 00010111 00001011 00010100 00111100 00001011 10010111 10111011 10000111 10100101 01001110 01010100 00110001 11000000 11110111 01110001 11100011 10010101 10100100 11001101 10101011 11110001 10001011 00001010 01100011 01110001 10111001 10000100 11011011 11000110 00101110 10000100 11101110 10011101 00000011 11111111 01000100 00000010 10110011 10001010 10111001 10011011 10100001 00101001 00001111 11101000 01001000 11010110 11111011 00001011 11111110 10001000 00010100 00100101 10101000 11110001 00111101 01010011 11001100 11110000 01101110 01111001 01000011 10011101 00001000 10100110 10111010 11001010 00110001 00011100 11111001 10100100 00001101 00100110 10010001 00001001 01011100 11001000 10001000 10100010 11011000 10001000 01010111 10101110 00010001 01001001 01010100 00100001 11111000 01101110 11101011 10110000 11101110 01000010 00100000 01101110 10000100 01100000 10111110 00111111 01011110 00100011 10010101 10010010 00100110 11011010 10100001 11011010 01000111 01001000 01010100 01000010 00000011 00010110 00011101 00111110 00001001 11100111 11011110 01001001 01011001 00110000 11101011 01100000 01010111 01010001 "
x=x.replace(" ","")
x=int(x,2)
x='0x{:02x}'.format(x)
x=x.replace("0x","")
#print x
#print type(x)
g=132;
z=abs(crc32(str(g)))
y="0."+str(z)
y=float(y)
print(str(y)+" "+str(type(y)))

def zero_one_float(a):
    y = "0." + str(a)
    y = float(y)
    return y
'''

x = [1] * 150

print
len(x)
print
x
