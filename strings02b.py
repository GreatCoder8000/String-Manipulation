string = "this exam is an example of how we can examine the curriculum"
matching = "exam"

print(".. first 'an' appears at position: ", string.find("an"))
print(".. second 'an' appears at position: ", string.find("an",15))

first_exam = string.find("matching")
second_exam = string.find("matching",first_exam+1)

print(".. first "exam" appears at position: ", first_exam)
print(".. second "exam" appears at position: ", second_exam)

position = 0
count = 0
start_position = position
uinput = input("string")
find = input("what to find")

while position >= 0:
  position = input.find(find,start_position)
  
  if position != -1:
    print("found at position:",position)
    start_position = position
    count+=1
  else:
    print("no more matches")
print("found",count,"of",find,"in phrase:",uinput)
