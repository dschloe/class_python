#!/venv/bin/python
# -*- coding: utf-8 -*-

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():  # isalnum(): 영문자, 숫자 여부 판별하여 False, True 변환
                strs.append(char.lower())  # 모든 문자 소문자 변환하여 str에 입력
                print('문자 처리: ', strs)

        # 팰린드롬 여부 판별
        while len(strs) > 1:  # strs의 길이가 1 이상이면 반복

            # pop(0): 맨 앞의 값, pop(): 맨 뒤의 값을 가져옴
            if strs.pop(0) != strs.pop():
                return False
        return True

if __name__ == '__main__':
    print('실행합니다: main')
    # 현재 스크립트 파일이 프로그램 시작점이 맞는지 판단
    # 스크립트 파일이 메인 프로그램으로 사용될 때와 모듈로 사용될 때를 구분하기 위함

    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a car"))