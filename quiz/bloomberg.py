# question one
# Asked to reverse a string in Python
# https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/\
s='shanghairenisthemaster'
s1=s[::-1]
print 'using the negitive index to reverse the string',s1
for x in s:
    s1 = x + s1
print 'using loop to reverse the string:', s1
s1= list(reversed(s))
s1 = ''.join(s1)
print'using the reversed list function to reverse the string:', s1

# question two
# Input string s. Check if string s is a valid string with valid brackets
# For example:
#
# (({{}})) is a valid s
#
# {[]} is a valid s
#
# [{[}]] is not valid
#

# Python3 code to Check for
# balanced parentheses in an expression
open_list = ["[","{","("]
close_list = ["]","}",")"]

def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"


# Driver code
string = "{}"
print(string, "-", check(string))

string = "[{}{})(]"
print(string, "-", check(string))

# using queue
def check0(expression):
    open_tup = tuple('({[')
    close_tup = tuple(')}]')
    map = dict(zip(open_tup, close_tup))
    queue = []

    for i in expression:
        if i in open_tup:
            queue.append(map[i])
        elif i in close_tup:
            if not queue or i != queue.pop():
                return "Unbalanced"
    return "Balanced"

# Driver code
string = "{}"
print(string, "-", check(string))

def check1(str):
    open_tup = ('[','{','(')
    close_tup = (']','}',')')
    map = dict(zip(open_tup,close_tup))
    queue = []
    for s in str:
        if s in open_tup:
            queue.append(map[s])
        elif s in close_tup:
            if not queue or s != queue.pop():
                return 'unbalanced'
    return 'balanced'

str ='{[}]'
print ('doing check1 checking:', check1(str))

# question three
# If you had n racers and m checkpoints, how would you list out the racers in the order in
# which they are in the race given that each checkpoint gets a notification when
# a specific racer crosses it?
# Your code should run in O(1).
#
# Note: Players cannot cheat, i.e. they cannot miss a checkpoint
#
# Example:
#
# Assume 5 checkpoints(C1, C2, C3, C4, C5) and 10 racers(P1, P2,...P10).
#
# Now once the race begins, lets say P2 first crosses C1. So the current race order is P2.
#
# Now P1, P3, P4 cross C1; so the race order is P2, P1, P3, P4.
#
# Now P1, crosses C2; so the race order becomes P1, P2, P3, P4
#
# Now P3, crosses C2; so the race order becomes P1, P3, P2, P4
#
# Now P5, crosses C1; so the race order becomes P1, P3, P2, P4, P5
#
# Now P1 crosses C3; so the race order remains P1, P3, P2, P4, P5
# and so on.
# solusion page
# https://www.careercup.com/question?id=5741433848332288
from collections import OrderedDict
class racers_checkpoint:
    def __init__(self, num_players, num_checkpoints):
        self.n = num_players
        self.m = num_checkpoints
        self.player_current_position = {x: 0 for x in range(1, self.n + 1)}
        self.check_point_queues = {x:OrderedDict() for x in range(1, self.m + 1)}
        self.ordered_players = [self.check_point_queues[i].keys() for i in list(range(self.m, 0, -1))]

    def update_and_retrieve(self, player, checkpoint):
        try:
            del self.check_point_queues[self.player_current_position[player]][player]  # remove player from old queue
        except KeyError:
            print("no player in the queue")
        self.check_point_queues[checkpoint][player] = None  # add to the new queue
        self.player_current_position[player] = checkpoint  # update current position
        return self.ordered_players


if __name__ == '__main__':
    my_race = racers_checkpoint(10, 5)
    print(my_race.update_and_retrieve(5, 1))
    print(my_race.update_and_retrieve(1, 1))
    print(my_race.update_and_retrieve(2, 1))
    print(my_race.update_and_retrieve(5, 2))
    print(my_race.update_and_retrieve(3, 1))
    print(my_race.update_and_retrieve(5, 3))
    print(my_race.update_and_retrieve(4, 1))

# question four
# Given an input string, reverse the string word by word.
# Example:
# input: "the sky is blue"
# output blue is sky the
# Assume that you get notified of players crossing a checkpoin
s = 'the sky is blue'
s1 = s.split()
print 'reversed sentence by the words', s1[::-1]