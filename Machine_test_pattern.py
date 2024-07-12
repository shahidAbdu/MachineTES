def hexagon_pattern(rows,columns):
  for k in range(rows):
      # Loop through each row of the pattern
      for i in range(3):
          # Loop through each column of the pattern
          for j in range(columns):
              # Determine the character to print based on row and column index
              if i == 0 and k==0:
                  if j % 2 == 0:
                      print(" ___", end='')
                  else:
                      print("    ", end='')
                  # Print a newline at the end of the first row
                  if j == columns - 1:
                      print()
              
              elif i == 1:
                  if j % 2 == 0:
                      print("/   \\", end='')
                  else:
                      print("___", end='')
                  # Print a newline at the end of the second row
                  if j == columns - 1:
                      print()
              
              elif i == 2:
                  if j % 2 == 0:
                      print("\\___/", end='')
                  else:
                      print("   ", end='')
                  
                  # Print a newline at the end of the third row
                  if j == columns - 1:
                      print()

rows = int(input('Number of rows: '))
columns = int(input('Number of columns: '))
hexagon_pattern(rows,columns)