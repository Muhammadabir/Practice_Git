#The usual
print("New Python file")

#A for loop without a for loop (time complexity and space complexity is a matter of question though)
boolean_state = True
message = "The End"
final_point = 5
count = 0
while boolean_state:
    
    if(count != final_point): 
        print(count)
        count+=1
    else : 
        print(count)
        print(message)
        boolean_state = False
