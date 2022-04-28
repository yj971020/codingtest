n=list(input())
#혹은 input() 대신 sys.stdin.readline().rstrip()
print(''.join(sorted(n,reverse=True)))