# 패키지로서 import 하기 위해 필요한 파일 : 패키지 임을 알려주는 파일일
'''
sample_pack/__init__.py
sample_pack 패키지를 import 할 때, 자동 실행되는 파일 ex) 환경 설정, 빈 파일도 관계 없음
최초 호출에만 초기화되고 이후 unload 후 다시 import해도 작동하는 내용이 아님 : 임시메모리를 사용하여 실용성을 올린 듯
'''
print('sample_pack 패키지를 load 했습니다.')