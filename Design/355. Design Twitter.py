from collections import defaultdict
from typing import List


class Post:

    def __init__(self, tweetId: int, timestamp: int):
        """
        Initialize your data structure here.
        """
        self.tweetId = tweetId
        self.timestamp = timestamp


class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.post = defaultdict(list)
        self.follower = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if len(self.post[userId]) == 10:
            self.post[userId].pop(0)
        self.post[userId] += [Post(tweetId, self.timestamp)]
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        feeds = []

        users = [userId] + list(self.follower[userId])

        for user in users:
            feeds += self.post[user]

        feeds = sorted(feeds, key=lambda x: x.timestamp, reverse=True)

        return map(lambda feed: feed.tweetId, feeds[:10])

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            self.follower[followerId].add(followeeId)
            # self.followee[followeeId] += [followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.follower[followerId] and followerId != followeeId:
            self.follower[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)