from termcolor import colored

def printMap(Map,enemies,colororder):
    for row in range(len(Map)):
        count = 0
        for column in range(len(Map[0])):
            count += 1
            if 'O' in Map[row] and count != len(Map[0]) : 
                if Map[row][column] == 'A':
                    print(colored('-','grey'), end = colored('----','grey'))
                else:
                    print(colored(Map[row][column],'grey'), end = colored('----','grey'))
            else:
                if Map[row][column] == 'Q':
                    for i in range(len(enemies)):
                        if [row,column] == enemies[i]:
                            print(colored(Map[row][column], colororder[i]),end = '    ')
                elif Map[row][column] == '.':
                    print(colored(Map[row][column],'red'), end = '    ')
                elif Map[row][column] == 'P':
                    print(colored(Map[row][column],'cyan', attrs=['bold']), end = '    ')
                elif Map[row][column] == 'X':
                    print(colored(Map[row][column],'red', attrs = ['bold']), end = '    ')
                else:
                    print(colored(Map[row][column],'grey'), end = '    ')    
        print()

def declareEmptySpaces(Map):
    empty = []
    for row in range(len(Map)):
        for column in range(len(Map[0])):
            if Map[row][column] == '.':
                empty.append([row,column])
    return empty
