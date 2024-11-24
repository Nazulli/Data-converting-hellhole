import random
import time

ProgramIsAlive = True
convTypes = ['bool', 'int', 'float', 'string']

print("Hi. Today we will be converting a variable into other types. Let's get started.")
UservarToManip = input("Go ahead and give me any input.\n")
    
print(f"Great. Next, choose what type of variable you'd like this to be.")
    
while ProgramIsAlive:
    print(f"{convTypes}")

    UserRequestedVarType = input('')
    match UserRequestedVarType:
        case 'bool':
            convertedType = bool(UservarToManip)
                        
        case 'int':
            try:
                ConvertedUserVar = int(UservarToManip)
            except ValueError:
                print("Invalid input for int conversion. Please try again.")
            continue
                        
        case 'float':
            convertedType = float(UservarToManip)
                        
        case 'string':
            convertedType = str(UservarToManip)
        case _:
            print("Invalid response given. Please try again.")
            continue
                        
                
    print(f"'{UservarToManip}' is now a" , (type(convertedType)))        
        #time.sleep(1)
    print(f"Nice job. We will be switching it up shortly.")
        #time.sleep(1)
    print(f"Now, would you like to choose a new type to convert your original string to, or let it be random? (Select 1 or 2.)")
        #time.sleep(1)
    UserResponse = input()

    if UserResponse == "1":
        print("Okay. Please pick a type to convert the variable into.")
        print(convTypes)
        UserTypeSelected = input().lower()
        
        if UserTypeSelected in convTypes:
            match UserTypeSelected:
                 case 'bool':
                     print(f"So it's true you want to turn '{UservarToManip}' into a bool? Processing...")
                     ConvertedUserVar = bool(UservarToManip)
                     
                 case 'int':
                     print("So many possibilities, it seems int-possible to decide for {UservarToManip}. Calculating...")
                     ConvertedUserVar = int(UservarToManip)
                 
                 case 'float':
                     print("Can {UservarToManip} float and boat? Converting variable...")
                     ConvertedUserVar = float(UservarToManip)
                     
                 case 'string':
                     print("It's a cats favorite thing to play with and also the type you're looking for! Stringing {UservarToManip} up now...")
                     ConvertedUserVar = str(UservarToManip)
                     
                 case _:
                     print("Invalid choice selected. Please try again.")
        else:
            print("Invalid.")
                
            #time.sleep(3)
            print("Done!")
           # time.sleep(1)
            print(f"Awesome. Your '{UservarToManip}' is now a '{ConvertedUserVar}'")
            
    elif UserResponse == "2":
        print("You have chosen to randomize the variable. Beware of Rand the ruiner of ways...")
      #  time.sleep(1)
        print(random.choice(convTypes), "has been chosen. Be prepared for your conversion...")
        
        
        

