print('Answer just "Yes" or "No".')

answer1_statement = input("Are you still looking for a content creator/social media manager? ")
answer2_statement = input("Do you want somebody who is interested in coding a programming? ")
answer3_statement = input("Do you like MEMEs? ")

if answer1_statement == "Yes" or answer1_statement == "yes" or answer1_statement == "YES":
    answer1 = True
elif answer1_statement == "No" or answer1_statement == "no" or answer1_statement == "NO":
    answer1 = False
else:
    print("Ivalid value.")

if answer2_statement == "Yes" or answer2_statement == "yes" or answer2_statement == "YES":
    answer2 = True
elif answer2_statement == "No" or answer2_statement == "no" or answer2_statement == "NO":
    answer2 = False
else:
    print("Ivalid value.")

if answer3_statement == "Yes" or answer3_statement == "yes" or answer3_statement == "YES":
    answer3 = True
elif answer3_statement == "No" or answer3_statement == "no" or answer3_statement == "NO":
    answer3 = False
else:
    print("Ivalid value.")

if answer1 and answer2 and answer3:
    print("Nika should be hired.")
elif answer2 and answer3:
    print("Ouuu... So, am I too late for this position?")
elif answer1 and answer3:
    print("That's a pitty! It seems that coding and programming could be fun. 😏")
elif answer1 and answer2:
    print("Waaat?! 😱 MEME's are great!")
else:
    print("Why am I writing to you? 😅")