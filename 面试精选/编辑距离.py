# -*- coding:utf-8 -*-
# @Time    : 2019/9/2 15:28
# @Author  : Junwu Yu

'''
https://mp.weixin.qq.com/s?__biz=MzUyNjQxNjYyMg==&mid=2247486327&idx=3&sn=34994866cc0d9e5cb3969b6516263f63&chksm=fa0e64f6cd79ede084aeff5b0464104b0d43f4ba627318e641309344a41d9b2239254ddd8d63&scene=0&xtrack=1&key=7cc4803a8502bf684bc61d9246dc304c5233867eef7962bcc5521697c9e0418fbcb64c0322c0cacdfce9e06b37a52203ec569902c925f69d5fe71c5a038b2eb91aa799695b10fa383a9782604dfd079e&ascene=1&uin=OTI5MDI4MzA0&devicetype=Windows+10&version=62060844&lang=zh_CN&pass_ticket=ekGc3YOPyxWeui0T1uMkiFM5L1LIrmgMQ31S2BbyjtWYus%2BR9cNrnd0M7WPzCYz7

给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
插入一个字符;删除一个字符;替换一个字符

输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

解决两个字符串的动态规划问题，一般都是用两个指针i,j分别指向两个字符串的最后，然后一步步往前走，缩小问题的规模。
base case 是i走完s1或j走完s2，可以直接返回另一个字符串剩下的长度。
对于每对字符s1[i]和s2[j]，可以有四种操作：
if s1[i] == s2[j]:
    啥都别做（skip）
    i, j 同时向前移动
else:
    三选一：
        插入（insert）
        删除（delete）
        替换（replace）

'''


def miniDistance(s1, s2):
    def dp(i, j):
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1

        if s1[i] == s2[j]:
            # 解释：
            # 本来就相等，不需要任何操作
            # s1[0..i] 和 s2[0..j] 的最小编辑距离等于
            # s1[0..i-1] 和 s2[0..j-1] 的最小编辑距离
            # 也就是说 dp(i, j) 等于 dp(i-1, j-1)
            return dp(i - 1, j - 1)
        else:
            return min(
                dp(i, j - 1) + 1,  # 插入
                # 直接在 s1[i] 插入一个和 s2[j] 一样的字符
                # 那么 s2[j] 就被匹配了，前移 j，继续跟 i 对比
                # 别忘了操作数加一

                dp(i - 1, j) + 1,  # 删除
                # 我直接把 s[i] 这个字符删掉
                # 前移 i，继续跟 j 对比
                # 操作数加一

                dp(i - 1, j - 1) + 1  # 替换
                # 直接把 s1[i] 替换成 s2[j]，这样它俩就匹配了
                # 同时前移 i，j 继续对比
                # 操作数加一
            )

    return dp(len(s1) - 1, len(s2) - 1)


d = miniDistance('rad', 'apple')
print(d)
