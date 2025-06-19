STACK = []
REGISTER = 0

def minilang(string_command):
    def n(value):
        global REGISTER
        REGISTER = value
    def PUSH():
        global REGISTER, STACK
        STACK.append(REGISTER)
    def ADD():
        global REGISTER, STACK
        REGISTER += STACK.pop()
    def SUB():
        global REGISTER, STACK
        try:
            REGISTER -= STACK.pop()
        except IndexError:
            print(f'You can not subtract from an empty stack! STACK = {STACK}')
    def MULT():
        global REGISTER, STACK
        REGISTER *= STACK.pop()
    def DIV():
        global REGISTER, STACK
        REGISTER = int(REGISTER/STACK.pop())
    def REMAINDER():
        global REGISTER, STACK
        REGISTER = int(REGISTER%STACK.pop())
    def POP():
        global REGISTER, STACK
        REGISTER = STACK.pop()
    def PRINT():
        print(f'{REGISTER}')

    commands = {
        'PRINT': PRINT,
        'PUSH': PUSH,
        'ADD' : ADD,
        'SUB' : SUB,
        'MULT' : MULT,
        'DIV' : DIV,
        'REMAINDER' : REMAINDER,
        'POP' : POP,
    }

    user_commands = string_command.split()
    for command in user_commands:
        try:
            register = int(command)
            n(register)
        except ValueError:
            commands[command]()

minilang('SUB')

minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)