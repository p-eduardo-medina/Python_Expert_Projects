# A binary clock displays the time of day in binary format.
# Modern binary clocks have six columns of lights; 
# two for each of the hours, minutes and seconds. 
# The photo below shows a binary clock displaying the time "12:15:45":

def binary_clock(num):
    num2bin = [ list(bin(int(nu))[2:])[::-1] for nu in list(num.replace(":","")) ]
    indexrows = [[],[],[0],[0,2,4]]
    matr = [[' ']*6 for _ in range(4)]
    for i in range(6):
        for j in range(4):
            if i not in indexrows[j]:
                if j >= len(num2bin[i]): matr[j][i] = '0'    
                else: matr[j][i] = num2bin[i][j]
    return [ ''.join(row) for row in matr[::-1]]

    
  
print(binary_clock("10:37:49") == [
  " 0 0 1",
  " 00110",
  "001100",
  "101101"
]      )
print(binary_clock("07:24:16"), [' 0 0 0', ' 10101', '011001', '010010'])
print(binary_clock("13:48:18"), [' 0 1 1', ' 01000', '010000', '110010'])
print(binary_clock("18:48:15"), [' 1 1 0', ' 01001', '000000', '100011'])
print(binary_clock("07:24:16") == [' 0 0 0', ' 10101', '011001', '010010'])
print(binary_clock("13:48:18") == [' 0 1 1', ' 01000', '010000', '110010'])
print(binary_clock("18:48:15") == [' 1 1 0', ' 01001', '000000', '100011'])
print(binary_clock("11:47:55") == [' 0 0 0', ' 01111', '000100', '110111'])
print(binary_clock("05:46:39") == [' 0 0 1', ' 11100', '000110', '010011'])
print(binary_clock("20:35:19") == [' 0 0 1', ' 00100', '101000', '001111'])
print(binary_clock("10:51:40") == [' 0 0 0', ' 01010', '000000', '101100'])
print(binary_clock("10:16:17") == [' 0 0 0', ' 00101', '000101', '101011'])
print(binary_clock("08:17:26") == [' 1 0 0', ' 00101', '000111', '001100'])
print(binary_clock("17:48:59") == [' 0 1 1', ' 11010', '010000', '110011'])
print(binary_clock("20:04:33") == [' 0 0 0', ' 00100', '100011', '000011'])
print(binary_clock("01:35:39") == [' 0 0 1', ' 00100', '001010', '011111'])
print(binary_clock("13:23:39") == [' 0 0 1', ' 00000', '011110', '110111'])
print(binary_clock("01:56:09") == [' 0 0 1', ' 01100', '000100', '011001'])
print(binary_clock("10:50:22") == [' 0 0 0', ' 01000', '000011', '101000'])
print(binary_clock("07:41:09") == [' 0 0 1', ' 11000', '010000', '010101'])
print(binary_clock("10:20:42") == [' 0 0 0', ' 00010', '001001', '100000'])
print(binary_clock("02:19:30") == [' 0 1 0', ' 00000', '010010', '001110'])
print(binary_clock("13:41:41") == [' 0 0 0', ' 01010', '010000', '110101'])
print(binary_clock("03:17:28") == [' 0 0 1', ' 00100', '010110', '011100'])