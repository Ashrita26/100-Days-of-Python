#This is Tressure island Project
#The picture is bacially to make the projet look attractive, the code is not related with the picture
print("Want to find the Tressure!!!!")
print('''____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/''')
ans=input("Turn left or right? \n-----( PRESS 'L' for left and 'R' for right)------  ")
print("\n\n\n||||||||||CAUTION|||||||||||")
print("\nRIVER HAS MANY DANGEROUS ANIMALS!!")
pat=input("\n\nWill wait for the boat or swim accross the river? \n------( PRESS 'B' for boat and 'S' for swim)-----------  ")
room=input("\n\nNow you enterd a Mansion with THREE rooms!\n\n Which colour door will you open! (PRESS 'R' for RED, 'Y' for YELLOW, 'O' for ORANGE)--------   ")
if ans=='L':
    print("You entered Lava!!!\n ----Game Over!----")
elif ans=='R':
    if pat=='S':
        print("Game Over!")
    elif pat=='B':
        if room=='Y':
            print("\n\nCONGRATULATIONS! \nYou are the winner!")
            print("-------THE TRESSURE IS YOURS!----------")
        elif room=='R':
            print("You entered the FIREEE!!! \n  ----Game Over!----")
        elif room=='O':
            print("You Fell into a Hole!!! \n  ----Game Over!----") 
        else:
            print("\n\nWrong choice! Try Again!..")
    else:
        print("\n\nWrong choice! Try Again!..")
else:
    print("\n\nWrong choice! Try Again!..")