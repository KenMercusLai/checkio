from collections import defaultdict
from math import hypot
from random import choice


possible_positions = [(i, j) for i in range(10) for j in range(10)]


def distance(point_1, point_2):
    return hypot(point_2[0] - point_1[0], point_2[1] - point_1[1])


def checkio(steps):
    global possible_positions
    previous_distance = defaultdict(int)

    if len(steps) == 1:
        possible_positions = [(i, j) for i in range(10) for j in range(10)]
        possible_positions.remove(tuple(steps[0][:2]))
        for i in possible_positions:
            previous_distance[i] = distance(tuple(steps[0][:2]), i)
        max_distance = max(previous_distance.values())
        candidates = [
            cell for cell, value in previous_distance.items() if value == max_distance
        ]
        next_step = choice(candidates)
        possible_positions.remove(next_step)
        return next_step

    last_step = tuple(steps[-1][:2])
    last_feedback = steps[-1][-1]
    disqualified = []
    for i in possible_positions:
        last_distance = distance(tuple(steps[-2][:2]), i)
        current_distance = distance(last_step, i)
        if last_feedback == -1 and last_distance >= current_distance:
            disqualified.append(i)
        elif last_feedback == 0 and last_distance != current_distance:
            disqualified.append(i)
        elif last_feedback == 1 and last_distance <= current_distance:
            disqualified.append(i)
    for i in disqualified:
        possible_positions.remove(i)
    next_step = choice(possible_positions)
    possible_positions.remove(next_step)
    return next_step


if __name__ == '__main__':
    # This part is using only for self-checking and not necessary for
    # auto-testing
    MAX_STEP = 12

    def check_solution(func, goal, start):
        prev_steps = [start]
        for step in range(MAX_STEP):
            row, col = func([s[:] for s in prev_steps])
            if [row, col] == goal:
                return True
            if 10 <= row or 0 > row or 10 <= col or 0 > col:
                print("You gave wrong coordinates.")
                return False
            prev_distance = hypot(
                prev_steps[-1][0] - goal[0], prev_steps[-1][1] - goal[1]
            )
            distance = hypot(row - goal[0], col - goal[1])
            alteration = (
                0
                if prev_distance == distance
                else (1 if prev_distance > distance else -1)
            )
            prev_steps.append([row, col, alteration])
        print("Too many steps")
        return False

    assert check_solution(checkio, [7, 7], [5, 5, 0]), "1st example"
    assert check_solution(checkio, [5, 6], [0, 0, 0]), "2nd example"
