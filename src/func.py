
# 众数计算

def caluMaxNumber(list):
    list_set=set(list)#取list的集合，去除重复元素
    frequency_dict={}
    for i in list_set:#遍历每一个list的元素，得到该元素何其对应的个数.count(i)
        frequency_dict[i]=list.count(i)#创建dict; new_dict[key]=value
    grade_mode=0
    for key,value in frequency_dict.items():#遍历dict的key and value。key:value
        if value==max(frequency_dict.values()):
            grade_mode = key
    return list.count(grade_mode)


# 均值计算
def calAverValue(list):
    num = 0
    for number in list:
        num += number

    return num/len(list)

# 二分查找
def binary_chop(alist, data):
    """
    非递归解决二分查找
    :param alist:
    :return:
    """
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (last + first) // 2
        if alist[mid] > data:
            last = mid - 1
        elif alist[mid] < data:
            first = mid + 1
        else:
            low = mid
            high = mid

            while low != 0:
                if alist[low] != data:
                    low = low+1
                    break
                low = low -1

            while high != n-1:
                if alist[high] != data:
                    high = high-1
                    break
                high = high+1

            return [low,high]
    return []
