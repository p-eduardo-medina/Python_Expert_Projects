def is_it_inside(folders, X, Y):
    def find_path(folders, current, target):
        if current not in folders.keys():return None
        if target in folders[current]:
            return 1
        else:
            for child in folders[current]:
                if child in folders.keys():  
                  if find_path(folders, child, target): 
                    return 1
    return find_path(folders, Y, X) is not None
    

print(is_it_inside({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "B",  "A")==True)

print(is_it_inside({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "B",  "D")==False)

print(is_it_inside({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "I",  "D")==True)

print(is_it_inside({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "A", "K")==False)

print(is_it_inside({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "D", "D")==True)