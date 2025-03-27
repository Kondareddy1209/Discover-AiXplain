# Multi-Agent System

This project implements a simple multi-agent system where multiple agents interact with an environment.

## Files and Their Roles

- **multi_agent_system.py**: Defines the `Agent` class that represents an autonomous agent.
- **environment.py**: Implements the `Environment` class to manage state and agent interactions.
- **utils.py**: Provides utility functions, including logging setup.
- **agent_runner.py**: Coordinates multiple agents and runs them in a shared environment.

## How to Run

1. Ensure you have Python installed.
2. Run `agent_runner.py` to initialize the environment and execute agents.

```sh
python agent_runner.py
```

## Requirements
This project uses Python's built-in `logging` module, so no additional dependencies are required.

## Example Output
```
2025-03-27 12:00:00 - INFO - Logging setup complete.
2025-03-27 12:00:01 - INFO - Initializing environment...
2025-03-27 12:00:02 - INFO - Agent-0 is starting execution.
2025-03-27 12:00:03 - INFO - Agent-0 executed task: data processing.
2025-03-27 12:00:04 - INFO - Agent-0 has completed execution.
...
2025-03-27 12:00:10 - INFO - All agents have completed execution.
```

## License
This project is released under the MIT License.
