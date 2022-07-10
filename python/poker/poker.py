rank_dict = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "0": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14
}

ranks = "234567890JQKA"

suits = "CDHS"

def straight_flush(hand):
    hand_sort = sorted(hand, key=lambda x: rank_dict[x[0]])
    hand_seq = "".join(map(lambda x: x[0], hand_sort))
    hand_seq_true = hand_seq if hand_seq in ranks else None
    num_suit = len(set(list(zip(*hand))[1]))
    if hand_seq_true and num_suit == 1:
        return hand
    
def four_of_a_kind(hand):
    ranks_ = list(set(list(zip(*hand))[0]))
    comb = [list(zip(*hand))[0].count(i) for i in ranks_]
    if sorted(comb) == [1, 4]:
        return hand
    
def full_house(hand):
    ranks_ = list(set(list(zip(*hand))[0]))
    comb = [list(zip(*hand))[0].count(i) for i in ranks_]
    if sorted(comb) == [2, 3]:
        return hand
    
def flush(hand):
    num_suit = len(set(list(zip(*hand))[1]))
    if num_suit == 1:
        return hand
    
def straight(hand):
    hand_sort = sorted(hand, key=lambda x: rank_dict[x[0]])
    hand_seq = "".join(map(lambda x: x[0], hand_sort))
    hand_seq_true = hand_seq if hand_seq in ranks else None
    if hand_seq_true:
        return hand
    
def straight_a(hand):
    hand_sort = sorted(hand, key=lambda x: rank_dict[x[0]])
    hand_seq = "".join(map(lambda x: x[0], hand_sort))
    hand_seq_true = hand_seq if hand_seq[:-1] in ranks and hand_seq[-1] == "A" else None
    if hand_seq_true:
        return hand
    
def three_of_a_kind(hand):
    ranks_ = list(set(list(zip(*hand))[0]))
    comb = [list(zip(*hand))[0].count(i) for i in ranks_]
    if sorted(comb) == [1, 1, 3]:
        return hand
    
def two_pair(hand):
    ranks_ = list(set(list(zip(*hand))[0]))
    comb = [list(zip(*hand))[0].count(i) for i in ranks_]
    if sorted(comb) == [1, 2, 2]:
        return hand
    
def one_pair(hand):
    ranks_ = list(set(list(zip(*hand))[0]))
    comb = [list(zip(*hand))[0].count(i) for i in ranks_]
    if sorted(comb) == [1, 1, 1, 2]:
        return hand
    
categories = [straight_flush, four_of_a_kind, full_house, flush, straight, straight_a, three_of_a_kind, two_pair, one_pair]

def max_card(hands):
    for i in range(5):
        hands_sort = [sorted(hand, key=lambda x: ({item: list(zip(*hand))[0].count(item) for item in list(zip(*hand))[0]}[x[0]], rank_dict[x[0]]), reverse=True) for hand in hands]
        high_card = max([hand[i] for hand in hands_sort], key=lambda x: rank_dict[x[0]])[0]
        hands = list(filter(lambda hand: high_card == sorted(hand, key=lambda x: ({item: list(zip(*hand))[0].count(item) for item in list(zip(*hand))[0]}[x[0]], rank_dict[x[0]]), reverse=True)[i][0], hands))
    hands = [["1" + item if item[0] == "0" else item for item in hand] for hand in hands]
    return [" ".join(hand) for hand in hands]
    
def best_hands(hands):
    hands = [[item.lstrip("1") for item in hand.split()] for hand in hands]
    for category in categories:
        result = []
        for hand in hands:
            if category(hand):
                result.append(hand)
        if result:
            return max_card(result)
    return max_card(hands)


