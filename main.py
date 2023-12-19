used_list = []
turn = 1

list = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]
is_playing = True
 
 
while is_playing == True:
    for i in range(0, len(list)):
        if i+1 == 3 or i+1 == 6:
            print(list[i])
        else:
            print(list[i], end=" ")
    print("\n")

    if list[1-1] == "X" and list[2-1] == "X" and list[3-1] == "X":
        is_playing = False
        print("\nKonec výhra: křížek")
    
    elif list[4-1] == "X" and list[5-1] == "X" and list[6-1] == "X":
        is_playing = False
        print("\nKonec výhra: křížek")

    elif list[7-1] == "X" and list[8-1] == "X" and list[9-1] == "X":
        is_playing = False
        print("\nKonec výhra: křížek")
    
    elif list[1-1] == "X" and list[4-1] == "X" and list[7-1] == "X":
        is_playing = False
        print("\nKonec výhra: křížek")
    
    elif list[2-1] == "X" and list[5-1] == "X" and list[8-1] == "X":
        is_playing = False
        print("\nKonec výhra: křížek")

    elif list[3-1] == "X" and list[6-1] == "X" and list[9-1] == "X":
        is_playing = False
        print("\nKonec výhra: křížek")

    elif list[1-1] == "X" and list[5-1] == "X" and list[9-1] == "X":
        is_playing = False
        print("\nKonec výhra: křížek")

    elif list[3-1] == "X" and list[5-1] == "X" and list[7-1] == "X":
        is_playing = False
        print("\nKonec výhra: křížek")

    

    if list[1-1] == "O" and list[2-1] == "O" and list[3-1] == "O":
        is_playing = False
        print("\nKonec výhra: křížek")
    
    elif list[4-1] == "O" and list[5-1] == "O" and list[6-1] == "O":
        is_playing = False
        print("\nKonec výhra: křížek")

    elif list[7-1] == "O" and list[8-1] == "O" and list[9-1] == "O":
        is_playing = False
        print("\nKonec výhra: křížek")
    
    elif list[1-1] == "O" and list[4-1] == "O" and list[7-1] == "O":
        is_playing = False
        print("\nKonec výhra: křížek")
    
    elif list[2-1] == "O" and list[5-1] == "O" and list[8-1] == "O":
        is_playing = False
        print("\nKonec výhra: křížek")

    elif list[3-1] == "O" and list[6-1] == "O" and list[9-1] == "O":
        is_playing = False
        print("\nKonec výhra: křížek")

    elif list[1-1] == "O" and list[5-1] == "O" and list[9-1] == "O":
        is_playing = False
        print("\nKonec výhra: křížek")

    elif list[3-1] == "O" and list[5-1] == "O" and list[7-1] == "O":
        is_playing = False
        print("\nKonec výhra: křížek")


    if turn == 1:
        sign = int(input("1. Hráč kam si přejete dát pole? "))
 
        if sign > 0 and sign <= 9 and sign is not str and sign not in used_list:
            list[sign-1] = "X"
            used_list.append(sign)
            print(used_list)
 
        turn = 2
 
 
    elif turn == 2:
 
        sign = int(input("2. Hráč kam si přejete dát pole? "))
 
        if sign > 0 and sign <= 9 and sign is not str and sign not in used_list:
            list[sign-1] = "O"
            used_list.append(sign)
            print(used_list)
 
        turn = 1