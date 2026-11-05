def ascending(txt):
  for i in range(1,int(len(txt)/2)+1):
    if len(txt)%i==0: 
       if [ int(txt[index:index+i])-int(txt[0:i]) for index in range(0, len(txt), i) ] == list(range(int(len(txt)/i))):return True
  return False

print(ascending("232425")  == True)
print(ascending("2324256") == False)
print(ascending("444445")  == True)