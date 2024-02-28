import logging # import statement is key to tap into logging module
# objective
# Import and use the logging module/class
# Understand and use the severity levels
# Configure file path and use exception handling to write logs to file with different severity levels


"read for 2 minutes"

''' Python Exception is represented in class hierarchy using built in or user define exception types
object of the class exception will be created when an exception is raised.
 exception class inherits from the base exception class

 Both the StandardError and Warning inherits from the Exception class.
 
 Standard errors will terminate program if not handle correctly
 Standard error like EOFError results in trying to read beyond the end of a file at run time.
 ZeroDivisionError trying to divide by zero.
 Indentation error improper indentation of programming/code blocks.'''

# An exception is handled using the try and except block.

"To Do: Predict, then Run, and then Investigate"

#different logging methods and severity

logging.basicConfig (filename= r"Week 10 - Pyton\Day 6\Pt8_ExceptionsCodeBase2024/file1.log", level = logging.INFO) #comment to see what logging level will be displayed in the terminal
logging.critical("Critical")
logging.error("Error")
logging.warning("Warning")
logging.info("Info")
logging.debug ("Debug")




"To Do: Modify"
# Modify: 
# Task 1. Change the level from level=logging.DEBUG to logging.INFO, run the code and explain the output from the terminal
# Task 2. Remove the level=logging.DEBUG or level=logging.INFO, between the parenthesis of logging.basicConfig and run the code and explain the output from the terminal

# task 1: shows INFO:root:Info, the debug message is being logged but it's showing as debug

# task 2: no debug and info showing

