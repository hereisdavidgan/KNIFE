## [387. 字符串中的第一个唯一字符](https://leetcode-cn.com/problems/first-unique-character-in-a-string/)

> 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
> **示例：**
> s = "leetcode"
> 返回 0
> s = "loveleetcode"
> 返回 2

和出现次数有关的，不要犹豫，hash

~~~python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        fre = collections.Counter(s)
        for i, ch in enumerate(s):
            if fre[ch] == 1:
                return i
        return -1
~~~

> 执行用时：72 ms, 在所有 Python3 提交中击败了93.73%的用户
> 内存消耗：15.1 MB, 在所有 Python3 提交中击败了43.01%的用户
#########################################################
## [383. 赎金信](https://leetcode-cn.com/problems/ransom-note/)

>给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。如果可以构成，返回 true ；否则返回 false。
>(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。)
>
>**示例 1：**
>**输入：**ransomNote = "a", magazine = "b"
>输出：false
>
>**示例 2：**
>**输入：**ransomNote = "aa", magazine = "ab"
>**输出：**false
>
>**示例 3：**
>**输入：**ransomNote = "aa", magazine = "aab"
>**输出：**true

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = dict(collections.Counter(ransomNote))
        for k, v in a.items():
            if magazine.count(k) < v:
                return False
        return True
```

> 执行用时：44 ms, 在所有 Python3 提交中击败了92.08%的用户
> 内存消耗：14.9 MB, 在所有 Python3 提交中击败了95.34%的用户