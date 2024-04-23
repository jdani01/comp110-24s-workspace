"""Some functions for my garden plan!"""

__author__ = "730404642"


def add_by_kind(garden: dict[str, list[str]], kind: str, name:str) -> None:
    """Adds a plant."""
    if kind in garden:
        garden[kind].append(name)
    else:
        garden[kind] = [name]


def add_by_date(garden: dict[str, list[str]], month: str, name: str) -> None:
    """Adds a date."""
    if month in garden:
        garden[month].append(name)
    else:
        garden[month] = [name]


def lookup_by_kind_and_date(by_kind: dict[str, list[str]], by_date: dict[str, list[str]], kind: str, date: str) -> str:
    """Looks up plant kind and date. """
    plants_of_kind = by_kind.get(kind, [])
    plants_on_date = by_date.get(date, [])
    
    common_plants = [plant for 
                     plant in 
                     plants_of_kind if 
                     plant in plants_on_date]
    
    if common_plants:
        return f"{kind.capitalize()}s to plant in {date}: {common_plants}"
    else:
        return f'No {kind}s to plant in {date}.'