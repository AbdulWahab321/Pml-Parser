# Pml
Pyml is just like XML but it is very easy to retrieve data using this library!
The syntax is like:



## Basic Syntax
```
[example programming language="python";age=13;hobby="Coding";]
    [<name>]
        Abdul Wahab
    [</name>]
[/example]
```
## Retrieving data
```
import pyml
my_age = pyml.get_tag_property("example","age")
print(my_age)
my_name = pyml.get_sub_tag_value("example","name").get_value()
print(my_name)
```
