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


def count_animals(txt):
    animals = ["dog", "cat", "bat", "cock", "cow", "pig",
                "fox", "ant", "bird", "lion", "wolf", "deer", "bear",
                "frog", "hen", "mole", "duck", "goat"]
    count,result = 0,0
    dictTxt = {}    
    

print(count_animals("dogcat")==2)
print(count_animals("bcaatt")==2)
print(count_animals("dopig")==1)
print(count_animals("goatcode")==2)
print(count_animals("dogdogdogdogdog")==5)