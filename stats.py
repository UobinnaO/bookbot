"""Des:functions for analyzing the text"""


def count_words(string):
    """return word count from string of words"""
    num_words = len(string.split())
    print(f"Found {num_words} total words")


def count_char(string):
    """counts each occurrence of each character"""
    countcharDic = {}
    for chr in string:
        if (chr.lower()) in countcharDic.keys():
            countcharDic[chr.lower()] += 1
        else:
            countcharDic[chr.lower()] = 1

    return countcharDic


def sort_Dict(dict):
    """input:dict of char and counts"""
    """return:sorted list of dictionaries"""

    def sort_on(dict):
        return dict["count"]

    _lst = []
    for key, Value in dict.items():
        if key.isalpha():
            _lst.append({"chr": key, "count": Value})

    _lst.sort(key=sort_on, reverse=True)

    return _lst
