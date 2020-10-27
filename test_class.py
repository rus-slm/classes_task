if __name__ == '__main__':
    import class_task as ct


corpus = ['Crock Pot Pasta Never boil pasta again',
'Pasta Pomodoro Fresh ingredients Parmesan to taste']


vectorizer = ct.CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_name())
print(count_matrix)