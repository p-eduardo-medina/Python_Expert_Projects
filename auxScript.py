
a = [1,2,3]

for i in range(5):
    try:
        print(a[i])
    except Exception as e:
        print(f'Exeption: {e}')
        a.append(i+1)
print(a)