if __name__ == "__main__":
    import sys

    from difficulty.factory import get_difficulty

    selected_difficulty = sys.argv[1] if len(sys.argv) > 1 else "easy"
    difficulty_instance = get_difficulty(selected_difficulty)
    print(f"Selected Difficulty: {difficulty_instance.get_difficulty_level()}")
    print(f"Number of Pieces: {difficulty_instance.get_num_pieces()}")
