# My Code - 테스크테이스는 통과하는데 Time Limit Exceeded 발생.
class Solution(object):
    def trap(self, height):
        my_dict = {}
        # 각 층별 블록 갯수 dict 생성
        for i in range(max(height)):
            li = []
            for j in range(len(height)):
                if height[j] == 0:
                    li.append(0)
                else:
                    li.append(1)
                    height[j] = height[j] - 1
            my_dict[i] = li
        
        # 각 층별 1사이에 있는 0 갯수 합 구하기
        sum = 0
        for i in range(len(my_dict)):
            a = my_dict[i]
            while 1 in a:
                idx1 = a.index(1)
                try:
                    idx2 = a[idx1+1:].index(1)
                except:
                    break
                sum += idx2
                a = a[idx1+idx2+1:]
        return sum
        

