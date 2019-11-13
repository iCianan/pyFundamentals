# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note:
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".


def wordBreak(s, words):
    # dp[i] means s[:i+1] can be segmented into words in the wordDicts
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(len(s)):
        if dp[i]:
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in words:
                    dp[j] = True
    return dp[-1]

    def bruteWordBreak(s, wordDict):
        return word_Break(s, set(wordDict), 0)

    def word_Break(s, wordDict, start):
        if start == len(s):
            return True
        for end in range(start + 1, len(s)):
            if (wordDict.contains(s.substring(start, end)) and word_Break(s, wordDict, end)):
                return True
        return False


def main():
    sample = 'catsandog'
    sample2 = ['cats', 'dog', 'sand', 'and', 'cat']
    print(wordBreak(sample, sample2))


if __name__ == "__main__":
    main()
