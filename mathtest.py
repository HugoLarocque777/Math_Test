print ("this is a math test")
correct_answers = 0

print ("what is 10 X 10")
answer = input()
if answer == "100":
    print ("correct")
    correct_answers += 1
else:
    print("sorry, incorrect")

print ("what is 90 divided by 9")
answer1 = input()
if answer1 == "10":
    print ("correct")
    correct_answers += 1
else:
    print ("sorry, incorrect")

print ("what is 20 + 49")
answer2 = input ()
if answer2 == "69":
    print ("correct")
    correct_answers += 1
else:
    print ("sorry, incorrect")

print ("what is 16 percent of 100")
answer3 = input()
if answer3 == "16" or answer3 == "16 percent" or answer3 == "16%":
        print ("correct")
        correct_answers += 1
else:
    print ("sorry, incorrect")

print ("what is (5 X 2) X 2 + (8 - 6)")
answer = input()
if answer == "22":
    print ("correct")
    correct_answers += 1
else:
    print("sorry, incorrect")

percentage = (correct_answers / 5) * 100
print(f"You got {percentage}% correct!")
