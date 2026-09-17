"""
Given a string s. The task is to find the first repeated character in it. We need to find the character that occurs more than once and whose index of second occurrence is smallest. s contains only lowercase letters.

Examples :

Input: s ="geeksforgeeks"
Output: "e"
Explanation: 'e' repeats at third position.
Input: s ="hellogeeks"
Output: "l"
Explanation: 'l' repeats at fourth position.
Input: s ="abc"
Output: "-1"
Explanation: There is no repeated character.
Constraints:
1 ≤ s.size() ≤ 105


"""
class Solution:
    def firstRepChar(self, s):
        # code here
        rep=[]
        for i in s:
            if i not in rep:
                rep.append(i)
            else:
                return i

        return -1
