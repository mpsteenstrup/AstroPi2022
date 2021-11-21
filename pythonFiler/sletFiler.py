# getting the file based on the ending. can be used to delete alle .jpg files

import os
files = os.listdir('.')
for f in files:
        print(f)


for f in files:
        if f.endswith('.jpg'):
                print('her er billederne:', f)


# der er ingen fortrydknap her!!!!!
for f in files:
        if f.endswith('.jpg'):
                os.remove(f)

# opretter en folder ( som så kan slettes)
#os.mkdir('test')

# for at fjerne en hel folder, PAS PÅ, I sletter!!!
#files =os.listdir('test')
#for f in files:
#        print('test/',f)
