
import random


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        relationships = []
        # Add users

        for user in range(numUsers):
            self.addUser(user)

        for userID in self.users:
            for friendID in range(userID + 1, self.lastID+1):
                if userID != friendID:
                    relationships.append((userID, friendID))

        random.shuffle(relationships)

        total = avgFriendships * numUsers

        make_friends = relationships[:int(total / 2)]

        for friendship in make_friends:
            f1 = friendship[0]
            f2 = friendship[1]
            self.addFriendship(f1, f2)
        # Create friendships

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        friend_group = {}  # Note that this is a dictionary, not a set

        def shortest_connection(start, stop):
            breadth = Queue()
            visited = []
            breadth.enqueue([start])
            while breadth.size():
                path = breadth.dequeue()
                node = path[-1]
                if node not in visited:
                    visited.append(node)
                    if node == stop:
                        friend_group[node] = path[::-1]
                    for neighbor in self.friendships[node]:
                        new_path = path[:]
                        new_path.append(neighbor)
                        breadth.enqueue(new_path)

        for friend in self.friendships:
            if friend == userID:
                continue

            else:
                shortest_connection(userID, friend)

        print(f"All of {userID}'s connections")
        return friend_group

        # !!!! IMPLEMENT ME
        return friend_group


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
