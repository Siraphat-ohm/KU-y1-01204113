# text = "acababababaccbabab"
# sub = "abc"
# #
# text = "AAAGTGTGTCTGAC"
# sub = "GTAT"

text = "acababababaccbabab"
sub = "aba"


def count_dis(s, p):
    return sum(1 for a, b in zip(s, p) if a != b)


length = len(text)
len_s = len(sub)
i = 0
l = i + len_s
appears = []


def add_highlight(start, end):
    appears.append((start, end))


while l <= length:
    if text[i:l] == sub:
        add_highlight(i, l)
        i = l
        l = i + len_s
    else:
        i += 1
        l = i + len_s

if appears:
    result = ""
    for k in range(length):
        if appears and k in range(appears[0][0], appears[0][1]):
            if k == appears[0][1] - 1:
                result += f"[{text[appears[0][0]:appears[0][1]]}]"
                appears.pop(0)
        else:
            result += text[k]
    print(result)
else:
    i = 0
    l = i + len_s
    appears = []
    while l <= length:
        if count_dis(sub, text[i:l]) == 1:
            add_highlight(i, l)
            i = l
            l = i + len_s
        else:
            i += 1
            l = i + len_s

    result = ""
    k = 0
    while k < length:
        if appears and k in range(appears[0][0], appears[0][1]):
            if k == appears[0][1] - 1:
                result += "["
                for f, c in zip(text[appears[0][0] : appears[0][1]], sub):
                    result += "?" if f != c else f
                result += "]"
                appears.pop(0)
        else:
            result += text[k]
        k += 1
    print(result)
