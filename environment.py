class Environment:
    """Represents the environment in which agents operate."""
    def __init__(self):
        self.state = {}
    
    def update(self, key, value):
        """Updates the environment state."""
        self.state[key] = value
    
    def get(self, key, default=None):
        """Retrieves a value from the environment state."""
        return self.state.get(key, default)
