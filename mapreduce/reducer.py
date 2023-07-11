#!/usr/bin/env python
# 데이터 구성요소들을 소트하고자 할 때 사용하는 것으로
# 키 밸류 쌍(key-value pair)으로 검색(retrieve)하고자 할 때 사용함.
# 결국 키 밸류 쌍을 구성하고자 itemgetter를 사용함.
from operator import itemgetter
# sys
import sys

current_word = None # 값을 초기화할 경우 혹은 정의되지 않는 변수값 정의
current_count = 0 # 현재 변수를 숫자로 초기화하며 숫자 0 제로를 정의하는 숫자형 변수
word = None 

# STDIN (맵 단계를 거쳐 나온 결과값이 이제 입력값으로 시작됨
for line in sys.stdin:
   # 빈 스페이스들을 제거하는 과정
    line = line.strip()
   # 맵 단계에서 가져온 입력값(Input data)을 파싱하는 과정
   # 개별 단어들을 키로서 파싱할 때 ‘\t’ 곧 탭을 다음에 넣으라는 지시
   # 동시에 별류(Value)는 모든 값을 1로 지정.
    word, count = line.split('\t', 1)
   # 스트링으로 가지고 온 카운트 값을 Int 값으로 변환하여 컨버팅하는 과정
    try:
        count = int(count)
    except ValueError:
       # 숫자가 없는 카운트 값은 무시하고 진행
        continue
   # if 문장으로 비교하고자 하는 현재 텍스트 단어(current_word)가 
   # 맵에서 가지고 온 단어(word)와
# 비교하여 같으면 current_count 값을 count 값 만큼 증가시키라는 말, 
   # 만약 같은 단어가 있다면 하나씩 더 증가하게 됨.
   # 비교하고자 하는 현재 텍스트와 맵에서 가지고 온 단어와 다르면
   # 화면에 출력하게 된다. 
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print( '%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word
   # 최종적으로 비교하려는 현재 텍스트 단어와 맵에서 가지고 온 단어가 같은    
   # 값이라면 최종적으로 단순히 출력하게 하려는 코드.
if current_word == word:
    print( '%s\t%s' % (current_word, current_count))
