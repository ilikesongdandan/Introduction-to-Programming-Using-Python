# 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
# 但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
# 没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck! 
# 输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
# -*- coding:utf-8 -*-
class Solution:
#     *初始化small=1，big=2;
# *small到big序列和小于sum，big++;大于sum，small++;
# *当small增加到(1+sum)/2是停止
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum<3:
            return []
        small = 1
        big = 2
        result = []
        while small != int((1+tsum)/2):
            currentSum = self.SumOfList(small,big)
            if currentSum == tsum:
                res = []
                for i in range(small,big+1):
                    res.append(i)
                result.append(res)
                small +=1
                big +=1
            elif currentSum<tsum:
                big +=1
            else:
                small +=1
        return result

    
    def SumOfList(self,start,end):
        sum = (start+end)*(end-start+1)/2
        return sum

s= Solution()
print(s.FindContinuousSequence(3))