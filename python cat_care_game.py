bug = '''                        
                      \`*-.                    
                       )  _`-.                 
                      .  : `. .                
                      : _   '  \               
                      ; *` _.   `*-._          
                      `-.-'          `-.       
                        ;       `       `.     
                        :.       .        \    
                        . \  .   :   .-'   .   
                        '  `+.;  ;  '      :   
                        :  '  |    ;       ;-. 
                        ; '   : :`-:     _.`* ;
               [bug] .*' /  .*' ; .*`- +'  `*' 
                     `*-*   `*-*  `*-*'        

'''
happy = '''
          ._
              .-'  `-.
           .-'        \
          ;    .-'\    ;
          `._.'    ;   |
                   |   |
                   ;   :
                  ;   :
                  ;   :
                 /   /
                ;   :                   ,
                ;   |               .-"7|
              .-'"  :            .-' .' :
           .-'       \         .'  .'   `.
         .'           `-. ""-.-'`""    `",`-._..--"7
         ;    .          `-.J `-,    ;"`.;|,_,    ;
       _.'    |         `"" `. ."""--. o \:.-. _.'
    .""       :            ,--`;   ,  `--/}o,' ;
    ;   .___.'        /     ,--.`-. `-..7_.-  /_
     \   :   `..__.._;    .'__;    `---..__.-'-.`"-,
     .'   `--. |   \_;    \'   `-._.-")     \\  `-,
     `.   -.`_):      `.   `-"""`.   ;__.' ;/ ;   "
       `-.__7"  `-..._.'`7     -._;'  ``"-''
                         `--.,__.'          
'''
sad = '''
  _                ___       _.--.
    \`.|\..----...-'`   `-._.-'_.-'`
    /  ' `         ,       __.--'
    )/' _/     \   `-_,   /
    `-'" `"\_  ,_.-;_.-\_ ',     
        _.-'_./   {_.'   ; /
       {_.-``-'         {_/
'''
choked = '''
 _._     _,-'""`-._
     (,-.`._,'(       |\`-/|
         `-.-' \ )-`( , o o)
               `-    \`_`"'-
'''

print("Welcome to the Cat Care game")
print("Your mission is to pleased the hungry cat")
game_imgs =[bug, happy, sad, choked]
choice1 = input(
    "You are being with your cat, do you want to feed it with a fish or a bug? Type 'fish' or 'bug' \n"
).lower()
if choice1 == 'fish':
    print (game_imgs[1])
    choice2 = input(
        "Your cat is happy. There are three kinds of fish in the kitchen. Which one do you want to feed it? Type 'salmon', 'tuna' or 'sardine' \n"
    ).lower()
    if choice2 == ('salmon') or choice2== ('tuna'):
        print (game_imgs[1])
        choice3 = input(
            "Your cat is pleased and is now full. Do you want to interact more with it? Type 'yes' or 'no' \n"
        ).lower()
        if choice3 == 'yes':
            choice4 = input(
                "Choose the activity you want to do with your cat. Type 'cuddle', 'shower' or 'bug' \n"
            ).lower()
            if choice4 == 'cuddle':
                print(game_imgs[1])
                print("Your cat is very happy to be with you! You win!")
            elif choice4 == 'shower':
                print(game_imgs[2])
                print("Oops...Your cat doesn't like the shower. Game over.")
            else:
                print(game_imgs[3])
                print("Your cat got choked by eating the plastic toy bug. Game over.")
        else:
            print(game_imgs[2])
            print("Your cat is not pleased. Game over.")
    else:
        print(game_imgs[2])
        print("Your cat is allerged to sardine. She is sick. Game over.")
else:
    print(game_imgs[3])
    print("Your cat has a stomach ache and is not happy. Game over.")
