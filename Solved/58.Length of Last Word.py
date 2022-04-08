def lengthOfLastWord(s):

    if (s.split(" ")[-1].isalnum()):
        return len(s.split(" ")[-1])
    else:
        i = -1
        while(not s.split(" ")[i].isalnum()):
            i -= 1
        return len(s.split(" ")[i])
