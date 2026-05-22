if __name__ == "__main__":
    import sys

    from difficulty.factory import get_difficulty

    from .dtos import GetToyDifficultyPayload

    selected_difficulty = sys.argv[1] if len(sys.argv) > 1 else "easy"
    dto = GetToyDifficultyPayload(difficulty=selected_difficulty)
    result_get_difficulty = get_difficulty(dto)
    if not result_get_difficulty.success:
        for error in result_get_difficulty.error:
            print(f"Error: {error}")
            sys.exit(1)

    if not result_get_difficulty.data:
        print("Error: No difficulty data returned.")
        sys.exit(1)

    difficulty = result_get_difficulty.data
    print(f"Selected difficulty: {difficulty.get_difficulty_level}")
    print(f"Number of pieces: {difficulty.get_num_pieces}")
