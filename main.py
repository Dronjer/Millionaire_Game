'''
This game program allows the user to play a game called Who Wants to Be a Millionaire. 
The game is played by asking the user a series of questions, and the user has to answer.

Game Rules:
1. There are a total of 10 questions 
2. Each question has four options
3. Each question has a certain amount of money
4. If the user answers the question correctly, the user gets the amount of money for that question.
5. If the user answers the question incorrectly, the game ends, and the user gets the amount of money they have.
6. If the user answers all the questions, he will be rewarded with a million dollars.
7. Least amount of money is $0.
'''
count = 0
print('Wish you the very best and the game begins from here')
print('Welcome to Who Wants to Be a Millionaire')
print()
list1 = (2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000, 512000, 1000000)
print('The money amounts are as follows(in USD): ', list1)
print()
while True:
    print('Question 1: What is the capital of India? \n 1. New Delhi \n 2. Mumbai \n 3. Kolkata \n 4. Chennai')
    if int(input('Enter your answer: ')) == 1:
      print(f'Congratulations! You have won ${list1[0]}')
      count += 1
    else:
      print('Sorry that is wrong answer. I am sad, but you have lost the game.')
      print()
      print('Total money earned is: ', list1[0])
      count += 1
      break
    print()
    print('Question 2: What is the capital of USA? \n 1. Washington DC \n 2. New York \n 3. San Francisco \n 4. Chicago')
    if int(input('Enter your answer: ')) == 1:
      print(f'Congratulations! You have won ${list1[1]}')
      count += 1
    else:
      print('Sorry that is wrong answer. I am sad, but you have lost the game.')
      print()
      print('Total money earned is: ', sum(list1[:2]))
      count += 1
      break
    print()
    print('Question 3: Which city was recoganised as the home for Levis Jeans? \n 1. New York \n 2. London \n 3. Pairs \n 4. San Francisco')
    if int(input('Enter your answer: ')) == 4:
      print(f'Congratulations! You have won ${list1[2]}')
      count += 1
    else:
      print('Sorry that is wrong answer. I am sad, but you have lost the game.')
      print()
      print('Total money earned is: ', sum(list1[:3]))
      count += 1
      break
    print()
    print('Question 4: What is G stands for in Parle G biscuit? \n 1. Gold \n 2. Grapes \n 3. Glucose \n 4. Garlic')
    if int(input('Enter your answer: ')) == 3:
      print(f'Congratulations! You have won ${list1[3]}')
      count += 1
    else:
      print('Sorry that is wrong answer. I am sad, but you have lost the game.')
      print()
      print('Total money earned is: ', sum(list1[:4]))
      break
    print()
    print('Question 5: What is a group of flamingoes called? \n 1. Flock \n 2. Herd \n 3. Brood \n 4. Flamboyance')
    if int(input('Enter your answer: ')) == 4:
      print(f'Congratulations! You have won ${list1[4]}')
      count += 1
    else:
      print('Sorry that is wrong answer. I am sad, but you have lost the game.')
      print()
      print('Total money earned is: ', sum(list1[:5]))
      break
    print()
    print('Question 6: What is the name of the longest river in the world? \n 1. Amazon \n 2. Nile \n 3. Yangtze \n 4. Mississippi')
    if int(input('Enter your answer: ')) == 2:
      print(f'Congratulations! You have won ${list1[5]}')
      count += 1
    else:
      print('Sorry that is wrong answer. I am sad, but you have lost the game.')
      print()
      print('Total money earned is: ', sum(list1[:6]))
      break
    print()
    print('Question 7: What is the color of the black box ? \n 1. Black \n 2. White \n 3. Red \n 4. Orange')
    if int(input('Enter your answer: ')) == 4:
      print(f'Congratulations! You have won ${list1[6]}')
      count += 1
    else:
      print('Sorry that is wrong answer. I am sad, but you have lost the game.')
      print()
      print('Total money earned is: ', sum(list1[:7]))
      break
    print()
    print('Question 8: What is the name of the largest ocean in the world? \n 1. Atlantic \n 2. Pacific \n 3. Indian \n 4. Arctic')
    if int(input('Enter your answer: ')) == 2:
      print(f'Congratulations! You have won ${list1[7]}')
      count += 1
    else:
      print('Sorry that is wrong answer. I am sad, but you have lost the game.')
      print()
      print('Total money earned is: ', sum(list1[:8]))
      break
    print()
    print('Question 9: What is the name of the largest country in the world by area? \n 1. USA \n 2. China \n 3. Russia \n 4. India')
    if int(input('Enter your answer: ')) == 3:
      print(f'Congratulations! You have won ${list1[8]}. The next question is the last one.')
      count += 1
    else:
      print('Sorry that is wrong answer. I am sad, but you have lost the game.')
      print()
      print('Total money earned is: ',sum(list1[:9]))
      break
    print()
    print('Question 10:How many bones we have in ear? \n 1. 0 \n 2. 1 \n 3. 2 \n 4. 3')
    if int(input('Enter your answer: ')) == 4:
      print(f'Congratulations! You have won ${list1[9]}.')
      count += 1
    else:
      print('Sorry that is wrong answer. I am sad, but you have lost the game.')
      print()
      print('Total money earned is: ',sum(list1[:10]))
    break
  
print()
print('Number of questions answered correctly: ', count)
if count == 10:
      print('Congratulations! You have won the game. \n You are the Millionaire')
else:
  print('Better Luck Next Time')

