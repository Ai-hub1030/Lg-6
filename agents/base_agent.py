"""
Base Agent class for LG-6 project.

This module provides the foundation for creating specialized agents.
"""


class BaseAgent:
    """
    Base class for all agents in the LG-6 project.
    
    Attributes:
        name (str): Agent identifier
        version (str): Agent version
        config (dict): Agent configuration
    """
    
    def __init__(self, name: str, version: str = "1.0.0", config: dict = None):
        """
        Initialize the BaseAgent.
        
        Args:
            name (str): Agent name/identifier
            version (str): Agent version (default: "1.0.0")
            config (dict): Configuration dictionary (default: {})
        """
        self.name = name
        self.version = version
        self.config = config or {}
        self._initialized = True
    
    def __str__(self) -> str:
        """Return string representation of agent."""
        return f"{self.name} (v{self.version})"
    
    def __repr__(self) -> str:
        """Return detailed representation of agent."""
        return f"BaseAgent(name='{self.name}', version='{self.version}')"
    
    def initialize(self) -> bool:
        """
        Initialize agent resources.
        
        Returns:
            bool: True if initialization successful
        """
        print(f"Initializing {self.name}...")
        return self._initialized
    
    def execute(self, task: str, **kwargs) -> dict:
        """
        Execute a task.
        
        Args:
            task (str): Task to execute
            **kwargs: Additional arguments
            
        Returns:
            dict: Task results
        """
        return {
            "status": "success",
            "agent": self.name,
            "task": task,
            "result": None
        }
    
    def shutdown(self) -> bool:
        """
        Shutdown agent and cleanup resources.
        
        Returns:
            bool: True if shutdown successful
        """
        print(f"Shutting down {self.name}...")
        self._initialized = False
        return True
