"""
Digital Clock application displaying time in multiple time zones.
"""

import sys
from datetime import datetime
from typing import List, Dict
import pytz


class DigitalClock:
    """
    A digital clock that displays current time in multiple time zones.
    
    Attributes:
        time_zones (list): List of time zone identifiers
        format_12h (bool): Use 12-hour format if True, 24-hour if False
    """
    
    def __init__(self, time_zones: List[str] = None, format_12h: bool = True):
        """
        Initialize the digital clock.
        
        Args:
            time_zones (list): List of timezone strings (e.g., ['US/Eastern', 'Europe/London'])
            format_12h (bool): Whether to use 12-hour format (default: True)
        """
        self.format_12h = format_12h
        self.time_zones = time_zones or [
            'US/Eastern',
            'US/Central',
            'US/Mountain',
            'US/Pacific',
            'Europe/London',
            'Europe/Paris',
            'Asia/Tokyo',
            'Australia/Sydney'
        ]
        self._validate_timezones()
    
    def _validate_timezones(self) -> None:
        """Validate that all provided timezones are valid."""
        for tz in self.time_zones:
            try:
                pytz.timezone(tz)
            except pytz.exceptions.UnknownTimeZoneError:
                raise ValueError(f"Unknown timezone: {tz}")
    
    def get_current_time(self, timezone_str: str) -> datetime:
        """
        Get current time in a specific timezone.
        
        Args:
            timezone_str (str): Timezone identifier
            
        Returns:
            datetime: Current time in the specified timezone
        """
        tz = pytz.timezone(timezone_str)
        return datetime.now(tz)
    
    def format_time(self, dt: datetime) -> str:
        """
        Format datetime object as a time string.
        
        Args:
            dt (datetime): Datetime object to format
            
        Returns:
            str: Formatted time string
        """
        if self.format_12h:
            return dt.strftime("%I:%M:%S %p")
        else:
            return dt.strftime("%H:%M:%S")
    
    def display_all_times(self) -> Dict[str, str]:
        """
        Get current time for all configured timezones.
        
        Returns:
            dict: Dictionary mapping timezone names to formatted times
        """
        times = {}
        for tz in self.time_zones:
            current_time = self.get_current_time(tz)
            times[tz] = self.format_time(current_time)
        return times
    
    def display_all_times_detailed(self) -> Dict[str, Dict]:
        """
        Get detailed current time info for all configured timezones.
        
        Returns:
            dict: Dictionary with detailed timezone information
        """
        times = {}
        for tz in self.time_zones:
            current_time = self.get_current_time(tz)
            times[tz] = {
                'time': self.format_time(current_time),
                'date': current_time.strftime("%Y-%m-%d"),
                'day': current_time.strftime("%A"),
                'utc_offset': current_time.strftime("%z")
            }
        return times
    
    def print_clock(self) -> None:
        """Print a formatted display of all timezone clocks."""
        print("\n" + "="*60)
        print("DIGITAL WORLD CLOCK".center(60))
        print("="*60)
        
        times = self.display_all_times_detailed()
        
        for tz, info in times.items():
            print(f"\n{tz}")
            print(f"  Time:   {info['time']}")
            print(f"  Date:   {info['date']} ({info['day']})")
            print(f"  Offset: {info['utc_offset']}")
        
        print("\n" + "="*60)
    
    def add_timezone(self, timezone_str: str) -> None:
        """
        Add a new timezone to the clock.
        
        Args:
            timezone_str (str): Timezone identifier to add
            
        Raises:
            ValueError: If timezone is invalid or already exists
        """
        try:
            pytz.timezone(timezone_str)
        except pytz.exceptions.UnknownTimeZoneError:
            raise ValueError(f"Unknown timezone: {timezone_str}")
        
        if timezone_str in self.time_zones:
            raise ValueError(f"Timezone {timezone_str} already exists")
        
        self.time_zones.append(timezone_str)
    
    def remove_timezone(self, timezone_str: str) -> None:
        """
        Remove a timezone from the clock.
        
        Args:
            timezone_str (str): Timezone identifier to remove
            
        Raises:
            ValueError: If timezone is not in the list
        """
        if timezone_str not in self.time_zones:
            raise ValueError(f"Timezone {timezone_str} not found")
        
        self.time_zones.remove(timezone_str)
    
    def set_timezones(self, time_zones: List[str]) -> None:
        """
        Set a new list of timezones.
        
        Args:
            time_zones (list): List of timezone identifiers
        """
        self.time_zones = time_zones
        self._validate_timezones()
    
    def toggle_format(self) -> None:
        """Toggle between 12-hour and 24-hour format."""
        self.format_12h = not self.format_12h


def main():
    """Main function to demonstrate the digital clock."""
    # Create clock with default timezones
    clock = DigitalClock()
    
    # Display all times
    clock.print_clock()
    
    # Add custom timezone
    print("\nAdding custom timezone: Asia/Dubai")
    clock.add_timezone('Asia/Dubai')
    clock.print_clock()
    
    # Toggle to 24-hour format
    print("\nSwitching to 24-hour format...")
    clock.toggle_format()
    clock.print_clock()
    
    # Display just the times dictionary
    print("\nTimes dictionary (12-hour format):")
    clock.toggle_format()
    times = clock.display_all_times()
    for tz, time_str in times.items():
        print(f"  {tz}: {time_str}")


if __name__ == "__main__":
    main()
