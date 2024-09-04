# Asteroid Collision Simulation

The `asteroid_collision` function simulates the collision of asteroids based on their size and direction. Given a list of integers representing the size and direction of asteroids, the function returns the list of asteroids that remain after all collisions occur.

## Function Overview

### `asteroid_collision(asteroids: List[int]) -> List[int]`

This function takes a list of integers, where:
- Positive integers represent asteroids moving to the right.
- Negative integers represent asteroids moving to the left.

When two asteroids collide:
- The larger one survives if the absolute value of its size is greater than the other.
- If both are the same size, both asteroids are destroyed.
- Asteroids moving in the same direction do not collide.

### Parameters:
- `asteroids` (`List[int]`): A list of integers representing the sizes and directions of asteroids. Positive values move to the right, negative values move to the left.

### Returns:
- A `List[int]` representing the sizes of the asteroids that remain after all collisions.

### How it Works:
1. The function uses a **stack** to simulate the sequence of collisions.
2. For each asteroid in the list, the function checks if a collision is possible (i.e., an asteroid on the stack is moving to the right and the current asteroid is moving to the left).
3. If a collision occurs:
   - The function compares the absolute sizes of the two asteroids.
   - The smaller one is destroyed, and the larger one continues moving.
   - If they are the same size, both are destroyed.
4. If no collision occurs, or if the asteroid survives, it is added to the stack.
5. The stack holds the final result of surviving asteroids after all collisions are processed.

### Requirements:
1. Python 3.x

### Future Improvements:
1. Add support for other types of asteroid events, such as asteroids that change direction after a collision.
2. Optimize the function further for larger datasets of asteroids.