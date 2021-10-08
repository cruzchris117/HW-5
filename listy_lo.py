

food = ['rice', 'beans']

food.append('broccoli')

print(food)

new_list = ['bread', 'pizza']

food.extend(new_list)

print(food)


print(food[0:2])

print(food[4])


breakfast = "eggs,fruit,orange juice"

breakfast = breakfast.split(',')

print(breakfast)

print(len(breakfast))

values = []

while True:
    ur_input = input("give me a float: ")
    if (ur_input=='stop'):
        break
    else: 
        values.append(float(ur_input))

print(min(values))
print(max(values))

average = 0

for numbers in values:
    average += numbers

average = average/len(numbers)

#------------------------------------



list = []
while "stop" not in list:
  list.append(input("print a float. input \"stop\" to stop "))
list.remove("stop")
list = [float(i) for i in list]
list.sort()
print("average", sum(list)/len(list), "lowest value", list[0], "highest value", list[-1])


