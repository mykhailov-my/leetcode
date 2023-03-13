
import heapq


class Twitter:
    """
    Status -> Solved by myself

    Tags -> Heap, set, hash

    __init__
    Time complexity -> O(1)
    Space complexity -> O(1)

    postTweet
    1. append tweet to user list of tweets
        1.1 tweet is tuple of time -> used to place in heap, postid - result, author id - used to remove tweets from feed
    2. for each follower add tweet to their feed (it's a heap)
    3. increment time
    Time complexity -> O(N)
    Space complexity -> O(N)
    where N - amount of followers

    follow
    1. check if we not following ourselfs
    2. check if user already follow that person
    3. assign user to followers, and and followee to his list (set)
    4. place all tweets from folowee to users feed (heap push)
    Time complexity -> O(T log F)
    Space complexity -> O(T)
    where T - amount of tweets from followee, F size of follower feed

    unfollow
    1. check if we not unfollowing ourselves, and this ids have in realtions
    2. update feed
        2.1 iterate by feed to find post of folowee
        2.2 then move i-th element to end (place end element on i-th position), pop element from list
        2.3 heapify feed
    Time complexity -> O(F)
    Space complexity -> O(1)
    where F size of follower feed

    getNewsFeed
    1 get 10 smallest element from heap, format to recieve only tweet id
    Time complexity -> O(F)
    Space complexity -> O(1)
    where F size of follower feed

    Notes
    There are room for optimization especially that we have limited feed size
    """
    def __init__(self):
        self.followers = {}  # who follows user
        self.followees = {}  # who user follow
        self.tweets = {}
        self.feed = {}
        self.time_counter = 0  # increment each post to compare them
        self.feed_limit = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        existing_tweets = self.tweets.get(userId, [])
        existing_tweets.append((-self.time_counter, tweetId, userId))
        self.tweets[userId] = existing_tweets
        for follower_id in self.followers.get(userId, [userId]):
            follower_feed = self.feed.get(follower_id, [])
            heapq.heappush(follower_feed, (-self.time_counter, tweetId, userId))
            self.feed[follower_id] = follower_feed
        self.time_counter += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        return [t[1] for t in heapq.nsmallest(self.feed_limit, self.feed.get(userId, []))]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            # Assign relations
            existing_followees = self.followees.get(followerId, {followerId})
            if followeeId in existing_followees:
                return
            existing_followees.add(followeeId)
            self.followees[followerId] = existing_followees
            existing_followers = self.followers.get(followeeId, {followeeId})
            existing_followers.add(followerId)
            self.followers[followeeId] = existing_followers
            # update followers feed with posts from followee
            tweets = self.tweets.get(followeeId, [])
            follower_feed = self.feed.get(followerId, [])
            for tweet in tweets:
                heapq.heappush(follower_feed, tweet)
            self.feed[followerId] = follower_feed


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            # Remove relations
            existing_followers = self.followers.get(followeeId, set())
            if followerId in existing_followers:
                existing_followers.remove(followerId)
            existing_followees = self.followees.get(followerId, set())
            if followeeId in existing_followees:
                existing_followees.remove(followeeId)
            # update followers feed with posts from followee
            follower_feed = self.feed.get(followerId, [])
            i = 0
            while i < len(follower_feed):
                if follower_feed[i][2] == followeeId:
                    follower_feed[i] = follower_feed[-1]
                    follower_feed.pop()
                    i -= 1
                i += 1
            heapq.heapify(follower_feed)
            self.feed[followerId] = follower_feed



if __name__ == '__main__':
    twitter = Twitter()
    # twitter.postTweet(1, 5)  # User 1 posts a new tweet (id = 5).
    # _ = twitter.getNewsFeed(1)   # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
    # print(_)
    # twitter.follow(1, 2)     # User 1 follows user 2.
    # twitter.postTweet(2, 6)  # User 2 posts a new tweet (id = 6).
    # _ = twitter.getNewsFeed(1)   # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
    # print(_)
    # twitter.unfollow(1, 2)   # User 1 unfollows user 2.
    # _ = twitter.getNewsFeed(1)   # User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
    # print(_)
    ###########################
    twitter.postTweet(2, 5)
    twitter.follow(1, 2)
    twitter.follow(1, 2)
    _ = twitter.getNewsFeed(1)
    print(_)
