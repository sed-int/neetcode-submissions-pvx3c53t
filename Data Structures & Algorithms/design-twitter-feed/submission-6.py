class Twitter:

    def __init__(self):
        self.tweet = {}      # key = userId, value = [tweetId, timestamp]
        self.follows = {}    # key = follower, value = followee
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweet:
            self.tweet[userId] = []
        if tweetId in self.tweet[userId]:
            return
        self.tweet[userId].append([self.timestamp, tweetId])
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        news = []
        if userId in self.tweet:
            news += self.tweet[userId]
        if userId in self.follows:
            for followeeId in self.follows[userId]:
                if followeeId not in self.tweet:
                    continue
                news += self.tweet[followeeId]
        news.sort(reverse=True)
        res = [v[1] for v in news]
        if len(res) > 10:
            return res[:10]
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = []
        if followeeId in self.follows[followerId] or followeeId == followerId:
            return
        self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            return
        if followeeId not in self.follows[followerId]:
            return
        self.follows[followerId].remove(followeeId)