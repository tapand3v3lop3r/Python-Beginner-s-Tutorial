"""
Modules in Python allow you to organize code into reusable units,
structuring large programs and promoting code reusability.

We'll explore how to use modules effectively in Python.

To install a module, use pip:
    pip install pyjokes

Once installed, import the module into your Python script:
    import pyjokes

Importing a module allows you to access its functions and classes.

We will delve deeper into different modules and their functionalities in upcoming sections.
Modules are powerful tools in Python programming for maintaining clean, organized code.

Stay tuned as we explore more advanced topics later on.
"""

# Import the `pyjokes` module
import pyjokes

# Get a random joke using `pyjokes.get_joke()`
joke = pyjokes.get_joke()

# Print the joke to the console
print("Here's a joke for you:")
print(joke)
