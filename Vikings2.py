while True:
    userInput = input("Enter the name of the king : ")
    wrong_answer_message= " Your answer is wrong "

    if userInput == "Ragnar Lothbrock":
        print("Yes, your king is Ragnar Lothbrock!")
        print("You won GAME OVER")
        break  # Ends the loop
    elif userInput == "King Horik":
        print(wrong_answer_message )
        print("King Horik was deposed brutally by Ragnar!")
    elif userInput == "Bjorn Ironside":
        print(wrong_answer_message )
        print("Bjorn is Ragnar's mighty son!")
    elif userInput == "Quit":
        print("Goodbye, warrior.")
        break
    else:
        print("That name is not a true viking. Try again.")