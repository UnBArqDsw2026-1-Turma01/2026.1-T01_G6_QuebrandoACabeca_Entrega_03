from __future__ import annotations

import importlib

from .base import Difficulty


def get_difficulty(selected_difficulty: str) -> Difficulty:
    """
    Dynamically imports and instantiates the difficulty only when requested.
    Args:
        selected_difficulty (str): The selected_difficulty to use.
    Returns:
        Difficulty: An instance of the requested difficulty.
    """
    try:
        module = importlib.import_module(
            f".{selected_difficulty.lower()}", package=__package__
        )

        class_name = f"{selected_difficulty.capitalize()}Difficulty"
        backend_class = getattr(module, class_name)

        if not issubclass(backend_class, Difficulty):
            raise ValueError(
                f"Class '{class_name}' in '{selected_difficulty}.py' module does not implement Difficulty."
            )

        return backend_class()
    except ImportError:
        raise ValueError(
            f"Module for difficulty level '{selected_difficulty}' not found."
        )

    except AttributeError:
        raise ValueError(
            f"Class '{class_name}' not found in '{selected_difficulty}.py' module."
        )
