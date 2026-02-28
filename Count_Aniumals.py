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
    count = 0
    dictTxt = {}    
    for char in txt: dictTxt[char] = dictTxt.get(char, 0) + 1
    for animal in animals:
        dictAnimal = {}
        for char in animal: dictAnimal[char] = dictAnimal.get(char, 0) + 1
        while all(char in dictTxt and dictTxt[char] >= dictAnimal[char] for char in dictAnimal):
            count += 1
            for char in dictAnimal: dictTxt[char] -= dictAnimal[char]
    return count

print(count_animals("dogcat")==2)
print(count_animals("bcaatt")==2)
print(count_animals("dopig")==1)
print(count_animals("goatcode")==2)
print(count_animals("dogdogdogdogdog")==5)