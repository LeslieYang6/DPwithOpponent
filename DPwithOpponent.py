import random

def winwithmax(media,array,i,j):
    //使用已经记忆了的情况//
    if media[i][j]!=-1:
        return media[i][j]
    //解决basecase//
    if i+1==j:
        media[i][j]=max(array[i],array[j])
        return media[i][j]
    """
    假设对手也会选择对我最不利的情况，所以需要选择min下下次轮到我的选择
    """
    media[i][j]=max(min(winwithmax(media,array,i+2,j),winwithmax(media,array,i+1,j-1))+array[i],min(winwithmax(media,array,i,j-2),winwithmax(media,array,i+1,j-1))+array[j])
    return media[i][j]

def main():
    array=[4,5,8,7]

    media=[[-1 for i in range(4)] for j in range(4)]
    p=winwithmax(media,array,0,3)
    print(p)


main()