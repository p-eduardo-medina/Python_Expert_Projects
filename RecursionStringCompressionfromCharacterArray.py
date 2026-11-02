def compress(c):# A string as input  
    last_index = 0
    while last_index + 1 < len(c) and c[last_index + 1] == c[0]:last_index += 1
    num = c[0]+str(last_index+1) if last_index > 0 else c[0]
    if last_index == len(c) - 1: return num
    return num+compress(c[last_index+1:])
    
print(compress(["t", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "s", "s", "s", "h"])== "te14s3h")
print(compress(["a", "a", "b", "b", "c", "c", "c"])== "a2b2c3")
print(compress(["a"])== "a")
print(compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])== "ab12")
print(compress(["a", "a", "a", "b", "b", "a", "a"])== "a3b2a2")
