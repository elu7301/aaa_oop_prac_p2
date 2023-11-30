from keyword import kwlist


class ColorizeMixin:
    """A mixin class for adding color representation to strings."""

    def color_repr(self, text: str) -> str:
        """Wraps the given text with ANSI color codes for representation.

        Args:
            text (str): The text to wrap with color codes.

        Returns:
            str: The colored representation of the text.
        """
        return f'\033[1;{self.repr_color_code}m{text}'


class JsonParser:
    """A class for parsing JSON data and dynamically creating attributes."""

    def __init__(self, json_data: dict):
        """Initializes the JsonParser with JSON data.

        Args:
            json_data (dict): The JSON data to parse.
        """
        for key, value in json_data.items():
            if key in kwlist:
                key = key + '_'
            if isinstance(value, dict):
                setattr(self, key, JsonParser(value))
            else:
                setattr(self, key, value)


class Advert(ColorizeMixin, JsonParser):
    """A class representing an advertisement."""

    repr_color_code = 32  # цвет 32 - зеленый, 33 - желтый

    def __init__(self, mapping: dict):
        """Initializes an Advert instance.

        Args:
            mapping (dict): The mapping data for the Advert.

        Raises:
            ValueError: If the 'title' key is missing in the mapping data.
        """
        if 'title' not in mapping:
            raise ValueError('Title is required')
        if not hasattr(self, 'price'):
            self.price = 0

        super().__init__(mapping)

    @property
    def price(self):
        """int: The price of the advertisement."""
        return self._price

    @price.setter
    def price(self, value):
        """Sets the price of the advertisement.

        Args:
            value (int): The price value to set.

        Raises:
            ValueError: If the price value is less than 0.
        """
        if value < 0:
            raise ValueError('Price must be >= 0')
        self._price = value

    def __repr__(self) -> str:
        """Returns a colored representation of the Advert.

        Returns:
            str: The colored representation of the Advert.
        """
        return self.color_repr(text=f'{self.title} | {self.price} ₽')