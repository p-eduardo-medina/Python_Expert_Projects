def last_ancestor(folders, X, Y):
  mini,result = len(folders),""
  for key in folders.keys():
    sL, count = [key], 0
    while True:
      if X in sL and Y in sL:break
      else:
        count+=1
        sL  = list(set( sL + [x for key2 in sL if key2 in folders.keys() for x in folders[key2]]))
        if count >= len(folders):break
    if count < mini:mini,result=count,key
  return result


print(last_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "B", "C") == "A")

print(last_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "I", "J") == "G")

print(last_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "I", "K") == "D")

print(last_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "D", "I") == "D")

print(last_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "G", "G") == "G")
