import random
import math
from operator import itemgetter


class UserBasedCF:

    def __init__(self):
        self.n_sim_user = 20
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

    def calc_user_sim(self):
        # key = movieID, value = list of userIDs who have seen this movie
        # build movie-user table
        movie_user = {}
        for user, movies in self.trainSet.items():
            for movie in movies:
                if movie not in movie_user:
                    movie_user[movie] = set()
                movie_user[movie].add(user)

        self.movie_count = len(movie_user)

        # build user co-rated movies matrix
        for movie, users in movie_user.items():
            for u in users:
                for v in users:
                    if u == v:
                        continue
                    self.user_sim_matrix.setdefault(u, {})
                    self.user_sim_matrix[u].setdefault(v, 0)
                    self.user_sim_matrix[u][v] += 1

        # calculate similarity
        for u, related_users in self.user_sim_matrix.items():
            for v, count in related_users.items():
                self.user_sim_matrix[u][v] = count / math.sqrt(len(self.trainSet[u]) * len(self.trainSet[v]))

    def recommend(self, user):
        K = self.n_sim_user
        N = self.n_rec_movie
        rank = {}
        watched_movies = self.trainSet[user]

        # v = similar user, wuv = similar factor
        for v, wuv in sorted(self.user_sim_matrix[user].items(), key=itemgetter(1), reverse=True)[0:K]:
            for movie in self.trainSet[v]:
                if movie in watched_movies:
                    continue
                rank.setdefault(movie, 0)
                rank[movie] += wuv
        return sorted(rank.items(), key=itemgetter(1), reverse=True)[0:N]

    # evaluation


if __name__ == '__main__':
    rating_file = '../ml-latest-small/ratings.csv'
    userCF = UserBasedCF()
    userCF.get_dataset(rating_file)
    userCF.calc_user_sim()

