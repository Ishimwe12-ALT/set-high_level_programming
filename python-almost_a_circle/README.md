# Python - Almost a Circle

## Description
This project covers object-oriented programming (OOP) foundations in Python, including class inheritance, private attributes, getter/setter data validation, `*args` and `**kwargs`, object serialization/deserialization (JSON/CSV), and unit testing with `unittest`.

## Tasks Summary
- **0. Test suite**: All files, classes, and methods are unit tested using `unittest`.
- **1. Base Class**: Created `Base` class to manage `id` attribute across all future classes.
- **2. First Rectangle**: Created `Rectangle` class inheriting from `Base`.
- **3. Validate Attributes**: Implemented setters with `TypeError` and `ValueError` checks.
- **4. Area First**: Added `area()` method returning rectangle area.
- **5. Display #0**: Added `display()` method printing shape using `#`.
- **6. __str__**: Overrode standard `__str__` method.
- **7. Display #1**: Updated `display()` method handling `x` and `y` offsets.
- **8. Update #0**: Added `update(*args)` method for positional argument assignment.
- **9. Update #1**: Updated `update(*args, **kwargs)` method for keyword arguments.
- **10. And Now, the Square!**: Created `Square` class inheriting from `Rectangle`.
- **11. Square Size**: Added getter/setter property `size`.
- **12. Square Update**: Added `update(*args, **kwargs)` method for `Square`.
- **13. Rectangle Instance to Dictionary Representation**: Added `to_dictionary()`.
- **14. Square Instance to Dictionary Representation**: Added `to_dictionary()`.
- **15. Dictionary to JSON String**: Added static method `to_json_string()`.
- **16. JSON String to File**: Added class method `save_to_file()`.
- **17. JSON String to Dictionary**: Added static method `from_json_string()`.
- **18. Dictionary to Instance**: Added class method `create()`.
- **19. File to Instances**: Added class method `load_from_file()`.
- **20. JSON Okay, but CSV?**: Added CSV serialization `save_to_file_csv()` and deserialization `load_from_file_csv()`.
