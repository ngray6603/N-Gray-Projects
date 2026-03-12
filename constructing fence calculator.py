#Fence details
Fence_Length= float(input("What is the length of your fence?"))
Fence_width= float(input("What is the width of your fence?"))
How_far_are_post=float(input("How far apart would you like each post?"))
#calculation of post
Total_Fence = Fence_Length * Fence_width

Length_board=float(input("What length of board do you need?"))
Single_board_across_fence =  Total_Fence / Length_board
Number_boards_per_post=float(input("How many boards for each post?"))
Total_number_boards=Number_boards_per_post * Single_board_across_fence
Cost_of_board=float(input("What is the cost of each board?"))
print("Total number of post needed:" +str(Total_Fence))
print("Total numer of boards required:" +str(Total_number_boards))
print("Cost of each board:" +str(Cost_of_board))
print("total cost of all boards:" +str(Cost_of_board * Total_number_boards))

