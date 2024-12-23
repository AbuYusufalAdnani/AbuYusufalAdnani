print("-------Welcome to the Quiz Game!-------")

Question1 = input("When did WW1 start? \n 1914? \n 1918? \n 1917? \n 1920? \n 1936? \n --Answer-- \n ")
Question2 = input("When did the Korean War first start? \n 1945? \n 1950? \n 1930? \n 1953? \n --Answer-- \n")
Question3 = input("When did the American Stockmarket crash occur? \n 2001 \n 2003 \n 2005 \n 2007 \n 2008 \n --Answer-- \n")
CorrectAnswer = "\n --Correct!--"
WrongAnswer = "\n --Incorrect!--"

if Question1 == "1914":
    print(CorrectAnswer)
else:
    print(WrongAnswer)

if Question2 == "1953":
    print(CorrectAnswer)
else:
    print(WrongAnswer)

if Question3 == "2007" or "2008":
    print(CorrectAnswer)
else:
    print(WrongAnswer)
