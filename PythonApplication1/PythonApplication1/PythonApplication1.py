#7η Άσκηση.

import random

def drawtictactoe(table):
# Η συνάρτηση τυπώνει τις γραμμές και στήλες της τρίλιζας, όπως αυτές δίνονται από τις παραμέτρους.
    print('   |   |')

    print(' ' + table[7] + ' | ' + table[8] + ' | ' + table[9])

    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + table[4] + ' | ' + table[5] + ' | ' + table[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + table[1] + ' | ' + table[2] + ' | ' + table[3])
    print('   |   |')

def choosechar():
# Η συνάρτηση επιτρέπει στον παίχτη να αποφασίσει αν θα είναι X ή O.
    character = ''
    while not (character == 'X' or character == 'O'):
        print('Do you want to be X or O?')
        character = input().upper()
    if character == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whostarts():
# Η συνάρτηση επιλέγει τυχαία ποιος θα παίξει πρώτος με την χρήση της βιβλιοθήκης random.
    if random.randint(0, 1) == 0:
        return 'computer begins'
    else:
        return 'player begins'

def replay():
# Η συνάρτηση ρωτάει τον παίχτη αν επιθυμεί να ξαναπαίξει μετά το τέλος κάθε παρτίδας.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def playermove(table, character, move):
# Η συνάρτηση καταχωρεί την κίνηση του παίχτη.
    table[move] = character

def whowins(table, character):
# Η συνάρτηση επιστρέφει αν ο παίχτης κέρδισε.
    return ((table[7] == character and table[8] == character and table[9] == character) or 
    (table[4] == character and table[5] == character and table[6] == character) or 
    (table[1] == character and table[2] == character and table[3] == character) or 
    (table[7] == character and table[4] == character and table[1] == character) or 
    (table[8] == character and table[5] == character and table[2] == character) or 
    (table[9] == character and table[6] == character and table[3] == character) or 
    (table[7] == character and table[5] == character and table[3] == character) or 
    (table[9] == character and table[5] == character and table[1] == character)) 

def tablecopy(table):
# Η συνάρτηση φτιάχνει μια αντιγραφή του table, προκειμένου να μπορούν να γίνουν προσωρινές επεξεργασίες σε αυτή, χωρίς να αλλάξει ο αρχικός πίνακας.
    dupetable = []
    for i in table:
        dupetable.append(i)
    return dupetable

def istherespace(table, move):
# Η συνάτηση επιστρέφει αν η κίνηση που επέλεξε ο παίχτης είναι διαθέσιμη.
    return table[move] == ' '

def getPlayerMove(table):
# Η συνάρτηση επιτρέπει στον παίχτη να πληκτρολογήσει την κίνησή του και ελέγχει αν αυτή είναι έγκυρη.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not istherespace(table, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def randommove(table, movesList):
# Η συνάρτηση  επιστρέφει πιθανές θέσεις για κινήσεις, αν αυτές υπάρχουν.
    possmoves = []
    for i in movesList:
        if istherespace(table, i):
            possmoves.append(i)
    if len(possmoves) != 0:
        return random.choice(possmoves)
    else:
        return None

def getComputerMove(table, computercharacter):
# Η συνάρτηση επιλέγει που θα κινηθεί ο υπολογιστής και επιστρέφει την κίνηση αυτή.
    if computercharacter == 'X':
        playercharacter = 'O'
    else:
        playercharacter = 'X'
# Ελέγχεται αν μπορεί ο υπολογιστής να κερδίσει στην επόμενη κίνηση.
    for i in range(1, 10):
        copy = tablecopy(table)
        if istherespace(copy, i):
            playermove(copy, computercharacter, i)
            if whowins(copy, computercharacter):
                return i
# Ελέγχεται αν ο παίχτης κερδίζει στην επομενή του κίνηση κι αν αυτό συμβαίνει, τον σταματά.
    for i in range(1, 10):
        copy = tablecopy(table)
        if istherespace(copy, i):
            playermove(copy, playercharacter, i)
            if whowins(copy, playercharacter):
                return i
# Ελέγχεται αν μία από τις γωνίες είναι διαθέσιμη.
    move = randommove(table, [1, 3, 7, 9])
    if move != None:
        return move
# Ελέγχεται αν το κέντρο είναι διαθέσιμο.
    if istherespace(table, 5):
        return 5
# Ελέγχεται αν οι πλευρές είναι διαθέσιμες.
    return randommove(table, [2, 4, 6, 8])

def nomoremoves(table):
# Επιστρέφει αν έχει καλυφθεί όλος ο πίνακας ή οχι.
    for i in range(1, 10):
        if istherespace(table, i):
            return False
    return True


# Αρχή της εκτέλεσης του προγράματος.
print('Welcome to Tic Tac Toe!')
while True:
# Αρχικοποιείται ο πίνακας με κενά.
    thetable = [' '] * 10
    playercharacter, computercharacter = choosechar()
    turn = whostarts()
    print('The ' + turn + ' will go first.')
    gamestarted = True
    while gamestarted:
        if turn == 'player':
# Η σειρά του παίχτη να κάνει την κινησή του.
            drawtictactoe(thetable)
            move = getPlayerMove(thetable)
            playermove(thetable, playercharacter, move)
            if whowins(thetable, playercharacter):
                drawtictactoe(thetable)
                print('Hooray! You have won the game!')
                gamestarted = False
            else:
                if nomoremoves(thetable):
                    drawtictactoe(thetable)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
# Η σειρά του υποογιστή να κάνει την κινησή του.
            move = getComputerMove(thetable, computercharacter)
            playermove(thetable, computercharacter, move)
            if whowins(thetable, computercharacter):
                drawtictactoe(thetable)
                print('The computer has beaten you! You lose.')
                gamestarted = False
            else:
                if nomoremoves(thetable):
                    drawtictactoe(thetable)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    if not replay():
        break
# Τέλος του προγράμματος.