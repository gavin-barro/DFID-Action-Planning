from action import Action

class PlanningProblem:

    def __init__(self, initial_state: list[str], goals: list[str]) -> None:
        self._initial_state = initial_state
        self._goals = goals
    
    @property
    def initial_state(self) -> list[str]:
        return self._initial_state
    
    @initial_state.setter
    def initial_state(self, initial_stare: list[str]) -> None:
        self._initial_state = initial_stare

    @property
    def goals(self) -> list[str]:
        return self._goals
    
    @goals.setter
    def goals(self, goals: list[str]) -> None:
        self._goals = goals


    def is_goal_reached(self, state: list[str]) -> bool:
        """
        Check if the goal state is reached.
        """
        return all(goal in state for goal in self.goals)

    def apply_action(self, state: list[str], action: Action) -> list[str]:
        """
        Apply an action to the current state and return the new state.
        Assumes action is applicable.
        """
        new_state: list = state.copy()
        # Remove negative effects
        for effect in action.effects:
            if effect.startswith("not("):
                effect_to_remove = effect[4:-1]  # Remove 'not(' and ')'
                if effect_to_remove in new_state:
                    new_state.remove(effect_to_remove)
        # Add positive effects
        for effect in action.effects:
            if not effect.startswith("not("):
                if effect not in new_state:
                    new_state.append(effect)
        return new_state
    
    def revert_action(self, state: list, action: Action):
        # This will attempt to create a previous state before action was applied
        previous_state = state.copy()
        for effect in action.effects:
            if not effect.startswith("not(") and effect in previous_state:
                previous_state.remove(effect)
        for effect in action.effects:
            if effect.startswith("not("):
                effect_to_add = effect[4:-1]  # 'not()' is stripped
                if effect_to_add not in previous_state:
                    previous_state.append(effect_to_add)
        return previous_state