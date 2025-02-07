class Card:
    def __init__(self, name: str, description: str, card_type: str):
        """
        Base class for all cards.
        :param name: The name of the card (e.g., "Bang!", "Missed!", "Beer").
        :param description: A brief description of the card's effect.
        :param card_type: The type of the card (e.g., "attack", "defense", "effect").
        """
        # Validate parameters
        if not isinstance(name, str) or not name.strip(): # - Makes sure the `name` is a non-empty string.
            raise ValueError("Card name must be a non-empty string.")
        if not isinstance(description, str): # - Validates that the `description` is a string.
            raise ValueError("Card description must be a string.")
        if card_type not in ("attack", "defense", "effect"):  # To adjust types as needed
            raise ValueError(f"Invalid card type: {card_type}.")

        # Assign attributes after validation
        self.name = name
        self.description = description
        self.card_type = card_type
        self.is_playable = True

    def use(self, player, target):
        """
        Executes the card logic. To be implemented in subclasses.
        :param player: The player using the card.
        :param target: The target player (can be None for self-effects like healing).
        """
        raise NotImplementedError("This method should be overridden in subclasses.")

    def __repr__(self):
        return f"{self.name} ({self.card_type})"
