print('\n'.join([''.join([('IloveU'[(x-y)%len('IloveU')]\
    if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 \
    else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))
print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x*y) \
    for y in range(1, x+1)]) for x in range(1, 10)]))

for y in range(15, -15, -1):#表示从15- -15每隔一个单位取一次值，
    ls=[]
    for x in range(-30, 30):
        tp=((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
        if tp<=0:  ##点在图像内部
            a=''.join('IloveU'[(x - y) % 6]) #加字母
        else:   ##点在图像外部
            a=''.join(' ')
        ls.append(a)
    s=''.join(ls)
    print(s)

text = "IloveU"
for y in range(15, -15, -1):#表示从15- -15每隔一个单位取一次值，
    ls=[]
    for x in range(-30, 30):
        tp=((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
        if tp<=0:  ##点在图像内部
            a=''.join(text[(x - y) % len(text)]) #加字母
        else:   ##点在图像外部
            a=''.join(' ')
        ls.append(a)
    s=''.join(ls)
    print(s)
