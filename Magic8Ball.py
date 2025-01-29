#Magic8Ball.py
#Name:
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
  answers = ["Yes", "Yes-definetely", "No", "Very Doubtful", "Ask Again Later", "Cannot Predict Now", "It is certain",
              "Most Likely", "I say no", "Outlook good", "Outlook bad", "Not so sure", 
              "it is certain", "It is not certain", "You may rely on it", "You may not like it"]
  #Answer question randomly with one of the options from your earlier list.
  question = input("Ask a question: ")
  num = random.random()
  num = num * 1000
  num = int(num)
  num = num % 15
  print(answers[num])
  #print(answers[16])

  response = random.choice(answers)
  print(response)
  print(random.choice(answers))


if __name__ == '__main__':
  main()
