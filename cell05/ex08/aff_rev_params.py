import sys

argv = sys.argv
argv.reverse()

for i in range(len(sys.argv)-1):
    print(argv[i])
