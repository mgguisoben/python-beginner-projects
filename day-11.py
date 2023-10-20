import random


def deal_card(hand, cards):
    if len(hand) == 0:
        for _ in range(2):
            hand.append(cards[0])
            cards.pop(0)
        return hand
    else:
        card = cards[0]
        hand.append(card)
        cards.pop(0)
        return hand


def dealer_ai(hand, cards):
    hand = deal_card(hand, cards)
    count = sum(hand)
    if 1 in hand and 10 in hand and len(hand) == 2:
        hand[hand.index(1)] = 11
        return hand
    else:
        while count <= 19:
            hand = deal_card(hand, cards)
            count = sum(hand)
        return hand


def check_winner(player, com):
    player_sum = sum(player)
    com_sum = sum(com)

    if player_sum == com_sum:
        print("Draw")
    elif player_sum == 21 or abs(player_sum - 21) < abs(com_sum - 21):
        print("You WIN")
    else:
        print("You LOST")


deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
random.shuffle(deck)

game = True
while game:

    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    # Check if player wants to start a game, deck is reset and shuffled if 'n'
    if play_game == 'n':
        deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
        random.shuffle(deck)
        game = False

    # Initialize player and dealer with empty hand
    elif play_game == 'y':
        deal = True
        player_hand = []
        dealer_hand = []

        # Run Dealer AI
        dealer_hand = dealer_ai(dealer_hand, deck)

        while deal:
            player_hand = deal_card(player_hand, deck)

            print(f"Your cards: {player_hand}")
            print(f"Dealer's upcard: [{dealer_hand[0]}]")

            deal_again = input("Type 'y' to get another card, type 'n' to pass: ")

            if deal_again == 'n':
                print(f"Your final cards: {player_hand}")
                print(f"Dealer's final cards: {dealer_hand}")
                check_winner(player_hand, dealer_hand)
                deal = False

            elif deal_again == 'y':
                continue
