user_input = input("> ")
while user_input.lower() != "stop":
   
    if user_input.lower() == "start":
        print("Car started... Ready to go")
    elif user_input.lower() == "stop":
        print("Car stopped.")
    elif user_input.lower() == "help":
        print("start - to start the car \n stop - to stop the car \n Quit - to exit")
    else:
        print("I don't understand that...")
        
    user_input = input("> ")

quit()
