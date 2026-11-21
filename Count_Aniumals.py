"""
txt = "goatcode"

count_animals(txt) ➞ 2
First animal = "dog"
Remaining string = "atcoe",
Second animal = "cat".
count = 2 (correct)
If you got a "goat" first time
remaining string = "code",
no animal will be found during next time.
count = 1 (wrong)
# """

animals = ["dog", "cat", "bat", "cock", "cow", "pig", 
  "fox", "ant", "bird", "lion", "wolf", "deer", "bear", 
  "frog", "hen", "mole", "duck", "goat"]

def count_animals(txt):
	counts = []
	
	def f(t, c):
		for a in animals:
			s = t
			for x in a: 
				s = s.replace(x, "", 1)
			if len(s) + len(a) == len(t): 
				f(s, c + 1)
		counts.append(c)
		
	f(txt, 0)
	return max(counts)
    

print(count_animals("dogcat")==2)
print(count_animals("bcaatt")==2)
print(count_animals("dopig")==1)
print(count_animals("goatcode")==2)
print(count_animals("dogdogdogdogdog")==5)