from typing import List


def asteroid_collision(asteroids: List) -> List:
    """
    The `asteroid_collision` method takes a list of integers representing the sizes of asteroids and returns a list of integers representing the sizes of asteroids remaining after the collision occurs.

    :param asteroids: A list of integers representing the sizes of asteroids. Positive integers represent asteroids moving to the right, negative integers represent asteroids moving to the left.
    :return: A list of integers representing the sizes of asteroids remaining after the collision.
    """
    stack = []
    for asteroid in asteroids:
        while stack and asteroid < 0 < stack[-1]:
            if stack[-1] < -asteroid:
                stack.pop()
                continue
            elif stack[-1] == -asteroid:
                stack.pop()
            break
        else:
            stack.append(asteroid)
    return stack
