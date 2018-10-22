# def hanoin(n, source, helper, target, cnt ):
#     if n > 0:
#         cnt = hanoin(n-1, source, target, helper, cnt)
#
#         if source[0]:
#             dick = source[0].pop()
#             cnt += 1
#
#             if cnt % 100 == 0:
#                 print(str(cnt))
#                 target[0].append(dick)
#
#         cnt = hanoin(n-1, helper, source, target, cnt)
# source = ([5,4, 3, 2, 1], 'A')
# helper = ([],'B')
# target = ([], 'C')
#
# cnt=0
# # import time
# # print('star'. time.time())
# cnt= hanoin(len(source[0]), source, helper, target, cnt)

def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        print( "    "*(3-height), "moveTower:", height, fromPole, toPole )
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole,height)
        moveTower(height-1,withPole,toPole,fromPole)
    #print(withPole)

def moveDisk(fp,tp,height):
    print("    "*(4-height), "moving disk", "~"*(height), "from",fp,"to",tp)


moveTower(3,"A","B","C")