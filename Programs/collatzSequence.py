def collatz(number):
    if number % 2 == 0:
        print(number//2)
        return number // 2
    elif number % 2 == 1:
        print(3*+number+1)
        return 3 * number + 1
r=''
print('Enter the number')
while r != int:
    try:
        r=input()
        while r != 1:
            r=collatz(int(r))
        break   
    except ValueError:
            print ('Please enter an integer')

# https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff
# https://www.reddit.com/r/learnpython/comments/4ps9zn/the_collatz_sequence_automate_the_boring_stuff/
