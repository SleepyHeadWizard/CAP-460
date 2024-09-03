''''scenario: simulate a traffic light at a intersection)
task: write a program that take an input color (green, yellow, red)and print the crossponding action (go, slow down, stop). use conditnol statement to implement the logic.
'''
while True:
    current_color = input("Enter the color of the traffic light: ")
    if current_color == "green":
        print("Go")
    elif current_color == "yellow":
        print("Slow down")
    elif current_color == "red":
        print("Stop")
    else:
        print("Invalid color")


    