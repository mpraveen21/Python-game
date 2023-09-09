import random


MAX_VALUES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count  = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8

}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][lines]
        for colums in columns:
            symbol_to_check = columns[line]
            if symbol !=symbol_to_check:
                break
            else:
                winnings += values[symbol] * bet
                winning_lines.append(lines +1)
                
    return winnings ,winning_lines
            
    

def get_slot_machine_spin(rows,cols,symbols):
    all_symbol= []
    for symbol , symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbol.append(symbol)
            
    columns = []
    for _ in range(cols):
        column =[]
        current_symbols = all_symbol[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
        
    return columns




def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end= " | ")
            else:
                print(column[row],end = "")
        
        print()




def deposit():
    while True:
        amount = input("ENTER THE AMOUNT TO BE DEPOSIT $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("AMOUNT MUST BE GREATER THAN 0")
        else:
            print("ENTER THE VALID AMOUNT")
    return amount
 
 
 
 
 
def get_number_of_lines():
    while True:
        lines = input("ENTER THE NUMBER OF LINES TO BET ON (1-{})? ".format(MAX_VALUES))
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_VALUES :
                break
            else:
                print("ENTER THE VALID NUMBER OF LINES")
        else:
            print("ENTER THE VALID DIGIT:")
    return lines  





def get_bet():
    while True:
        amount = input("WHAT WOULD YOU LIKE TO BET ON EACH LINE ? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<= amount <= MAX_BET:
                break
            else:
                print(f"AMOUNT MUST BE between ${MIN_BET}-${MAX_BET}.")
        else:
            print("ENTER THE VALID AMOUNT")
    return amount
    
def spin(balance):
    lines  = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"YOU ARE NOT HAVING SUFFICIENT BALANCE TO BET... AND YOUR BALANCE IS ${balance}")
        else:
            break
    print(f"YOU ARE BETTING $ {bet} on {lines} lines. TOTAL AMOUNT OF BETTING: ${total_bet}")
   
   
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines = check_winnings(slots,lines,bet,symbol_values)
    print(f"you won ${winnings}.")
    print(f"you won on  lines:",*winning_lines)
    return winnings-total_bet



def main():
    balance  = deposit()
    while True:
        print(f"CURRENT BALANCE IS A ${balance}")
        answer = input("PRESS ENTER TO PLAY(q TO QUIT).")
        if answer == "q":
            break
        balance += spin(balance)
   
    print(f"YOU LEFT WITH ${balance}")
main() 
