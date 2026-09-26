class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        freq = defaultdict(int)
        for num in hand:
            freq[num] += 1
        hand = sorted(hand)
  
        for card in hand:
            if freq[card] == 0:
                continue
            else:
                for val in range(card, card+groupSize):
                    if freq[val] == 0:
                        return False
                    else:
                        freq[val] -= 1
        return True
        