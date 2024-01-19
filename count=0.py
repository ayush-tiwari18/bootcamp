count=0
id=0
id2=0
id3=0
while True:
  name=input("Enter your name")
  course=input("Enter your course")
  # print("Your course id is ",id)
  # id=id+1
  print(f"Name is {name} and course is {course}")
  if(course=="python"):
    print(f"id now become pythonP{id}")
    id=id+1
  elif(course=="java"):   
    print(f"id now become java{id2}")
    id2=id2+1
  elif(course=="C"):   
    print(f"id now become java{id2}")
    id3=id3+1
  else:
    print("Invalid course")
  count=int(input("close 1, continue 0"))
  if(count==1):
    break
  
  
  

