import numpy as np
import random 

L = np.zeros(150).reshape(10,15)
print(L)

total = 0
filled1 = 0
filled2 = 0
filled3 = 0
filled4 = 0
filled5 = 0
filled6 = 0
filled7 = 0
filled8 = 0
filled9 = 0
filled10 = 0

y=1


while total<= 150:
    row = int(input('enter row: '))
    x= int(input('enter number of seats: '))
    if row == 1:
        if x <= 15 - filled1:
            L[0,filled1 : filled1+x]=y
            total = total + x
            filled1 = filled1 + x + 1
            y+=1
            print(L)
        elif x > 15 - filled1:
            if filled1 >= 15:
                print('no more seats available in this row')
            else:
                split=input(('Do you want your seats to be split?(y/n)'))
                if split == 'y':
                    k=int(input('enter another row: '))
                    if k == 1:
                        print('invalid row')
                        k=int(input('enter new row: '))
                    elif k == 2:
                        if x-(15-filled1) > 15 - filled2:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[1,filled2 : filled2 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled2 = filled2 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 3:
                        if x-(15-filled1) > 15 - filled3:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[2,filled3 : filled3 + (x-(15-filled2))]=y
                            total = total + x                    
                            filled3 = filled3 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 4:
                        if x-(15-filled1) > 15-filled4:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[3,filled4 : filled4 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled4 = filled4 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 5:
                        if x-(15-filled1) > 15 - filled5:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[4,filled5 : filled5 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled5 = filled5 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 6:
                        if x-(15-filled1) > 15 -filled6:
                            print('no seats available: ')                                                
                        else:
                            L[0,filled1: ]=y
                            L[5,filled6 : filled6 + (x-(15-filled1))]=y
                            total = total + x                   
                            filled6 = filled6 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 7:
                        if x-(15-filled1) > 15- filled7:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[6,filled7 : filled7 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled7 = filled7 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k== 8:
                        if x-(15-filled1) > 15-filled8:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[7,filled8 : filled8 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled8 = filled8 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 9:
                        if x-(15-filled1) > 15-filled9:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[8,filled9 : filled9 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled9 = filled9 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k== 10:
                        if x-(15-filled1) > 15- filled10:
                            print('no seats available: ')                        
                        else:
                            L[0,filled1: ]=y
                            L[9,filled10 : filled10 + (x-(15-filled1))]=y
                            total = total + x
                            filled10 = filled10 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    print(L)
                else:
                    print()
        
    elif row == 2:
        if x <= 15 - filled2:
                L[1,filled2 : filled2+x]=y
                total = total + x
                filled2 = filled2 + x+1
                y+=1
                print(L)
        elif x > 15 - filled2:
            if filled2 >= 15 :
                print('no more seats available in this row')
            else:
                split=input(('Do you want your seats to be split?(y/n)'))
                if split == 'y':
                    k=int(input('enter another row: '))
                    if k == 2:
                        print('invalid row')
                        k=int(input('enter new row: '))
                    elif k == 1:
                        if x-(15-filled2) > 15 - filled1:
                            print('no seats available: ')                            
                        else:
                            L[1,filled2: ]=y
                            L[0,filled1 : filled1 + (x-(15-filled2))]=y
                            total = total + x                    
                            filled1 = filled1 + (x-(15-filled2)) + 1
                            y+=1
                            filled2 = filled2 + x + 1
                    elif k == 3:
                        if x-(15-filled1) > 15 - filled3:
                            print('no seats available: ')                            
                        else:
                            L[1,filled2: ]=y
                            L[2,filled3 : filled3 + (x-(15-filled2))]=y
                            total = total + x                    
                            filled3 = filled3 + (x-(15-filled2)) + 1
                            y+=1
                            filled2 = filled2 + x + 1
                    elif k == 4:
                        if x-(15-filled2) > 15-filled4:
                            print('no seats available: ')                            
                        else:
                            L[1,filled2: ]=y
                            L[3,filled4 : filled4 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled4 = filled4 + (x-(15-filled2)) + 1
                            y+=1
                            filled2 = filled2 + x + 1
                    elif k == 5:
                        if x-(15-filled2) > 15 - filled5:
                            print('no seats available: ')                            
                        else:
                            L[1,filled2: ]=y
                            L[4,filled5 : filled5 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled5 = filled5 + (x-(15-filled2)) + 1
                            y+=1
                            filled2 = filled2 + x + 1
                    elif k == 6:
                        if x-(15-filled2) > 15 -filled6:
                            print('no seats available: ')                                                
                        else:
                            L[1,filled2: ]=y
                            L[5,filled6 : filled6 + (x-(15-filled2))]=y
                            total = total + x                   
                            filled6 = filled6 + (x-(15-filled2)) + 1
                            y+=1
                            filled2 = filled2 + x + 1
                    elif k == 7:
                        if x-(15-filled2) > 15- filled7:
                            print('no seats available: ')                            
                        else:
                            L[1,filled2: ]=y
                            L[6,filled7 : filled7 + (x-(15-filled2))]=y
                            total = total + x                    
                            filled7 = filled7 + (x-(15-filled2)) + 1
                            y+=1
                            filled2 = filled2 + x + 1
                    elif k== 8:
                        if x-(15-filled2) > 15-filled8:
                            print('no seats available: ')                            
                        else:
                            L[1,filled2: ]=y
                            L[7,filled8 : filled8 + (x-(15-filled2))]=y
                            total = total + x                    
                            filled8 = filled8 + (x-(15-filled2)) + 1
                            y+=1
                            filled2 = filled2 + x + 1
                    elif k == 9:
                        if x-(15-filled2) > 15-filled9:
                            print('no seats available: ')                            
                        else:
                            L[1,filled2: ]=y
                            L[8,filled9 : filled9 + (x-(15-filled2))]=y
                            total = total + x                    
                            filled9 = filled9 + (x-(15-filled2)) + 1
                            y+=1
                            filled2 = filled2 + x + 1
                    elif k== 10:
                        if x-(15-filled2) > 15- filled10:
                            print('no seats available: ')                        
                        else:
                            L[1,filled2: ]=y
                            L[9,filled10 : filled10 + (x-(15-filled2))]=y
                            total = total + x
                            filled10 = filled10 + (x-(15-filled2)) + 1
                            y+=1
                            filled2 = filled2 + x + 1
                    print(L)
                else:
                    print()

    elif row == 3:  
        if x <= 15 - filled3:
            L[2,filled3  :filled3 + x]=y
            total = total + x                
            filled3 = filled3 + x+1
            y+=1
                
            print(L)
        elif x > 15 - filled3:
            if filled3 >= 15 :
                print('no more seats available in this row')
            else:
                split=input(('Do you want your seats to be split?(y/n)'))
                if split == 'y':
                    k=int(input('enter another row: '))
                    if k == 3:
                        print('invalid row')
                        k=int(input('enter new row: '))
                    elif k == 1:
                        if x-(15-filled3) > 15 - filled1:
                            print('no seats available: ')                            
                        else:
                            L[2,filled3: ]=y
                            L[0,filled1 : filled1 + (x-(15-filled3))]=y
                            total = total + x                    
                            filled1 = filled1 + (x-(15-filled3)) + 1
                            y+=1
                            filled3 = filled3 + x + 1
                    elif k == 2:
                        if x-(15-filled3) > 15 - filled2:
                            print('no seats available: ')                            
                        else:
                            L[2,filled3: ]=y
                            L[1,filled2 : filled2 + (x-(15-filled3))]=y
                            total = total + x                    
                            filled2 = filled2 + (x-(15-filled3)) + 1
                            y+=1
                            filled3 = filled3 + x + 1
                    elif k == 4:
                        if x-(15-filled3) > 15-filled4:
                            print('no seats available: ')                            
                        else:
                            L[2,filled3: ]=y
                            L[3,filled4 : filled4 + (x-(15-filled3))]=y
                            total = total + x                    
                            filled4 = filled4 + (x-(15-filled3)) + 1
                            y+=1
                            filled3 = filled3 + x + 1
                    elif k == 5:
                        if x-(15-filled3) > 15 - filled5:
                            print('no seats available: ')                            
                        else:
                            L[2,filled3: ]=y
                            L[4,filled5 : filled5 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled5 = filled5 + (x-(15-filled3)) + 1
                            y+=1
                            filled3 = filled3 + x + 1
                    elif k == 6:
                        if x-(15-filled3) > 15 -filled6:
                            print('no seats available: ')                                                
                        else:
                            L[2,filled3: ]=y
                            L[5,filled6 : filled6 + (x-(15-filled3))]=y
                            total = total + x                   
                            filled6 = filled6 + (x-(15-filled3)) + 1
                            y+=1
                            filled3 = filled3 + x + 1
                    elif k == 7:
                        if x-(15-filled3) > 15- filled7:
                            print('no seats available: ')                            
                        else:
                            L[2,filled3: ]=y
                            L[6,filled7 : filled7 + (x-(15-filled3))]=y
                            total = total + x                    
                            filled7 = filled7 + (x-(15-filled3)) + 1
                            y+=1
                            filled3 = filled3 + x + 1
                    elif k== 8:
                        if x-(15-filled3) > 15-filled8:
                            print('no seats available: ')                            
                        else:
                            L[2,filled3: ]=y
                            L[7,filled8 : filled8 + (x-(15-filled3))]=y
                            total = total + x                    
                            filled8 = filled8 + (x-(15-filled3)) + 1
                            y+=1
                            filled3 = filled3 + x + 1
                    elif k == 9:
                        if x-(15-filled3) > 15-filled9:
                            print('no seats available: ')                            
                        else:
                            L[2,filled3: ]=y
                            L[8,filled9 : filled9 + (x-(15-filled3))]=y
                            total = total + x                    
                            filled9 = filled9 + (x-(15-filled3)) + 1
                            y+=1
                            filled3 = filled3 + x + 1
                    elif k== 10:
                        if x-(15-filled3) > 15- filled10:
                            print('no seats available: ')                        
                        else:
                            L[2,filled3: ]=y
                            L[9,filled10 : filled10 + (x-(15-filled3))]=y
                            total = total + x
                            filled10 = filled10 + (x-(15-filled3)) + 1
                            y+=1
                            filled4 = filled3 + x + 1
                    print(L)
                else:
                    print()

                
    elif row == 4:
        if x <= 15 - filled4:
            L[3,filled4 :filled4+ x]=y
            total = total + x
            filled4 = filled4 + x+1
            y+=1
                    
            print(L)
        elif x > 15 - filled4:
            if filled4 >= 15 :
                print('no more seats available in this row')
            else:
                split=input(('Do you want your seats to be split?(y/n)'))
                if split == 'y':
                    k=int(input('enter another row: '))
                    if k == 4:
                        print('invalid row')
                        k=int(input('enter new row: '))
                    elif k == 2:
                        if x-(15-filled4) > 15 - filled2:
                            print('no seats available: ')                            
                        else:
                            L[3,filled4: ]=y
                            L[1,filled2 : filled2 + (x-(15-filled4))]=y
                            total = total + x                    
                            filled2 = filled2 + (x-(15-filled4)) + 1
                            y+=1
                            filled4 = filled4 + x + 1
                    elif k == 3:
                        if x-(15-filled4) > 15 - filled3:
                            print('no seats available: ')                            
                        else:
                            L[3,filled4: ]=y
                            L[2,filled3 : filled3 + (x-(15-filled4))]=y
                            total = total + x                    
                            filled3 = filled3 + (x-(15-filled4)) + 1
                            y+=1
                            filled4 = filled4 + x + 1
                    elif k == 1:
                        if x-(15-filled4) > 15-filled1:
                            print('no seats available: ')                            
                        else:
                            L[3,filled4: ]=y
                            L[0,filled1 : filled1 + (x-(15-filled4))]=y
                            total = total + x                    
                            filled1 = filled1 + (x-(15-filled4)) + 1
                            y+=1
                            filled4 = filled4 + x + 1
                    elif k == 5:
                        if x-(15-filled4) > 15 - filled5:
                            print('no seats available: ')                            
                        else:
                            L[3,filled4: ]=y
                            L[4,filled5 : filled5 + (x-(15-filled4))]=y
                            total = total + x                    
                            filled5 = filled5 + (x-(15-filled4)) + 1
                            y+=1
                            filled4 = filled4 + x + 1
                    elif k == 6:
                        if x-(15-filled4) > 15 -filled6:
                            print('no seats available: ')                                                
                        else:
                            L[3,filled4: ]=y
                            L[5,filled6 : filled6 + (x-(15-filled4))]=y
                            total = total + x                   
                            filled6 = filled6 + (x-(15-filled4)) + 1
                            y+=1
                            filled4 = filled4 + x + 1
                    elif k == 7:
                        if x-(15-filled4) > 15- filled7:
                            print('no seats available: ')                            
                        else:
                            L[3,filled4: ]=y
                            L[6,filled7 : filled7 + (x-(15-filled4))]=y
                            total = total + x                    
                            filled7 = filled7 + (x-(15-filled4)) + 1
                            y+=1
                            filled4 = filled4 + x + 1
                    elif k== 8:
                        if x-(15-filled4) > 15-filled8:
                            print('no seats available: ')                            
                        else:
                            L[3,filled4: ]=y
                            L[7,filled8 : filled8 + (x-(15-filled4))]=y
                            total = total + x                    
                            filled8 = filled8 + (x-(15-filled4)) + 1
                            y+=1
                            filled4 = filled4 + x + 1
                    elif k == 9:
                        if x-(15-filled4) > 15-filled9:
                            print('no seats available: ')                            
                        else:
                            L[3,filled4: ]=y
                            L[8,filled9 : filled9 + (x-(15-filled4))]=y
                            total = total + x                    
                            filled9 = filled9 + (x-(15-filled4)) + 1
                            y+=1
                            filled4 = filled4 + x + 1
                    elif k== 10:
                        if x-(15-filled4) > 15- filled10:
                            print('no seats available: ')                        
                        else:
                            L[3,filled4: ]=y
                            L[9,filled10 : filled10 + (x-(15-filled4))]=y
                            total = total + x
                            filled10 = filled10 + (x-(15-filled4)) + 1
                            y+=1
                            filled4 = filled4 + x + 1
                    print(L)
                else:
                    print()
    elif row == 5:
        if x <= 15 - filled5:
            L[4,filled5 :filled5+x]=y
            total = total + x
            filled5 = filled5 + x+1
            y+=1           
            print(L)
        elif x > 15 - filled1:
            if filled1 >= 15 :
                print('no more seats available in this row')
            else:
                split=input(('Do you want your seats to be split?(y/n)'))
                if split == 'y':
                    k=int(input('enter another row: '))
                    if k == 1:
                        print('invalid row')
                        k=int(input('enter new row: '))
                    elif k == 2:
                        if x-(15-filled1) > 15 - filled2:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[1,filled2 : filled2 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled2 = filled2 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 3:
                        if x-(15-filled1) > 15 - filled3:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[2,filled3 : filled3 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled3 = filled3 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 4:
                        if x-(15-filled1) > 15-filled4:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[3,filled4 : filled4 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled4 = filled4 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 5:
                        if x-(15-filled1) > 15 - filled5:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[4,filled5 : filled5 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled5 = filled5 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 6:
                        if x-(15-filled1) > 15 -filled6:
                            print('no seats available: ')                                                
                        else:
                            L[0,filled1: ]=y
                            L[5,filled6 : filled6 + (x-(15-filled1))]=y
                            total = total + x                   
                            filled6 = filled6 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 7:
                        if x-(15-filled1) > 15- filled7:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[6,filled7 : filled7 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled7 = filled7 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k== 8:
                        if x-(15-filled1) > 15-filled8:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[7,filled8 : filled8 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled8 = filled8 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 9:
                        if x-(15-filled1) > 15-filled9:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[8,filled9 : filled9 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled9 = filled9 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k== 10:
                        if x-(15-filled1) > 15- filled10:
                            print('no seats available: ')                        
                        else:
                            L[0,filled1: ]=y
                            L[9,filled10 : filled10 + (x-(15-filled1))]=y
                            total = total + x
                            filled10 = filled10 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    print(L)
                else:
                    print()     
    elif row ==  6:
        if x <= 15 - filled6:
            L[5,filled6 :filled6+x]=y
            total = total + x
            filled6 = filled6 + x+1
            y+=1
                          
            print(L)
        elif x > 15 - filled1:
            if filled1 >= 15 :
                print('no more seats available in this row')
            else:
                split=input(('Do you want your seats to be split?(y/n)'))
                if split == 'y':
                    k=int(input('enter another row: '))
                    if k == 1:
                        print('invalid row')
                        k=int(input('enter new row: '))
                    elif k == 2:
                        if x-(15-filled1) > 15 - filled2:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[1,filled2 : filled2 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled2 = filled2 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 3:
                        if x-(15-filled1) > 15 - filled3:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[2,filled3 : filled3 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled3 = filled3 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 4:
                        if x-(15-filled1) > 15-filled4:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[3,filled4 : filled4 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled4 = filled4 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 5:
                        if x-(15-filled1) > 15 - filled5:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[4,filled5 : filled5 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled5 = filled5 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 6:
                        if x-(15-filled1) > 15 -filled6:
                            print('no seats available: ')                                                
                        else:
                            L[0,filled1: ]=y
                            L[5,filled6 : filled6 + (x-(15-filled1))]=y
                            total = total + x                   
                            filled6 = filled6 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 7:
                        if x-(15-filled1) > 15- filled7:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[6,filled7 : filled7 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled7 = filled7 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k== 8:
                        if x-(15-filled1) > 15-filled8:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[7,filled8 : filled8 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled8 = filled8 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 9:
                        if x-(15-filled1) > 15-filled9:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[8,filled9 : filled9 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled9 = filled9 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k== 10:
                        if x-(15-filled1) > 15- filled10:
                            print('no seats available: ')                        
                        else:
                            L[0,filled1: ]=y
                            L[9,filled10 : filled10 + (x-(15-filled1))]=y
                            total = total + x
                            filled10 = filled10 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    print(L)
                else:
                    print()    
    elif row == 7:
        if x <= 15 - filled7:
            L[6,filled7:filled7+x]=y
            total = total + x
            filled7 = filled7 + x+1
            y+=1
                               
            print(L)
       elif x > 15 - filled1:
            if filled1 >= 15 :
                print('no more seats available in this row')
            else:
                split=input(('Do you want your seats to be split?(y/n)'))
                if split == 'y':
                    k=int(input('enter another row: '))
                    if k == 1:
                        print('invalid row')
                        k=int(input('enter new row: '))
                    elif k == 2:
                        if x-(15-filled1) > 15 - filled2:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[1,filled2 : filled2 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled2 = filled2 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 3:
                        if x-(15-filled1) > 15 - filled3:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[2,filled3 : filled3 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled3 = filled3 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 4:
                        if x-(15-filled1) > 15-filled4:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[3,filled4 : filled4 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled4 = filled4 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 5:
                        if x-(15-filled1) > 15 - filled5:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[4,filled5 : filled5 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled5 = filled5 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 6:
                        if x-(15-filled1) > 15 -filled6:
                            print('no seats available: ')                                                
                        else:
                            L[0,filled1: ]=y
                            L[5,filled6 : filled6 + (x-(15-filled1))]=y
                            total = total + x                   
                            filled6 = filled6 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 7:
                        if x-(15-filled1) > 15- filled7:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[6,filled7 : filled7 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled7 = filled7 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k== 8:
                        if x-(15-filled1) > 15-filled8:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[7,filled8 : filled8 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled8 = filled8 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 9:
                        if x-(15-filled1) > 15-filled9:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[8,filled9 : filled9 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled9 = filled9 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k== 10:
                        if x-(15-filled1) > 15- filled10:
                            print('no seats available: ')                        
                        else:
                            L[0,filled1: ]=y
                            L[9,filled10 : filled10 + (x-(15-filled1))]=y
                            total = total + x
                            filled10 = filled10 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    print(L)
                else:
                    print()
    elif row == 8:
        if x <= 15 - filled8:
            L[7,filled8:filled8+x]=y
            total = total + x
            filled8 = filled8 + x+1
            y+=1
                               
            print(L)
elif x > 15 - filled1:
            if filled1 >= 15 :
                print('no more seats available in this row')
            else:
                split=input(('Do you want your seats to be split?(y/n)'))
                if split == 'y':
                    k=int(input('enter another row: '))
                    if k == 1:
                        print('invalid row')
                        k=int(input('enter new row: '))
                    elif k == 2:
                        if x-(15-filled1) > 15 - filled2:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[1,filled2 : filled2 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled2 = filled2 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 3:
                        if x-(15-filled1) > 15 - filled3:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[2,filled3 : filled3 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled3 = filled3 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 4:
                        if x-(15-filled1) > 15-filled4:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[3,filled4 : filled4 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled4 = filled4 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 5:
                        if x-(15-filled1) > 15 - filled5:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[4,filled5 : filled5 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled5 = filled5 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 6:
                        if x-(15-filled1) > 15 -filled6:
                            print('no seats available: ')                                                
                        else:
                            L[0,filled1: ]=y
                            L[5,filled6 : filled6 + (x-(15-filled1))]=y
                            total = total + x                   
                            filled6 = filled6 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 7:
                        if x-(15-filled1) > 15- filled7:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[6,filled7 : filled7 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled7 = filled7 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k== 8:
                        if x-(15-filled1) > 15-filled8:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[7,filled8 : filled8 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled8 = filled8 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 9:
                        if x-(15-filled1) > 15-filled9:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[8,filled9 : filled9 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled9 = filled9 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k== 10:
                        if x-(15-filled1) > 15- filled10:
                            print('no seats available: ')                        
                        else:
                            L[0,filled1: ]=y
                            L[9,filled10 : filled10 + (x-(15-filled1))]=y
                            total = total + x
                            filled10 = filled10 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    print(L)
                else:
                    print()
    elif row == 9:
        if x <= 15 - filled9:
            L[8,filled9:filled9+x]=y
            total = total + x
            filled9 = filled9 + x+1
            y+=1
                               
            print(L)
        elif x > 15 - filled1:
            if filled1 >= 15 :
                print('no more seats available in this row')
            else:
                split=input(('Do you want your seats to be split?(y/n)'))
                if split == 'y':
                    k=int(input('enter another row: '))
                    if k == 1:
                        print('invalid row')
                        k=int(input('enter new row: '))
                    elif k == 2:
                        if x-(15-filled1) > 15 - filled2:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[1,filled2 : filled2 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled2 = filled2 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 3:
                        if x-(15-filled1) > 15 - filled3:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[2,filled3 : filled3 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled3 = filled3 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 4:
                        if x-(15-filled1) > 15-filled4:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[3,filled4 : filled4 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled4 = filled4 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 5:
                        if x-(15-filled1) > 15 - filled5:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[4,filled5 : filled5 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled5 = filled5 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 6:
                        if x-(15-filled1) > 15 -filled6:
                            print('no seats available: ')                                                
                        else:
                            L[0,filled1: ]=y
                            L[5,filled6 : filled6 + (x-(15-filled1))]=y
                            total = total + x                   
                            filled6 = filled6 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 7:
                        if x-(15-filled1) > 15- filled7:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[6,filled7 : filled7 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled7 = filled7 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k== 8:
                        if x-(15-filled1) > 15-filled8:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[7,filled8 : filled8 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled8 = filled8 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 9:
                        if x-(15-filled1) > 15-filled9:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[8,filled9 : filled9 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled9 = filled9 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k== 10:
                        if x-(15-filled1) > 15- filled10:
                            print('no seats available: ')                        
                        else:
                            L[0,filled1: ]=y
                            L[9,filled10 : filled10 + (x-(15-filled1))]=y
                            total = total + x
                            filled10 = filled10 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    print(L)
                else:
                    print()
    elif row == 10:
        if x <= 15 - filled10:
            L[9,filled10:filled10+x]=y
            total = total + x
            filled10 = filled10 + x+1
            y+=1
                               
            print(L)
        elif x > 15 - filled1:
            if filled1 >= 15 :
                print('no more seats available in this row')
            else:
                split=input(('Do you want your seats to be split?(y/n)'))
                if split == 'y':
                    k=int(input('enter another row: '))
                    if k == 1:
                        print('invalid row')
                        k=int(input('enter new row: '))
                    elif k == 2:
                        if x-(15-filled1) > 15 - filled2:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[1,filled2 : filled2 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled2 = filled2 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 3:
                        if x-(15-filled1) > 15 - filled3:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[2,filled3 : filled3 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled3 = filled3 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 4:
                        if x-(15-filled1) > 15-filled4:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[3,filled4 : filled4 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled4 = filled4 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 5:
                        if x-(15-filled1) > 15 - filled5:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[4,filled5 : filled5 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled5 = filled5 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 6:
                        if x-(15-filled1) > 15 -filled6:
                            print('no seats available: ')                                                
                        else:
                            L[0,filled1: ]=y
                            L[5,filled6 : filled6 + (x-(15-filled1))]=y
                            total = total + x                   
                            filled6 = filled6 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 7:
                        if x-(15-filled1) > 15- filled7:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[6,filled7 : filled7 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled7 = filled7 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k== 8:
                        if x-(15-filled1) > 15-filled8:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[7,filled8 : filled8 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled8 = filled8 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k == 9:
                        if x-(15-filled1) > 15-filled9:
                            print('no seats available: ')                            
                        else:
                            L[0,filled1: ]=y
                            L[8,filled9 : filled9 + (x-(15-filled1))]=y
                            total = total + x                    
                            filled9 = filled9 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    elif k== 10:
                        if x-(15-filled1) > 15- filled10:
                            print('no seats available: ')                        
                        else:
                            L[0,filled1: ]=y
                            L[9,filled10 : filled10 + (x-(15-filled1))]=y
                            total = total + x
                            filled10 = filled10 + (x-(15-filled1)) + 1
                            y+=1
                            filled1 = filled1 + x + 1
                    print(L)
                else:
                    print()
    else:
        print('invalid row number(1-10)')
                                
                    
    


        
        