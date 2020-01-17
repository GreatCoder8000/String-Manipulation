string = "Question: Choose from A, B or C, Answer: is C"

print(string)

if string[0:7] == "Question":
  print(string, "is a Question")
else:
  print(string, "is NOT a Question")
 

print(string)

if string.find("answer") != -1:
  print(string, "is a Question")
else:
  print(string, "is NOT a Question, so is an ", string[0:5])
  
string = "Answer: is C"

print(string)

if string[0:7] == "Answer":
  print(string, "Question is: ",string[1,string.find("C")])
else:
  print(string, "is NOT a Question, so is an ", string[0:5])
