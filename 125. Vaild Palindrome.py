def checkPalindrome(s: str):

    # 문자와 숫자만 추출
    sentence = []
    for char in s:
        if char.isalnum():
            sentence.append(char.lower())

    # 양 끝 문자 비교
    while len(sentence) > 1:
        if sentence.pop(0) != sentence.pop():
            return False

    return True
