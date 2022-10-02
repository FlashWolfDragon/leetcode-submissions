/*
 * @lc app=leetcode id=20 lang=csharp
 *
 * [20] Valid Parentheses
 */

// @lc code=start
public class Solution
{
    public bool IsValid(string s)
    {
<<<<<<< HEAD
        var dict = new System.Collections.Generic.Dictionary<char, char> {{')', '('}, {']', '['}, {'}', '{'}};
=======
        var dict = new System.Collections.Generic.Dictionary<char, char> { { ')', '(' }, { ']', '[' }, { '}', '{' } };
>>>>>>> c42b797 (Initial Commit)
        var stack = new System.Collections.Generic.Stack<char>();

        foreach (var c in s)
        {
            stack.Push(c);

            if (dict.ContainsKey(c))
            {
                stack.Pop();
<<<<<<< HEAD
                
=======

>>>>>>> c42b797 (Initial Commit)
                if (stack.Count == 0)
                    return false;

                var brace = stack.Pop();
                if (dict[c] != brace)
                    return false;
            }

        }

        return stack.Count == 0;
    }
}
// @lc code=end

<<<<<<< HEAD
var solution = new Solution();
Console.WriteLine(solution.IsValid("()"));
=======
// var solution = new Solution();
// Console.WriteLine(solution.IsValid("()"));
>>>>>>> c42b797 (Initial Commit)
