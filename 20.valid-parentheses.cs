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
        var dict = new System.Collections.Generic.Dictionary<char, char> {{')', '('}, {']', '['}, {'}', '{'}};
        var stack = new System.Collections.Generic.Stack<char>();

        foreach (var c in s)
        {
            stack.Push(c);

            if (dict.ContainsKey(c))
            {
                stack.Pop();
                
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

var solution = new Solution();
Console.WriteLine(solution.IsValid("()"));
