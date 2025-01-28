import curses
import math

#function to perform the calculator operations
def calculation(expression):
    try:
        result=eval(expression)#evaluates the string expression
        return str(result)
    except Exception as e:
        return "Error"
#function to display calculator UI
def main(stdscr):
    #clear the screen and set the colour scheme
    curses.curs_set(0) #hides the curses when set to zero
    stdscr.clear()
    stdscr.refresh()
    expression=""
    result=""
    while True:
        #creating a simple menu and print it(the buttons)
        stdscr.clear()
        stdscr.addstr(0,0,"Simple Calculator",curses.A_BOLD)
        stdscr.addstr(2,0,f"Expression: {expression}")
        stdscr.addstr(3,0,f"Result:{result}")
        stdscr.addstr(5,0,"Pres 'q' to quit or use number keys and operators(+,-,*,/) and C to clear")

        #define the layout of the buttons in the calculator
        buttons=[
            ('7','8','9','/'),
            ('4','5','6','*'),
            ('1','2','3','-'),
            ('0','.','=','+')
        ]
        #display buttons
        y,x=7,0 #start position for buttons
        for row in buttons:
            for button in row:
                stdscr.addstr(y,x,button)
                x+=5
            y+=2
            x=0
        #user input
        key=stdscr.getkey()
        #quit the program if 'q is pressed
        if key=='q':
            break
        elif key in '0123456789.+-*/':
            expression+=key
        elif key == "\b" or key == "\x7f":  # "\b" for Backspace on some systems, "\x7f" on others
            expression = expression[:-1]
        elif key == '=' or key=='\n':
            result=calculation(expression)
            expression=result #shows the result as new expression
        elif key =='c':
            expression =""#clear the current expression
        stdscr.refresh()#refresh the screen
#run the program
if __name__=="__main__":
    curses.wrapper(main)
