# levels.py
game_levels = [
    {
        "targets": [(1, 3), (1, 5)],
        "pieces": [
            {"type": "p", "position": (2, 2)},
            {"type": "i", "position": (1, 4)},
        ],
        "move_limit": 2  
    },
    {
        "targets": [(0, 2), (2, 0), (2, 2), (2, 4), (4, 2)],
        "pieces": [
            {"type": "i", "position": (1, 2)},
            {"type": "i", "position": (2, 1)},
            {"type": "i", "position": (2, 3)},
            {"type": "i", "position": (3, 2)},
            {"type": "p", "position": (4, 0)}
        ],
        "move_limit": 3
    }
]
