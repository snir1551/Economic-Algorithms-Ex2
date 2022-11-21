import math
import queue
from typing import Dict
import json

def BFS(matrix: list[list]) -> dict:
    stack = queue.Queue()
    stack.put([0, 0, 0])
    count_states_deleted = 0
    visit = set()
    index_object = 0
    ans: Dict[int, list] = dict()
    min_between_players = math.inf
    max_between_objects = 0
    next_object = 0
    # ans.update({i: [0, 0, 0]})
    num_current_rank = math.pow(len(matrix[0]), index_object)
    while (not stack.empty()):
        # print(stack.pop())
        a = stack.get()
        # print(a)
        for index_player in range(len(matrix[0])):
            a[index_player] += matrix[index_object][index_player]
            if visit.__contains__(tuple(a)):
                a[index_player] -= matrix[index_object][index_player]
                for i in range(len(matrix) - index_object):
                    count_states_deleted += math.pow(len(matrix[0]), i)
                print("count_states")
                print(count_states_deleted)
                continue
            visit.add(tuple(a))
            if ans.get(index_object) == None:
                ans.update({index_object: [a.copy()]})

            else:
                ans.get(index_object).append(a.copy())

            print(a)
            if len(matrix) - 1 > index_object:
                print(len(matrix) - 1)
                stack.put(a.copy())

            for player_value in range(len(matrix[0])):
                if min_between_players > a[player_value]:
                    min_between_players = a[player_value]

            if max_between_objects < min_between_players:
                max_between_objects = min_between_players
            min_between_players = math.inf

            a[index_player] -= matrix[index_object][index_player]
        num_current_rank -= 1
        if num_current_rank == 0:
            index_object += 1
            num_current_rank = math.pow(len(matrix[0]), index_object)
            print("-----------------")
            print(ans)
            print("-----------------")

    return max_between_objects


def draw_tree(tree: dict):
    pretty = json.dumps(tree, indent=4, sort_keys=True)
    print(pretty)


