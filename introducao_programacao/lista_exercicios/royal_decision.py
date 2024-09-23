class RoyalDecision:
    def __init__(self, scores):
        self.scores = scores

    def determine_winner(self):
        averages = [sum(score) / len(score) for score in self.scores]
        highest_average = max(averages)
        candidates = [i for i, avg in enumerate(averages) if avg == highest_average]
        if len(candidates) == 1:
            return f"Candidate {candidates[0] + 1} is the winner"
        else:
            return "There is a tie among candidates"
if __name__ == "__main__":
    scores = [[7, 8, 9], [6, 8, 7], [9, 8, 7]]
    decision = RoyalDecision(scores)
    print(decision.determine_winner())
