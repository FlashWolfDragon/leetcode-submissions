/*
 * @lc app=leetcode id=14 lang=csharp
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
public class Solution
{
    public string LongestCommonPrefix(string[] strs)
    {
        var min = int.MaxValue;
        foreach (var s in strs)
        {
            var currentLength = s.Length;

            if (currentLength < min)
                min = currentLength;
        }

        var result = new System.Text.StringBuilder();
        for (int i = 0; i < min; i++)
        {
            var currentLetter = strs[0][i];

            foreach (var word in strs)
            {
                if (word[i] != currentLetter)
                    return result.ToString();
            }
            result.Append(currentLetter);
        }

        return result.ToString();
    }
}
// @lc code=end


// var x = new Solution();
// Console.WriteLine(x.LongestCommonPrefix(new string[] { "flower", "flow", "flight" }));