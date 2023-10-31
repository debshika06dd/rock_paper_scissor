import random

print('Winning rules of the game \n'
      +"Rock vs Paper-> Paper wins\n"
      +"Rock vs Scissors->Rock wins\n"
      +"Paper vs Scissors->Scissors wins\n")

print("Choices:\n 1.Rock\n 2.Paper\n 3.Scissors\n")

user_choice=int(input("Enter your choice:"))
comp_choice=random.randint(1,3)

u_choice_name=""
c_choice_name=""

if user_choice==1:
        u_choice_name='Rock'
elif user_choice==2:
        u_choice_name='Paper'
else:
        u_choice_name='Scissors'

if comp_choice==1:
        c_choice_name='Rock'
elif comp_choice==2:
        c_choice_name='Paper'
else:
        c_choice_name='Scissors'

print("\nUser Choice is:", u_choice_name,"\n")
print("Computer's Choice is:", c_choice_name, "\n")
print(u_choice_name, "vs", c_choice_name)

if user_choice==comp_choice:
        print("\It's a tie\n")
elif user_choice==1:
        if comp_choice==2:
                print("\nPaper covers Rock! You lose\n")
        else:
                print("\nRock smashes Scissors! You win\n")
elif user_choice==2:
        if comp_choice==1:
                print("\nPaper covers Rock! You win\n" )
        else:
                print("\nScissors cut the Paper! You lose\n")
elif user_choice==3:
        if comp_choice==1:
                print("\nRock smashes Scissors! You lose\n")
        else:
                print("\nScissors cut the paper You win\n")
