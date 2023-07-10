#GradeCalculator
#Created By Cephas Cardozo

user = int(input("What is your Score?\nType here :"))

if user >= 90:
  print("A - Grade")
elif user >= 80:
  print("B - Grade")
elif user >= 70:
  print("C - Grade")
elif user >= 60:
  print("D - Grade")
elif user <= 60:
  print("F - Grade --- FAILED")
