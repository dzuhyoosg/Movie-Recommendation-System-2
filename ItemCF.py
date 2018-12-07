import random
import math
from operator import itemgetter


class ItemBasedCF:

    def __init__(self):
        self.n_sim_movie = 20
        self.n_rec_movie = 10

        # divide data set into training set and test set
        self.trainSet = {}
        self.testSet = {}

        # user similarity matrix
        self.user_sim_matrix = {}
        self.movie_count = 0

    def get_dataset(self, filename, pivot=0.75):
        train_set_len = 0
        test_set_len = 0
        for line in self.load_file(filename):
            user, movie, rating, timestamp = line.split(',')
            if random.random() < pivot:
                self.trainSet.setdefault(user, {})
                self.trainSet[user][movie] = rating
                train_set_len += 1
            else:
                self.testSet.setdefault(user, {})
                self.testSet[user][movie] = rating
                test_set_len += 1
        print('Train Set = %s' % train_set_len)
        print('Test Set = %s' % test_set_len)

    def load_file(self, filename):
        with open(filename, 'r') as f:
            for i, line in enumerate(f):
                if i == 0:  # delete the first line of the file, which is title
                    continue
                yield line.strip('\r\n')
        print('File %s load successfully!' % filename)