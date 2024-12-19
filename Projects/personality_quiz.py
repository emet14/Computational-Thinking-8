kendrick_points = 0
tyler_points = 0


answer = input("What song is better, A) Tv off, or B) Darling, I")
if answer == "a":
    kendrick_points += 1
elif answer == "b":
    tyler_points += 1


answer = input("What song is better, A) Squabble up, or B) Hey jane")
if answer == "a":
    kendrick_points += 1
elif answer == "b":
    tyler_points += 1


answer = input ("What song is better, A) Gloria, or B) Judge judy")
if answer == "a":
    kendrick_points += 1
elif answer == "b":
    tyler_points += 1


answer = input ("What song is better, A) Luther, or B) Take you mask off")
if answer == "a":
    kendrick_points += 1
elif answer == "b":
    tyler_points += 1


answer =  input ("what song is better, A) Gnx, or B) See you again")
if answer == "a":

    kendrick_points += 1
elif answer == "b":
    tyler_points += 1


if tyler_points > kendrick_points:
    print("You are a Tyler fan")
elif kendrick_points > tyler_points:
    print("You are a Kendrick fan")
elif tyler_points == kendrick_points:
    print("You are a fan of Tyler and Kendrick")