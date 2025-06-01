# Logical Planning with DFID

This project implements a logical planning system using depth-first iterative deepening (DFID) to find action sequences that transition from an initial state to a desired goal state. The system models the world using logical predicates and applies a set of actions with preconditions and effects to reach the goal.

## 🧠 Overview

The planning environment is defined using logical predicates such as:

- `on(Block, Surface)`: Block is on top of a surface.
- `clear(Object)`: Object has nothing on top of it.
- `at_truck(Truck, Location)`: Truck is at a specific location.
- `in_truck(Object, Truck)`: Object is inside a truck.
- `at_location(Object, City)`: Object is at a specific city.

Actions are defined with:
- A name
- Preconditions (conditions that must be true to apply the action)
- Effects (changes that result from applying the action)

The planner searches for a sequence of actions that transforms the initial state into a state satisfying the goal predicates.

---

## 📁 File Structure

- `driver.py`: Main driver script that runs the planning algorithm.
- `action.py`: Contains the `Action` class used to represent actions with preconditions and effects.
- `planning_problem.py`: Contains the `PlanningProblem` class for managing the initial state, goal state, and action application logic.
- `dfid.py`: Contains the `BackwardsDFID` and `ForwardsDFID` classes implementing depth-first iterative deepening search.
- `actions.yaml`: (if applicable) YAML file describing the available actions in the domain.

---

## 🚀 How to Run

1. Ensure you have Python 3.x installed.
2. Clone the repo:
   ```bash
   git clone https://github.com/your-username/DFID-Action-Planning.git
   cd DFID-Action-Planning
3. Run the file python driver.py