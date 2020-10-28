tamagoch = {
    "имя": "tamagoch",
    "возраст": 1,
    "здоровье": 100,
    "сила": 10,
    "сытость": 10,
}

def print_tamagoch(tamagoch) :
    for key,value in tamagoch.items() :
        print(key, value)

#def feed_tamagoch(tamagoch) : 
    #tamagoch["сытость"] = 100
        

print_pet(tamagoch)