current_val = 1 
print(f"Initially, current value = {current_val}")
print("Exit the loop when the current value is 3")
while current_val < 5:
    current_val += 1
    print(f"The current value = {current_val}")
    if current_val == 3:
        break
    print("I'm still inside the loop")
print("The task is completed now.")