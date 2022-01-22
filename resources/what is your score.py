#what is your score?

Score = int(input("What is your test score?"))

#Determine the grade
if Score >= 90:
    print ("You have an A.")
else:
    if Score >=80:
        print ("You have a B.")
    else:
        if Score >=70:
            print ("You have a C.")
        else:
            print ("NaNA NA boo boo YOU FLUNK!")