from action import Action
from planning_problem import PlanningProblem
from dfid import ForwardDFID
from dfid import BackwardDFID
import yaml

def read_actions(filepath: str) -> list[Action]:
    actions = []

    with open(filepath, 'r') as file:
        data = yaml.safe_load(file)
        for action_name, action_data in data.get('actions', {}).items():
            name = action_name
            preconditions = action_data.get('preconditions', [])
            effects = action_data.get('effects', [])
            action = Action(name, preconditions, effects)
            actions.append(action)
        
    return actions

def read_predicates_from_file(filepath: str) -> list[str]:
    predicates = []

    # Open the file and read lines
    with open(filepath, 'r') as file:
        lines = file.readlines()
    
    # Process each line to extract predicate
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace
        if line and not line.startswith('#'):  # Ignore empty lines and comments
            predicates.append(line)  # Add the predicate to the list
    
    return predicates


def main():
    # Define file paths
    actions_file = "HW4/actions.yaml"
    initial_state_file = "HW4/initial_state.txt"
    goal_state_file = "HW4/goals.txt"

    # Read actions from YAML file
    actions = read_actions(actions_file)

    # Read predicates from initial state file
    initial_state_predicates = read_predicates_from_file(initial_state_file)

    # Read predicates from goal state file
    goal_state_predicates = read_predicates_from_file(goal_state_file)

    # Create a PlanningProblem instance
    problem = PlanningProblem(initial_state_predicates, goal_state_predicates)
    
    # Create ForwardDFID and BackwardDFID instances
    forward_search = ForwardDFID(problem, actions)
    backward_search = BackwardDFID(problem, actions)
    
    # Specify maximum depth for iterative deepening
    max_depth = 100

    # Compute plan using forward state-space search with DFID and maximum depth
    forward_plan = forward_search.depth_first_iterative_deepening(max_depth=max_depth)

    # Compute plan using backward/goal-directed state-space search with DFID and maximum depth
    backward_plan = backward_search.depth_first_iterative_deepening(max_depth=max_depth)

    # Print the resulting plans or messages
    if forward_plan is not None:
        print("Forward Plan found:")
        for step in forward_plan:
            print(step)
        print("\n")
    else:
        print("No forward plan found within the specified maximum depth.")

    print('-----------------------------------------------------------------------')

    if backward_plan is not None:
        print("Backward Plan found:")
        for step in backward_plan:
            print(step)
        print("\n")
    else:
        print("No backward plan found within the specified maximum depth.")


if __name__ == "__main__":
    main()
