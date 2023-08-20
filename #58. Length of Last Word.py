#58. Length of Last Word



"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

"""
def len_last_word(s):
    # Remove trailing spaces
    s = s.rstrip()
    
    # Split the string into words using spaces as separators
    word = s.split(' ')
    
    # Check if there are any words
    if word:
        # Get the last word and return its length
        return len(word[-1])
    else:
        return 0  # No words found

s_input = "asma hilal aljabri"
output = len_last_word(s_input)
print(output)  
