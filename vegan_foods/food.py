from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class Nutrient:
    """
    Data class representing a nutrient in a food item.
    """
    id: str  # euro fir id
    name: str
    quantity: float = 0.0
    unit: str = "g"


@dataclass
class Food:
    """
    Data class representing a food item.
    """
    id: str
    name: str
    group_id: str
    group_name: str
    nutrients: Dict[str, Nutrient] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, food_dict: Dict[str, Any]) -> 'Food':
        """
        Create a Food object from a dictionary.

        Args:
            food_dict: Dictionary containing food data

        Returns:
            Food: A Food object
        """
        constituents_dict = {}
        for euroFirId, constituent_data in food_dict.get('constituents', {}).items():
            nutrient = Nutrient(
                id=euroFirId,
                name=constituent_data['nutrientName'],
                quantity=float(constituent_data.get('quantity', 0.0)),
                unit=constituent_data.get('unit', 'g')
            )
            constituents_dict[nutrient.id] = nutrient

        return cls(
            id=food_dict['foodId'],
            name=food_dict['foodName'],
            group_id=food_dict['foodGroupId'],
            group_name=food_dict['foodGroupName'],
            nutrients=constituents_dict
        )
