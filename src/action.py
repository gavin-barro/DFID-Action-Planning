class Action:

    def __init__(self, name: str, preconditions: list[str], effects: list[str]) -> None:
        self._name = name
        self._preconditions = preconditions
        self._effects = effects

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    @property
    def preconditions(self) -> list[str]:
        return self._preconditions
    
    @preconditions.setter
    def preconditions(self, new_preconditions: list[str]) -> None:
        self._preconditions = new_preconditions

    @property
    def effects(self) -> list[str]:
        return self._effects 
    
    @effects.setter
    def effects(self, new_effects: list[str]) -> None:
        self._effects = new_effects

    def __str__(self):
        return f"Action(name={self.name}, preconditions={self.preconditions}, effects={self.effects})"
