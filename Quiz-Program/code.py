quiz = {
     "question1": {
          "question": "what is the capital of India?",
          "answer": "Delhi"
     },
     "question2": {
          "question": "what is the national bird of India?",
          "answer": "Peacock"
     },
     "question3": {
          "question": "which city is called pink city in  India?",
          "answer": "Jaypur"
     },
     "question4": {
          "question": "what is the national animal of India?",
          "answer": "Tiger"
     },
     "question5": {
          "question": "who is the king of fruit?",
          "answer": "Mango"
     },
     "question6": {
          "question": "who invent zero?",
          "answer": "Aariya bhath"
     },
     "question7": {
          "question": "what is the capital of france?",
          "answer": "Paris"
     },
}

score = 0

for key, value in quiz.items():
     print(value['question'])
     answer = input("Answer? ")

     if answer.lower() == value['answer'].lower():
          print('correct')
          score = score + 1
          print('your score is: ' + str(score))

     else:
          print('wrong:')
          print('The answer is: ' + value['answer'])
          print('your score is: ' + str(score))

print("You get "+ str(score) + "out of 2 questions correctly")
print("Your percentage is " + str(int(score/7 *100)) + "%")