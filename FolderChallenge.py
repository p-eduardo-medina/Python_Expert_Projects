def last_ancestor(folders, X, Y): 
    keys = list(folders.keys())
    keys = keys[::-1]
    subDict = {}
    for key in keys:
        subDict[key] = folders[key]
        
        
        
        
        
        
        
        if X in subList and Y in subList:
            return key
            
        

last_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "I", "K") #"D"
last_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "D", "I") # "D"

last_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "G", "G") # "G"