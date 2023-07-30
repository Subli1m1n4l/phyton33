with open('app/text.txt','w+') as file:
  for line in file:
    print(line)
  file.write('nuevas cosas en el archivo \n')
  file.write('nuevas cosas en el archivo2 \n')
  file.write('nuevas cosas en el archivo3 \n')
  file.write('nuevas cosas en el archivo4 \n')
  