def count_eatable_chocolates(total_money, cost_of_one_chocolate):
  ismoney = "-0123456789."
  total_money = float(''.join([x for x in total_money if x in ismoney]))
  cost_of_one_chocolate = float(''.join([x for x in cost_of_one_chocolate if x in ismoney]))
  if total_money <=0 or cost_of_one_chocolate<=0: return "Invalid Input"
  return int(total_money/cost_of_one_chocolate) + int((total_money-1)/(2*cost_of_one_chocolate))

print(f'{count_eatable_chocolates("4$", "1$")} ➞ 5')
print(f'{count_eatable_chocolates("55   $", "5$")}➞ 16')
print(f'{count_eatable_chocolates("I have 68$", "2$")}  ➞ 50')
print(f'{count_eatable_chocolates("I got -68$ from my mom ", "2$")} ➞ "Invalid Input"')

#  a = [1, 2, 3, 4]
#  res = list(map(lambda x: x ** 2, a))
#  print(res)