#Quiz Game

questions = ("What is the capital of Japan? : ",
 "Which planet is known as the Red Planet? : ", 
 "What is 12 * 8? : ",
  "Which language is used to create web pages? : ",
  "Which animal is the largest mammal? : ")

options = (("A. Beijing", "B. Tokyo", "C. Seoul", "D. Bangkok"),
 ("A. Venus", "B. Jupiter", "C. Mars", "D. Saturn"),
 ("A. 96", "B. 88", "C. 108", "D. 86"),
 ("A. Python", "B. HTML", "C. SQL", "D. C++"), 
 ("A. Elephant", "B. Giraffe", "C. Blue Whale", "D. Shark"))

answers = ("B", "C", "A", "B", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
  print("---------------------------")
  print(question)
  for option in options[question_num]:
    print(option)
  
  guess=input("Enter your answer(A, B, C, D): ").upper()
  guesses.append(guess)
  if guess == answers[question_num]:
    print("CORRECT !")
    score += 1
  else :
    print("INCORRECT !")
    print(f"{answers[question_num]} is the correct answer")

  question_num += 1

print("---------------------------")
print("          RESULTS          ")
print("---------------------------")

print("answers: ", end="")
for answer in answers:
  print(answer, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is {score}%")