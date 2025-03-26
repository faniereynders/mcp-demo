"""A robust Hello World application with logging, error handling, and interactive features.

This module demonstrates best practices in Python programming including:
- Type hints
- Proper documentation
- Error handling
- Logging
- Interactive user input
"""

import logging
from typing import Optional
import sys
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('hello_world.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

def get_user_name() -> Optional[str]:
    """
    Prompt the user for their name with input validation.
    
    Returns:
        Optional[str]: The user's name if valid, None if empty
    """
    try:
        name = input("Please enter your name (or press Enter for default): ").strip()
        return name if name else None
    except EOFError:
        logging.warning("EOF received while getting user input")
        return None
    except KeyboardInterrupt:
        logging.info("User interrupted the program")
        sys.exit(0)

def generate_greeting(name: Optional[str] = None) -> str:
    """
    Generate a personalized greeting message.
    
    Args:
        name (Optional[str]): The name to include in the greeting
        
    Returns:
        str: A personalized greeting message
    """
    current_hour = datetime.now().hour
    time_of_day = (
        "morning" if 5 <= current_hour < 12
        else "afternoon" if 12 <= current_hour < 17
        else "evening" if 17 <= current_hour < 22
        else "night"
    )
    
    base_greeting = f"Good {time_of_day}"
    if name:
        return f"{base_greeting}, {name}! 👋"
    return f"{base_greeting}, World! 👋"

def main() -> None:
    """
    Main function that runs the Hello World application.
    """
    logging.info("Starting Hello World application")
    try:
        name = get_user_name()
        greeting = generate_greeting(name)
        print(greeting)
        logging.info(f"Successfully displayed greeting: {greeting}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)
    finally:
        logging.info("Ending Hello World application")

if __name__ == "__main__":
    main()