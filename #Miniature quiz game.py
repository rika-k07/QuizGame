#Miniature quiz game 
print("Welocme to the Quizzarena!!\nDo you have what it takes to win this?\nCome on, let's find out :) ")
opt=input("Are you ready to play? ")
if opt.lower()=='yes':
    print("Let's get started")
else:
    print("Do come back and play again")
c=0
while opt.lower()=='yes':
    q1=input(("1.What does OS stand for?\nA) Open Software\nB) Operating System\nC) Output System\nD) Order Software  \n"))
    if q1.lower()=='b':
        print('CORRECT')
        c+=1
    else:
        print('WRONG')

    q2=input(("2.Which data structure works on FIFO principle?\nA) Stack\nB) Queue\nC) Tree\nD) Graph\n"))
    if q2.lower()=='b':
        print('CORRECT')
        c+=1
    else:
        print('WRONG')

    q3=input(("3.Which language is primarily used for web page structure?\nA) Python\nB) C++\nC) HTML\nD) Java\n"))
    if q3.lower()=='c':
        print('CORRECT')
        c+=1
    else:
        print('WRONG')

    q4=input(("4.Which of the following is NOT an operating system?\nA) Windows\nB) Linux\nC) Oracle\nD) macOS\n"))
    if q4.lower()=='c':
        print('CORRECT')
        c+=1
    else:
        print('WRONG')

    q5=input(("5.Which of the following is a non-volatile memory?\nA) RAM\nB) Cache\nC) Register\nD) ROM\n"))
    if q5.lower()=='d':
        print('CORRECT')
        c+=1
    else:
        print('WRONG')
    break
if c<=3:
    print("Your total score is",c,'/5\n')   
else:
    print("Great Jop! Your total score is",c,'/5')














