from shell_sort import shell_sort

def feedAnimals(animals,food):
    if (len(animals)==0) or (len(food)==0):
        return 0
    animals = shell_sort(animals)
    food = shell_sort(food)

    cnt = 0
    for f in food:
        if f>=animals[cnt]:
            cnt+=1
        
        if cnt == len(animals):
            break
    return cnt
        
        
    