"""Static action sets for binary to discrete action space wrappers."""


# actions for the simple run right environment
RIGHT_ONLY = [
    ['NOOP'],
    ['right'],
    ['right', 'A'],
    ['right', 'B'],
    ['right', 'A', 'B'],
]


# actions for very simple movement
SIMPLE_MOVEMENT = [
    ['NOOP'],
    ['right'],
    ['right', 'A'],
    ['right', 'B'],
    ['right', 'A', 'B'],
    ['A'],
    ['left'],
]


# actions for more complex movement
COMPLEX_MOVEMENT = [
    ['NOOP'],
    ['right'],
    ['right', 'A'],
    ['right', 'B'],
    ['right', 'A', 'up'],
    ['right', 'B', 'up'],
    ['right', 'A', 'B', 'up'],
    ['A'],
    ['B'],
    ['A', 'B'],

    ['left'],
    ['left', 'A'],
    ['left', 'B'],
    ['left', 'A', 'up'],
    ['left', 'B', 'up'],
    ['left', 'A', 'B', 'up'],

    ['down', 'A'],
    ['down', 'B'],
    ['down', 'A', 'B'],
    ['up', 'A'],
    ['up', 'A', 'B'],
]
