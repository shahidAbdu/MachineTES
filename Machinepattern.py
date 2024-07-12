# rows k range columns in j range
columns=int(input('no of columns'))
rows=int(input('no of rows'))
for k in range(rows): 
    for i in range(3):
        for j in range(columns):
            if i==0 and k==0:
                if j%2==0:
                    print(" ___",end='')
                else:
                    print("    ",end='')
            if j==columns-1 and i==0:
                print()

            if i==1 and j%2==0:
                print("/   \\",end='')

            if i==1 and j%2!=0:
                print("___",end='')
            
            if i==1 and j==columns-1:
                print()
           
            if i==2 and j%2==0:
                print('\___/',end='')
           
            if i==2 and j%2!=0:
                print("   ",end='')
              