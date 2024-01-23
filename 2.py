f=open('mat_dv.txt','r')
L=[]
for i in f:
    i=i.strip('\n')
    L.append(i)

L2=['8','9','10','11']
d_8={'Name': '', 'Last name': '', 'Alg': 0, 'Geom': 0, 'Max': 0}
d_9={'Name': '', 'Last name': '', 'Alg': 0, 'Geom': 0, 'Max': 0}
d_10={'Name': '', 'Last name': '', 'Alg': 0, 'Geom': 0, 'Max': 0}
d_11={'Name': '', 'Last name': '', 'Alg': 0, 'Geom': 0, 'Max': 0}
for i in L:
    L1=i.split(' ')
    if L1[2]==L2[0] and (int(L1[3]) + int(L1[4]) >d_8['Max']):
        d_8['Max']=int(L1[3])+int(L1[4])
        d_8['Name']=L1[0]
        d_8['Last name']=L1[1]
        d_8['Alg']=L1[3]
        d_8['Geom']=L1[4]
    if L1[2]==L2[1] and (int(L1[3]) + int(L1[4]) >d_9['Max']):
        d_9['Max']=int(L1[3])+int(L1[4])
        d_9['Name']=L1[0]
        d_9['Last name']=L1[1]
        d_9['Alg']=L1[3]
        d_9['Geom']=L1[4]
    if L1[2]==L2[2] and (int(L1[3]) + int(L1[4]) >d_10['Max']):
        d_10['Max']=int(L1[3])+int(L1[4])
        d_10['Name']=L1[0]
        d_10['Last name']=L1[1]
        d_10['Alg']=L1[3]
        d_10['Geom']=L1[4]
    if L1[2]==L2[3] and (int(L1[3]) + int(L1[4]) >d_11['Max']):
        d_11['Max']=int(L1[3])+int(L1[4])
        d_11['Name']=L1[0]
        d_11['Last name']=L1[1]
        d_11['Alg']=L1[3]
        d_11['Geom']=L1[4]

print(d_8['Name'], d_8['Last name'], d_8['Alg'], d_8['Geom'])
print(d_9['Name'], d_9['Last name'], d_9['Alg'], d_9['Geom'])
print(d_10['Name'], d_10['Last name'], d_10['Alg'], d_10['Geom'])
print(d_11['Name'], d_11['Last name'], d_11['Alg'], d_11['Geom'])
print()

max_alg=0
max_geom=0
s_alg=''
s_geom=''
for i in L:
    L1=i.split(' ')
    if int(L1[3])>max_alg:
        max_alg=int(L1[3])
        s_alg=L1[0]+' '+L1[1]+' '+L1[2]
    elif int(L1[3])==max_alg:
        s_alg+=','+L1[0]+' '+L1[1]+' '+L1[2]
    if int(L1[4])>max_geom:
        max_geom=int(L1[4])
        s_geom=L1[0]+' '+L1[1]+' '+L1[2]
    elif int(L1[4])==max_geom:
        s_geom+=','+L1[0]+' '+L1[1]+' '+L1[2]

print(s_alg)
print(s_geom)



