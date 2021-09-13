import random
#HANG MAN
#this is the word that will be used for test
#this is where the random words come into play
name=input(print("what is your name"))
word_1=input(print("hello "+name+" enter word"))
word_2=input(print("hello "+name+" enter word"))
word_3=input(print("hello "+name+" enter word"))
word_4=input(print("hello "+name+" enter word"))

#the words get turned into a list
words1=[word_1, word_2, word_3, word_4]
#makes the words random
word_to_guess=random.choice(words1)
wordlen=len(word_to_guess)

userinput=""
#edit this for the number of tries the player can have
lives=3
#this is where the game is really is not sure how else to explain
while lives >0:
    failcount=0
    # player input here
    word=input(" guess one letter, or try and guess the whole word")

    if word in word_to_guess:
        #shows the player if said word is correct and how many words left
        print(name+" ,what you guessed which was "+word+" is in the word you have "+str(wordlen)+" letters left to guess")
    else:
        #shows how many lives you have left and if word is correct
        failcount=failcount+1
        print("sadly, "+word+" is not one of the letters of the word to guess "+name+" you now have "+str(lives)+" lives left")
    #this is where player will lose a life
    lives = lives-failcount


    #stores words input into program
    userinput= userinput + word
    for letter in word_to_guess:
        if letter in userinput:
            print(letter, end="")
        else:
            print("_", end="")
    if word is word_to_guess:
        print("great job "+name+" you just found the word was "+word_to_guess+" with "+str(lives)+" left ")
        break

else:
    print(" sorry you did not guess the word with your lifes left. The word to guess was "+word_to_guess)
