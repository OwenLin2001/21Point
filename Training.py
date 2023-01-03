import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Create a deck
player_number = input("How many player?\n")
player_number = int(player_number)
Suit = np.array(["Club", "Diamond", "Heart", "Spade"])
Rank = np.array(["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])
Deck = []
for i in np.arange(4):
    for j in np.arange(13):
        Deck.append(Suit[i] + " " + Rank[j])


# initialize empty hand for each player
# eg. [ [], [] , [] ]
Hand = []
for i in np.arange(player_number):
    Hand.append([])


# Draw first two cards for everyone
card_left = 52
for round in range(2):
    for i in np.arange(player_number):
        draw = np.random.randint(card_left)
        Hand[i].append(Deck[draw])       
        Deck.pop(draw)
        card_left -= 1


# initialize decision for each player
# eg. [ [], [] , [] ]
decision = []
for i in np.arange(player_number):
    decision.append(["Yes"])


# Finalize everyone's hand
for round in range(4):
    for t in range(player_number):
        print(Hand[t])
        if decision[t][-1] == "Yes":
            d = input("Player"+ str(t) +": Draw another card? Yes/No\n")
            decision[t].append(d)
            if d == "Yes":
                draw = np.random.randint(card_left)
                Hand[t].append(Deck[draw])
                Deck.pop(draw)
                card_left -= 1
                
                TotalPoint = 0
                for card in Hand[t]:
                    if card[-1] == "J" or  card[-1] == "Q" or card[-1] == "K":
                        TotalPoint += 10
                    elif card[-1] == "A":
                        TotalPoint += 1
                    else:
                        TotalPoint += str(card[-1])
                if TotalPoint > 21:
                    decision[t].append("boom")
                    print("Point exceed 21")


print(Hand)

# 1 Tic Tac Toe
# 21points, texas hold'em
# 2 2048
# 3 matrix up down

# machine learning- regression 庄家
