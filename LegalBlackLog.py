"""A courthouse has a backlog of several cases that need to be heard, and is trying to set up an efficient
schedule to clear this backlog. You will be given the following inputs:

A dictionary cases whose values are the number of court sessions each case needs to be concluded.
An integer max_daily_sessions which gives the maximum number of court sessions that can be held each day.
Crucially, it is not possible to have two sessions of the same case in the same day."""

def legalbacklog(cases, max_daily_sessions):
    listSchedule = 0
    while True:
        subListSchedule = []
        keysToDelete = []
        numberofSesions = sum(cases.values())
        if numberofSesions!=0:
            for key,values in cases.items():
                if key in subListSchedule: 
                    listSchedule+=1
                    subListSchedule = []
                if cases[key] > 0:
                    subListSchedule.append(key)
                    cases[key]-=1    
                    if cases[key] == 0: keysToDelete.append(key)      
                if len(subListSchedule)>=max_daily_sessions or  sum(cases.values())==0 or key==(list(cases.keys()))[-1]:
                    listSchedule+=1
                    break
            for key in keysToDelete:
                del cases[key]
        else:
            return listSchedule



import time
start = time.time()

print(legalbacklog({'A': 4, 'B': 3, 'C': 2}, 5) == 4)
print(legalbacklog({'A': 4, 'B': 3, 'C': 2}, 3) == 4)
print(legalbacklog({'A': 4, 'B': 3, 'C': 2}, 1) == 9)
print(legalbacklog({'A': 4, 'B': 3, 'C': 2}, 2) == 5)
print(legalbacklog({'A': 4, 'B': 4, 'C': 4, 'D': 4}, 2) == 8)
print(legalbacklog({'A': 20, 'B': 10, 'C': 10, 'D': 10}, 3) == 20)
print(legalbacklog({'A': 70, 'B': 60, 'C': 50, 'D': 15, 'E': 15, 'F': 10, 'G': 10, 'H': 10, 'I': 10}, 6) == 70)



print('{:.6f}s'.format(time.time()-start))