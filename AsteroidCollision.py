""" You are given a list asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign
represents its direction (positive meaning right, negative meaning left). 
Each asteroid moves at the same speed. Find out the state of the asteroids 
after all collisions. If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. Two asteroids moving 
in the same direction will never meet. """
def asteroid_collision(asteroids):
    while any(asteroids[ind] * asteroids[ind + 1] < 0 and asteroids[ind + 1] < 0 for ind in range(len(asteroids[:-1]))):
        for ind,asteroid in enumerate(asteroids[:-1]):
            if asteroid * asteroids[ind + 1] < 0 and asteroids[ind + 1] < 0:
                if abs(asteroid) > abs(asteroids[ind + 1]):
                    asteroids.pop(ind + 1)
                elif abs(asteroid) == abs(asteroids[ind + 1]):
                    asteroids.pop(ind + 1)
                    asteroids.pop(asteroids.index(asteroid))
                else: asteroids.pop(asteroids.index(asteroid))
                break
    return asteroids



print(asteroid_collision([5,10,-5])==[5,10])
print(asteroid_collision([8, -8])==[])
print(asteroid_collision([10, 2, -5])==[10])
print(asteroid_collision([-2, -1, 1, 2])==[-2, -1, 1, 2])
print(asteroid_collision([-2, 1, 1, -2])==[-2, -2])
print(asteroid_collision([1, 1, -2, -2])==[-2, -2])
print(asteroid_collision([-10, 66, -56, -9, -32, -41, 81, 10, 31, 65, -84, -73, -63, 94, -100, -56, -88, 41, 44, -45, -61, 12, 27, 85, -69, -26, -74, -18, -60, 90])==[-10, -84, -73, -63, -100, -56, -88, -45, -61, 12, 27, 85, 90])
print(asteroid_collision([50, -36, 4, 35, 43, 72, -46, 68, 65, 94, -11, -78, -59, 15, -9, 1, 96, 42, 34, 60, -42, 5, 92, -55, 26, 39, -80, -18, -87, -51, 91, -21, -7, 80, -12, -61, -32, 6, -52, -67, 46, 24, -70, -64, -94])==[50, 4, 35, 43, 72, 68, 65, 94, 15, 1, 96])
print(asteroid_collision([-24, 55, -68, 69, -35, 33, -75, -7, 9, -56, 71, 22, 59, -96, 1, -37, 61, -98, 30, -21, 57, -73, -3, -32, -93, -41, 63, 26, 41, 56, -60, 18, 67, 80, 100, -23, -53, 74, 49, 86, 48, 83, 40, 77, -57, 91, -8, 7, -33, 15, -92, 89, -48, 25, 66])==[-24, -68, -75, -7, -56, -96, -37, -98, -73, -3, -32, -93, -41, 63, 18, 67, 80, 100, 89, 25, 66])
print(asteroid_collision([-25, -97, 57, -72, -85, 89, 81, -88, 24, -5, 75, 65, 12, 43, 25, 67, 34, 98, 10, 52, -42, -55, -87, -26, 31, -59, -47, 59, 72, -70, 30, -58, -62, 15, -71, 61, 69, -79, -34, 95, -28, -12, -40, -29, -100, 38, 36, -6, 94, 96, -76, -35, 18, 41, -80])==[-25, -97, -72, -85, -100, 38, 36, 94, 96])