list1 = []
vowls = ['a', 'e', 'i', 'o', 'u']

list2= []

def getword(string):
    if string[0].lower() in vowls:
        return "an"
    else:
        return "a"

def new():
    
    for i in range(97 , 122 + 1):
        current_character = chr(i)
        current_string = 'i went to the market and bought'
        while True:
            try:
                item = input(f'i went to the market and bought {current_character}: ')
                if item[0].lower() != current_character:
                    continue          
                else:
                    list1.append(item)
                    break
                    
            except:
                print('try again')

        for i in range(len(list1)):
            word = list1[i]
            seperator = getword(word)
            if word == 0:
                current_string += f'{seperator} {word}'
            else:
                current_string += f' and {seperator} {word}'
        print(current_string)

new()
            
    
            
            
