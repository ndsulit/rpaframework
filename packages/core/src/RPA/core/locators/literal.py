from RPA.core.locators import LocatorsDatabase, Locator, TYPES


def parse(locator: str) -> Locator:
    if isinstance(locator, Locator):
        return locator

    try:
        name, _, value = str(locator).partition(":")
    except ValueError as err:
        raise ValueError(f"Invalid locator format: {locator}") from err

    if not value:
        name, value = "alias", name

    name = name.strip().lower()
    if name == "alias":
        return LocatorsDatabase.load_by_name(value)
    else:
        klass = TYPES.get(name)
        if not klass:
            raise ValueError(f"Unknown locator type: {name}")

        args = value.split(",")
        return klass(*args)
