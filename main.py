


instructions = """
This will be our Tic Tac Toe board

 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|--- 
 7 | 8 | 9
   
*instructions:
 1. Insert the spot number(1-9) to put your sign.
 2. You must fill all 9 spots to get the result.
 3. Player 1 will go first.

"""


sign_dictionary = []
for i in range(9):
     sign_dictionary.append(' ')

def print_board():
  board = f"""
   
   {sign_dictionary[0]} | {sign_dictionary[1]} | {sign_dictionary[2]}
  ---|---|---
   {sign_dictionary[3]} | {sign_dictionary[4]} | {sign_dictionary[5]}
  ---|---|--- 
   {sign_dictionary[6]} | {sign_dictionary[7]} | {sign_dictionary[8]}


   """
  

  print(board)

index_list = []
def take_input(player_name):
  while True:
    x = int(input(f"{player_name}: "))
    x -= 1
    if 0 <= x <10:
      if x in index_list:
        print("This spot is blocked.")
        continue
      index_list.append(x)
      return x
    print("Please enter number between 1-9")

def calculate_result(player_one, player_two):
    
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    
    for a, b, c in wins:
        
        if sign_dictionary[a] == sign_dictionary[b] == sign_dictionary[c] == 'X':
            print(f"Congratulations {player_one}! You WON!")
            quit("Thank you both for joining.")

        
        if sign_dictionary[a] == sign_dictionary[b] == sign_dictionary[c] == 'O':
            print(f"Congratulations {player_two}! You WON!")
            quit("Thank you both for joining.")


def main():
     print("Welcome to the Tic Tac Toe game.!!")
     player_one = input("Enter player one name: ")
     player_two = input("Enter player two name: ")
     print(f"Thank you for joining {player_one} and {player_two}")

     print(instructions)

     print(f"{player_one}'s sign will be - X")
     print(f"{player_two}'s sign will be - O")

     input("Enter any key to start the game: ")

     print_board()

     for i in range(9):
         if i % 2 == 0:
             index = take_input(player_one)
             sign_dictionary[index] = 'X'
         else:
             index = take_input(player_two)
             sign_dictionary[index] = 'O'

         print_board()

         calculate_result(player_one, player_two)


     print("This a TIE, Nobody Won. Play Again.")
    




main()
