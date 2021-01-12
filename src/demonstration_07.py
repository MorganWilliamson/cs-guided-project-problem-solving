"""
Challenge #7:

Given a string of lowercase and uppercase alpha characters, write a function
that returns a string where each character repeats in an increasing pattern,
starting at 1. Each character repetition starts with a capital letter and the
rest of the repeated characters are lowercase. Each repetition segment is
separated by a `-` character.

Examples:
- repeat_it("abcd") -> "A-Bb-Ccc-Dddd"  a-b-c-d
- repeat_it("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
- repeat_it("cwAt") -> "C-Ww-Aaa-Tttt"

Understanding:
- Repeating the first character once, the second character twice. 
- What if there are non alpha characters in the string, including whitespace?
    - These are addressed in the question, we don't need to worry about them. 
- What if input is an empty string? 
    - Return an empty string.
- Can you simplify the output for the planning step?
"""
# Capitalize to capitalize the first character, and convert all other characters to lower case. 

def repeat_it(input_str):
    # Check for empty string
    if input_str == "":
        return ""
    # Convert to a list to separate the characters
    input_list = list(input_str)

    result_list = []
    # Loop through the list 
    for reps, char in enumerate(input_list):
        # Repeat the character
        """
        repeated_char = ""
        for _ in range(reps + 1):
            repeated_char += char
        """
        repeated_char = char * (reps + 1) # Quicker repeat method: You can multiply strings/characters to repeat them.
        # Capitalize the new strings
        repeated_char = repeated_char.capitalize()
        # Add items to a result list
        result_list.append(repeated_char)
    # Join back as a string with hyphens (-)
    result_str = "-".join(result_list)
    # Return the string
    return result_str

print(repeat_it("abcd")) # -> "A-Bb-Ccc-Dddd"  
print(repeat_it("RqaEzty")) # -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
print(repeat_it("cwAt")) # -> "C-Ww-Aaa-Tttt"