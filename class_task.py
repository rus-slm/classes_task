
class CountVectorizer:
    def __init__(self):
        pass

    def fit_transform(self, corpus):
        self.corpus = corpus
        self._bag_of_words = []
        for elem in range(len(self.corpus)):
            self._bag_of_words.append(self.corpus[elem].split())
        self._bag_of_words = [y.lower() for x in self._bag_of_words for y in x]
        self._bag_of_words = sorted(list(set(self._bag_of_words)))
        matrix = []
        for phrase in self.corpus:
            phrase = phrase.split()
            matrix_line = []
            new_phrase = [word.lower() for word in phrase]
            for point in self._bag_of_words:
                matrix_line.append(new_phrase.count(point))
            matrix.append(matrix_line)
        return matrix

    def get_feature_name(self):
        return self._bag_of_words


