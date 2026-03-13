import collections  # 导入collections模块，用于创建默认字典


class Solution(object):
    def groupAnagrams(self, strs):
        """
        将字符串数组中的字母异位词分组
        :type strs: List[str]  # 输入参数：字符串列表
        :rtype: List[List[str]]  # 返回值：分组后的字符串列表的列表
        """
        # 1. 创建一个默认字典，键是字符计数的元组，值是对应异位词的列表
        # defaultdict的特点是访问不存在的键时会自动创建空列表，避免KeyError
        hp = collections.defaultdict(list)

        # 2. 遍历输入的每个字符串
        for str in strs:
            # 3. 初始化长度为26的计数数组（对应a-z共26个小写字母），初始值都是0
            count = [0] * 26

            # 4. 遍历当前字符串的每个字符，统计每个字母出现的次数
            for ch in str:
                # ord(ch)获取字符的ASCII码，减去ord("a")得到0-25的索引（a=0, b=1...z=25）
                # 对应位置的计数+1
                count[ord(ch) - ord("a")] += 1

            # 5. 将计数数组转为元组（列表不能作为字典键，元组可以），作为字典的键
            # 把当前字符串添加到对应键的列表中（异位词的计数元组是相同的）
            hp[tuple(count)].append(str)

        # 6. 将字典的值（所有分组后的列表）转为列表返回
        return list(hp.values())