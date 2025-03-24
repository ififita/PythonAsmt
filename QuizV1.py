#this program is a simple chemistry quiz
score = 0
Qa = {'Carbon':'4',
      'Magnesium':'2',
      'Chlorine':'7'}
print("Please enter all answers as an integer.")
for k,v in Qa.items():
    user_ans = input(f'How many valence electrons does {k} have? ')
    if user_ans == v:
        print('Correct!')
        score+=1
    else:
        print('Incorrect.')
    
print(f'Final score: {score}')
        
