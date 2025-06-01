from action import Action
from planning_problem import PlanningProblem


class ForwardDFID:

    def __init__(self, problem: PlanningProblem, actions: list[Action]) -> None:
        self._problem = problem
        self._actions = actions

    @property
    def problem(self) -> PlanningProblem:
        return self._problem

    @problem.setter
    def problem(self, problem: PlanningProblem) -> None:
        self._problem = problem

    @property
    def actions(self) -> list[Action]:
        return self._actions

    @actions.setter
    def actions(self, actions: list[Action]) -> None:
        self._actions = actions

    def depth_first_iterative_deepening(self, max_depth: int | float = float('inf')) -> list[str] | None:
        depth = 0
        while depth <= max_depth:
            print(f"Searching at depth: {depth}")
            result = self.depth_first_search(self.problem.initial_state, [], depth)
            if result is not None:
                return result
            depth += 1
        return None  # Return None if no solution is found within the maximum depth

    def depth_first_search(self, current_state: list[str], path: list[str], depth: int) -> list[str] | None:
        print(f"Current state: {current_state}")
        print(f"Current path: {path}")
        print(f"Current depth: {depth}")

        if depth == 0 and self.problem.is_goal_reached(current_state):
            print("Goal reached!")
            return path
        elif depth > 0:
            for action in self.actions:
                if all(pre in current_state for pre in action.preconditions):
                    new_state = self.problem.apply_action(current_state, action)
                    if new_state is not None:  # Ensure action was applicable
                        print(f"Applying action: {action.name}")
                        print(f"New state after action: {new_state}")
                        result = self.depth_first_search(new_state, path + [action.name], depth - 1)
                        if result is not None:
                            return result
        return None


class BackwardDFID:

    def __init__(self, problem: PlanningProblem, actions: list[Action]) -> None:
        self._problem = problem
        self._actions = actions

    @property
    def problem(self) -> PlanningProblem:
        return self._problem

    @problem.setter
    def problem(self, problem: PlanningProblem) -> None:
        self._problem = problem

    @property
    def actions(self) -> list[Action]:
        return self._actions

    @actions.setter
    def actions(self, actions: list[Action]) -> None:
        self._actions = actions

    def depth_first_iterative_deepening(self, max_depth: int | float = float('inf')) \
            -> list[str] | None:
        depth = 0
        while depth <= max_depth:
            result = self.depth_first_search(self.problem.initial_state, [], depth)
            if result is not None:
                return result
            depth += 1
        return None

    def depth_first_search(self, current_state: list[str], path: list[str], depth: int) -> list[str] | None:
        if depth == 0 and all(item in self.problem.initial_state for item in current_state):
            return path
        elif depth > 0:
            for action in self.actions:
                if any(effect.strip("not()") in current_state for effect in action.effects
                       if effect.startswith("not")):

                    possible_prior_state = self.problem.revert_action(current_state, action)
                    if possible_prior_state is not None:
                        result = self.depth_first_search(possible_prior_state, path + [action.name], depth - 1)
                        if result is not None:
                            return result
        return None
