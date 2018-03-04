
import sys

cards = []
tc = int(input())

def cardsort(c):    
    if c == 'A':        
        return 14
    elif c == 'K':
        return 13
    elif c == 'Q':
        return 12
    elif c == 'J':
        return 11
    else:        
        return int(c)

while tc:
    tc -= 1
    players = int(input())
    cards = [raw_input().split() for x in range(0, players)]    
    noWin = True
    currentPlayers = range(players)    
    totalCards = sum(int(c.pop(0)) for c in cards)    
    poolIndex = [0] * players

    while noWin:
        currentHands = []
        
        for p in currentPlayers:
            if len(cards[p]) > poolIndex[p]:
                currentHands.append((p, cards[p][poolIndex[p]]))
            else:
                # someone has no cards, we haz a winner
                noWin = False
                break

        if (noWin == False):
            cardCount = [len(c) for c in cards]
            mostCardPlayer = []
            mostCards = max(cardCount)
            for p in currentPlayers:
                if cardCount[p] == mostCards:
                    mostCardPlayer.append(p)
            if len(mostCardPlayer) == 1:
                print mostCardPlayer[0]+1
            else:
                print "No Winner"
            continue

        #print ">",["".join(c) for c in cards]
        #print ">>", poolIndex
        #print ">>>",currentHands
        #who wins this hand, or go to war
        currentHands.sort(key = lambda x:cardsort(x[1]), reverse=True)
        currentPlayers = []
        for hand in currentHands:
            if currentHands[0][1] == hand[1]:
                currentPlayers.append(hand[0])

        #winner takes cards
        if len(currentPlayers) == 1:
            winner = currentPlayers[0]
            for p in range(players):
                cards[winner].extend(cards[p][:poolIndex[p]+1])
                cards[p] = cards[p][poolIndex[p]+1:]
            poolIndex = [0] * players
            currentPlayers = range(players)
            
            #print ["".join(c) for c in cards]
            #print "%d Takes cards\n" %(winner + 1)

            #see if there is one person with all the cards
            if len(cards[winner]) == totalCards:
                #print "Winner is %d"%(winner+1)
                print (winner+1)
                noWin = False
            
            continue        

        #no winner
        if len(currentPlayers) == 0:
            noWin = False
            print "No Winner"

        # war!
        for p in currentPlayers:
            poolIndex[p] += 2

        #print "WAR!\n"
