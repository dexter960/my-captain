print("program to find extension of the file")
while(True):

    a=input('enter the filename with extension: ')
    if (not a):
        break
    if (a.endswith('.py')) :
        print('extension of the flle is "python"')
    elif(a.endswith('.exe')):
        print('extension of the file is "executable"')
    elif(a.endswith('.c')):
        print('extension of the file is "c"')
    else:
        print('please enter the filename properly')

