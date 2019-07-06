# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
people=['John','Saqlain']

for person in people:
    print('Curretn persosn:',person)

#Break
for person in people:
    print('Curretn persosn:',person)
    break

#Continue
for person in people:
    print('Curretn persosn:', person)
    continue

#Range
for i in range(len(people)):
    print('Current person:',people[i])


# While loops execute a set of statements as long as a condition is true.
count=0
while count<=10:
    print('Count:',count)
    count +=1