import os

# with open('../Desktop/c2.txt','r') as file:
#     content = file.read()
#     print(content)

# cnt = 0
# for dir , subdir , files in os.walk(os.getcwd()):
#     for file in files:
#         if file.endswith('.py'):
#             cnt += 1
#
# print(cnt)
# print(os.getcwd())
# with open('./intro/files.py','r') as file:
#     for line in file:
#         if not line.startswith('#') and line.strip():
#             print(line)

# with open ('../Desktop/output3.jpg','rb') as image:
#     content = image.read()
#     with open('./intro/img.jpg','wb') as out_image:
#         out_image.write(content)


# with open('../Desktop/test.txt','a') as test_file:
#     test_file.write('Hello , I\'m Hussein Sarea.\nHow are you\n')
#     test_file.write('\nEdited by: hussein sarea')

# cnt = 0
# for dir , subdirs , files in os.walk('../Desktop/tst'):
#     for file in files:
#         if file.endswith('.txt'):
#             with open(dir + '/' + file , 'a') as text_file:
#                 text_file.write('\nEdited by Hussein from python')
#             cnt += 1
#
# print(cnt)

# cnt = 0
# for dir , subdirs , files in os.walk('../Desktop'):
#     for file in files:
#         if file.endswith('.txt'):
#             cnt += 1
#
# print(cnt)
