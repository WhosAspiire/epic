import random
aiChoices = ['rock', 'paper', 'scissors']
ai = random.choice(aiChoices)
user = input('enter rock paper or scissors: ').lower()
if(ai == '' and user == ''):
  input()
