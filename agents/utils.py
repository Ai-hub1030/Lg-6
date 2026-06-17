"""
Utility functions for agents module.
"""

from typing import Any, Dict, List


def validate_config(config: Dict[str, Any], required_keys: List[str]) -> bool:
    """
    Validate configuration dictionary.
    
    Args:
        config (dict): Configuration to validate
        required_keys (list): Required configuration keys
        
    Returns:
        bool: True if all required keys present
    """
    if not isinstance(config, dict):
        return False
    
    return all(key in config for key in required_keys)


def merge_configs(base_config: Dict[str, Any], override_config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge two configuration dictionaries.
    
    Args:
        base_config (dict): Base configuration
        override_config (dict): Configuration to override with
        
    Returns:
        dict: Merged configuration
    """
    result = base_config.copy()
    result.update(override_config)
    return result


def format_result(status: str, message: str, data: Any = None) -> Dict[str, Any]:
    """
    Format a standardized result dictionary.
    
    Args:
        status (str): Result status (success, error, warning)
        message (str): Status message
        data (any): Additional result data
        
    Returns:
        dict: Formatted result
    """
    return {
        "status": status,
        "message": message,
        "data": data
    }
