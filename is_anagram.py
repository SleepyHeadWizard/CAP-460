'''Create a Python function to check whether two given strings are anagrams of each other. 
Note:-An anagram is a word or phrase that is formed by rearranging the letters of another word or phrase, using each letter exactly once. To be an anagram, both the original and rearranged words must have the same letters in the same quantities. 
 
Example 1: 
Words: "listen" and "silent" 
Explanation: Both "listen" and "silent" contain the letters l, i, s, t, e, n. When these letters are rearranged, you can get the other word, so they are anagrams. 
Example 2: 
Words: "triangle" and "integral" 
Explanation: Both words contain the letters t, r, i, a, n, g, l, e in different orders, making them anagrams. 
Example 3: 
Phrases with spaces: "rail safety" and "fairy tales" 
Explanation: Ignoring spaces, both phrases contain the same letters r, a, i, l, s, a, f, e, t, y, arranged differently, so they are anagrams.'''


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    return sorted(s1) == sorted(s2)
    

if is_anagram(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams')
else:
    print(f'"{string1}" and "{string2}" are not anagrams')