s = "ab##"
t = "c#d#1"

print (max(len(s),len(t)))

# s_stack = []
# t_stack = []


# for i in range(len(s)):
#     if s[i] == '#':
#         if len(s_stack) == 0:
#             print(False,'s')
#             break
#         s_stack.pop()
#     else: 
#         s_stack.append(s[i])
    
#     if t[i] == '#':
#         if len(t_stack) == 0:
#             continue
#         t_stack.pop()
#     else:
#         t_stack.append(t[i])
# print( s_stack == t_stack)
