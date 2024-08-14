# main function that will be called 

text_introduction = "Hello, welcome to my first Python program (or script, or module)!, \n Here I will list some of my favourite video games of all time! \n I will have them listed by console (I have kept it to five for each or we would be here all day), you can type in the console name (or abbreviation of it) to have the list generated!"

text_instructions = "You can generate a list of consoles and their abbreviations anytime by typing the word 'Console', dont worry its not case sensitive :)"
list_of_consoles = ["Playstion 2 ","Playstion 3 ","Playstion 4","Playstion 56 "]

playstation_two = {
    "playStation2 ":
     ["Grandia III", 
     "Ratchet and Clank: Deadlocked", 
     "Sly Cooper: Honor Among Thieves",  
     "Dragon Quest 8: Journey Of The Cursed King",
     "Burnout Revenge" 
     ]
}

playstation_three = {"playstation3": 
[" Metal Gear Solid 4: Guns of the Patriots", 
"BioShock",
 "Dark Souls",
  "DmC: Devil May Cry", 
  "Infamous 2"]
}

def main():
    print(text_introduction)
    user_input = input("Enter a selection:")
    while user_input != "q": 
        selection(user_input)


def selection(user_input):
    match user_input :
            case 1 : return select_playstation3()

def select_playstation3():
    for i in range(len(playstation_three)):
        print(i)

if __name__ == '__main__':
    main()