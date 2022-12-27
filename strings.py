Python 3.10.7 (v3.10.7:6cc6b13308, Sep  5 2022, 14:02:52) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a="Amit Kumar"
>>> print(len(a))
10
>>> first_name="Amit"
>>> last_name="Kumar"
>>> full_name=first_name + last_name
>>> print(full_name)
AmitKumar
>>> full_name=first_name + " " +last_name
... print(full_name)
SyntaxError: multiple statements found while compiling a single statement
>>> full_name=first_name + " " + last_name
... print(full_name)
SyntaxError: multiple statements found while compiling a single statement
>>> first_name="Amit"
... last_name="Kumar"
... full_name=first_name + " " + last_name
... print(full_name)
SyntaxError: multiple statements found while compiling a single statement
