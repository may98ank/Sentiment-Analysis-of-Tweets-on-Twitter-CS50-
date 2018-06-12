import nltk

class Analyzer():
    """Implements sentiment analysis."""
    pos = set()
    neg = set()

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""

        with open(positives) as lines:
            for line in lines:
                if not line.startswith(";"):
                    self.pos.add(line.strip())

        with open(negatives) as lines:
            for line in lines:
                if not line.startswith(";"):
                    self.neg.add(line.strip())

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        tokenizer = nltk.tokenize.TweetTokenizer()
        ls = tokenizer.tokenize(text)

        ans = 0

        for word in ls:
            if word.lower() in self.pos:
                ans += 1
            elif word.lower() in self.neg:
                ans -= 1;
            # print(word in self.pos)
        # TODO
        return ans
