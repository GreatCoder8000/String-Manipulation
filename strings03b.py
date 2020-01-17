string = "Question: Choose from A, B or C, Answer: is C"

print(string)

if string[0:7] == "Question":
  print(string, "is a Question")
else:
  print(string, "is NOT a Question")
 

print(string)

if string[0:7] == "Question":
  print(string, "is a Question")
else:
  print(string, "is NOT a Question, so is an Answer")
  
string = "Answer: is C"

print(string)

if string[0:7] == "Question":
  print(string, "is a question")
else:
  print(string, "is NOT a Question, so is an Answer")
