def infinite_gold_pouch(num_coins_in, show_solution = False, return_ans = False):
  """
  This function calculates the solution to the problem presented in:
  https://www.youtube.com/watch?v=qgvmJTmJIKs
  'This one weird trick will get you infinite gold - Dan Finkel' by Ted-Ed

  It accepts the number of coins as an input,
  and prints the resulting number of coins as an output.

  Options to show the solution and return the answer as a value are also available.
  """
  # mini-problem: need to make sure that input number is an integer
  # solution: use try-except as failsafe
  try:
    num_coins_in = int(num_coins_in) # convert the input into an integer
  except:
    print("Number of coins must be an integer!")
    return None # forces the function to immediately end

  # mp: need to represent an table for solution
  # s: create three list variables to represent each column
  # initiate the three columns representing our table
  column1 = [0] * num_coins_in
  column2 = [0] * num_coins_in
  column3 = [0] * num_coins_in

  # mp: need to assign values to column1 and column3
  # s: use for loops to change values in created lists
  # populate column1 with integer sequence
  for i in range(num_coins_in):
    column1[i]=i+1
  # populate the column3 with multiples of 3
  for i in range(num_coins_in):
    column3[i]=(i+1)*3

  # mp: start solution for column2
  # s: assign first known value column2
  # initiates the first value of column2
  column2[0] = 2

  # mp: solve for the remaining values in column2
  # s: use for loops to iterate through list,
  # and if-else to assign values based on rules
  # compute for the values of the second column
  for i in range(num_coins_in): # this loop will run for the number of elements in column2
    if column2[i] == 0: # checks if the current number is 0, else it skips over
      if column1[i] in column2: # checks if a prior sequence has been established
        column2[i] = column3[column2.index(column1[i])] # copies the element from column3 to its equivalent index in column2
      else:
        column2[i] = column2[i-1]+1 # makes the element larger than the previous entry by 1
    else:
      pass

  # assigns the answer to variable
  num_coins_out = column2[num_coins_in-1]

  # mp: display solution
  # s: create a function to display lists in table format
  # will show the solution table if True
  if show_solution == True:
    list_to_table(column1, column2, column3)

  # will print out the answer by default, else will return the answer as an integer
  if return_ans == True:
    return num_coins_out
  else:
    print(f"{num_coins_in} coins will yield {num_coins_out} coins")


def list_to_table(*columns, column_width = 10, outer_line = '|', inner_line = '->'):
  """
  This function takes in multiple lists and prints them out in a table format.

  The input columns have to be distinct.
  """
  print("-"*((len(columns)*column_width)+(len(outer_line)*2)+(len(inner_line)*(len(columns)-1))))
  for row in range(len(columns[0])):
    print(outer_line, end = '')
    for col in columns:
      print(f"{col[row]: ^{column_width}}", end='')
      print(inner_line, end = '')
      if (columns.index(col)+1) % len(columns) == 0:
        print(('\b'*len(inner_line))+outer_line)
  # print("-"*36)
  print("-"*((len(columns)*column_width)+(len(outer_line)*2)+(len(inner_line)*(len(columns)-1))))
     
