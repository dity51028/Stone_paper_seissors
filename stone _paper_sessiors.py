
import random
print("\n\n\t\t****stone_paper_sessiors****\n\n")
list=["stone","paper","sessiors"]
print("\n\t\tYou can play 5 times\n\n")
your_score=0
comp_score=0

for i in range(0,5):
    comp=random.choice(list)
    print("\nEnter your choise")
    my_choice=input()

    if comp=='stone' and my_choice=='paper' or comp=="paper" and my_choice=="sessiors" or comp=="sessiors" and my_choice=="stone":
        print("\nYou win computer's choice ")
        print(comp)
        your_score=your_score+1
    elif my_choice=='stone' and comp=='paper' or my_choice=="paper" and comp=="sessiors" or my_choice=="sessiors" and comp=="stone":
        print("\ncomputer win computer's choice")
        print(comp)
        comp_score=comp_score+1
    else:
        print("\nBoth choice are same computer choose")
        print(comp)

if your_score>comp_score:
    print("\n\n\t\tCongrats...You win!!!!\n\n")
elif your_score<comp_score:
    print("\n\n\t\tComputer win!!!!Better luck next time\n\n")
else:
    print("\n\nBoth are same\n\n")









    """
if comp=='stone' and my_choice=='paper':
    print("You win computer's choice ",comp)
elif comp=="paper" and my_choice=="sessiors":
    print("You win computers choice",comp)
elif comp=="sessiors" and my_choice=="stone":
    print("You win computer's choice",comp)
elif my_choice=='stone' and comp=='paper':
    print("Computer win computer's choice ",comp)
elif my_choice=="paper" and comp=="sessiors":
    print("computer win computers choice",comp)
elif my_choice=="sessiors" and comp=="stone":
    print("computer win computer's choice",comp)
else:
    print("Both choice are same computer choose",comp)
"""