# Control Flow

## Karel Flow 
    - Multi-line comment -> """ \n comment \n """
    - Software Engineering Princpile - write readable code
## Control Flow  
    - for loop -> while loop -> if -> if/else -> control flow

### for loop
    - Syntax =>
        for i in range(count):
            statements } body of loop # indent the body  

        EG - def turn_right():
                for zi in range(3):
                    turn_left() # note indentation
    - Post/Precondition 

### if statement
    - Syntax =>
        if condition: // can be tr
            statements } body of loop # indent the body  

        EG - def safe_pick_up():
                if beepers_present():
                    pick_beeper() # note indentation

### if-else statement
    - Syntax =>
        if condition: // can be tr
            statements } body # body -> if true
        else:  
            statements # body -> if false 

        EG - def invert_beepers():
                if beepers_present():
                    pick_beeper() # note indentation
                esle:
                    put_beeper()