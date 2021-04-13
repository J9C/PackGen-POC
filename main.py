import random



FAMILYMEMBER = ["DAD", "BROTHER", "UNCLE", "AUNT", "COUSIN", "STEP SISTER", "MOM", "DOG", "GRANDMA", "GRANDPA"]
ACTIVITY = ["PUSHUPS", "SITUPS", "CHA CHA SLIDE",]
RANDOM1 = ["LONG LOST COUSIN", "DICK OUT", "ARMPITS OPEN", "PUSSY FLAPS CLOSED"]

def mainanswer():
    answer = input('WOULD YOU LIKE TO GENERATE A JOKE  : ')
    if answer == 'y':
        print(" ")
        print("THATS WHY I CAUGHT YOUR" , random.choice(FAMILYMEMBER),"DOING", random.choice(ACTIVITY), "WITH THERE", random.choice(RANDOM1))
        
mainanswer()
print(" ")
input("RESTART TO RUN ANOTHER JOKE")


