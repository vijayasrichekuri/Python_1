# Topic: Dictionary in Python
# ------------------------------------------------------------
# A Dictionary stores data as key-value pairs.
# Keys must be unique and immutable.

student = {
    "name": "Vijaya Sri",
    "age": 21,
    "course": "AI & ML"
}

print("Student Dictionary:", student)
print("Student Name:", student["name"])  # accessing value by key
print("All Keys:", student.keys())       # returns all keys
print("All Values:", student.values())   # returns all values

# Explanation:
# Dictionaries are used for structured data
# Key → unique identifier, Value → stored information
