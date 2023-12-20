import random

def pitcher_pro_Kopf():
    persons = {'Mattia': 0, 'Mischa': 0, 'Levin': 0}
    x = random.randrange(3, 10)
    for i in range(0, x + 1):
        y = random.choice(list(persons))
        persons[y] += 1
    max_person = max(persons, key = persons.get)
    return persons, max_person  

def gömmer_is_bqm(suffe, game):
    result = ''
    if suffe >= game:
        result = 'bqm'
    else:
        result = 'online'
    return result

def plan_für_de_abig(suffe, game):
    bqm_result = gömmer_is_bqm(suffe, game)
    pitcher_result, max_person = pitcher_pro_Kopf()
    skull_result = skull(max_person)

    if bqm_result == 'bqm':
        return f'''
        Mini Herre es freut mich, dass wir eus hüt wieder mal abschüssed. 
        Folgendi Persone münd hüt die folgendi Azahl Pitcher leere: 
        {pitcher_result}, 
        {skull_result}.'''
    
    else:
        return "Schad, dass es hüt nöd klappt, denn gömmer halt e rundi on."

def skull(max_person):

    mfg = f"""
            !!!!!!!!!!!    MFG -- {max_person} -- HAHAHAHA  !!!!!!!!!!!!
            """
    return mfg

suffe = int(input("Vo 1 bis 10 wie bock hesch zum suffe? "))
game = int(input("Vo 1 bis 10 wie bock hesch zum game? "))

print(plan_für_de_abig(suffe, game))




