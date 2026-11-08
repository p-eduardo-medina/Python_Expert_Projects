"""A courthouse has a backlog of several cases that need to be heard, and is trying to set up an efficient
schedule to clear this backlog. You will be given the following inputs:

A dictionary cases whose values are the number of court sessions each case needs to be concluded.
An integer max_daily_sessions which gives the maximum number of court sessions that can be held each day.
Crucially, it is not possible to have two sessions of the same case in the same day."""
import math
def legalbacklog(cases, max_daily_sessions):
    if not cases:
        return 0
    total_sessions = sum(cases.values())
    days_by_capacity = math.ceil(total_sessions/max_daily_sessions)
    return max(max(cases.values()), days_by_capacity)

print(legalbacklog({'A': 4, 'B': 3, 'C': 2}, 5) == 4)
print(legalbacklog({'A': 4, 'B': 3, 'C': 2}, 3) == 4)
print(legalbacklog({'A': 4, 'B': 3, 'C': 2}, 1) == 9)
print(legalbacklog({'A': 4, 'B': 3, 'C': 2}, 2) == 5)
print(legalbacklog({'A': 4, 'B': 4, 'C': 4, 'D': 4}, 2) == 8)
print(legalbacklog({'A': 20, 'B': 10, 'C': 10, 'D': 10}, 3) == 20)
print(legalbacklog({'A': 70, 'B': 60, 'C': 50, 'D': 15, 'E': 15, 'F': 10, 'G': 10, 'H': 10, 'I': 10}, 6) == 70)
