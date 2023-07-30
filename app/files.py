file= open('app/text.txt')
#print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

for line in file:
  print(line)

file.close()


with open('app/text.txt') as file:
  for line in file:
    print(line)