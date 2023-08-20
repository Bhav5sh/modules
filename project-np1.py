import numpy as np
months=['november','december','january','february']
weeks=['week1','week2','week3','week4']
days=['monday','tuesday','wednesday','thrusday','friday','satuarday','sunday']
min_temps=[15,8,10,7,6,11,9,
           7,10,7,-13,10,8,15,
           14,8,10,14,14,10,6,
           8,7,15,13,14,15,13,
           10,10,12,9,15,12,8,
           14,6,13,14,6,6,15,
           11,15,10,15,12,13,11,
           6,9,9,14,15,9,14,
           2,5,2,5,6,3,6,
           4,3,5,5,4,7,8,
           2,4,5,4,6,3,3,
           8,2,5,5,4,6,2,
           7,8,-10,11,9,9,12,
           11,8,11,8,7,8,10,
           8,12,9,12,9,7,11,
           12,9,11,10,8,11,11
          ]
max_temps=[30,32,26,31,27,22,26,
           20,29,28,27,22,28,21,
           25,31,29,20,32,22,25,
           27,25,28,26,27,23,28,
           32,24,22,20,21,28,20,
           29,23,26,22,21,31,31,
           22,32,32,25,23,29,29,
           28,21,23,29,20,28,30,
           19,19,18,20,18,23,20,
           21,21,19,22,21,28,21,
           20,18,19,18,22,27,22,
           18,21,19,19,20,26,19,
           21,19,18,20,21,17,20,
           18,21,19,20,19,22,18,
           19,18,21,19,20,20,21,
           21,22,18,18,20,27,22
           ]
dates=[]
for month in months:
  for week in weeks:
    for day in days:
      dates.append(f'{month}  {week}  {day}')

n_array=np.array([[date, f'min_temp:{i}' , f'max_temp:{j}' ]for date,i,j in zip(dates,min_temps,max_temps)])
print('numpy  array of temp data in winter season of jaipur city:')
print(n_array)
print(f'dimension of ndarray:{n_array.ndim}')
print(f'shape of numpy array:{n_array.shape}')


arr=[]
for month in months:
  for week in weeks:
    if week=='week1':
      for day in days:
        arr.append(True)
    else:
      for day in days:
        arr.append(False)

newarr=n_array[arr]
print('Daily temp for first week of each month: ')
print(newarr)


last=[]
for month in months:
  for week in weeks:
    for day in days:
      if day=='tuesday':
        last.append(True)
      else:
        last.append(False)

third=n_array[last]
print('temp for tuesday of each month:')
print(third)


forth=[]
for month in months:
  if month=='december' or  month=='february':
    for week in weeks:
      for day in days:
        forth.append(True)
  else:
    for week in weeks:
      for day in days:
        forth.append(False)
newf=n_array[forth]
print('maximum temp for all weekdays of december and february:')
print(newf[0:,2])

five=[]
for month in months:
  if month=='november':
    for week in weeks:
      for day in days:
        five.append(True)
  else:
    for week in weeks:
      for day in days:
        five.append(False)
new2=n_array[five]
newl=new2[0:,1].tolist()

bh=[]
for item in newl:
  if int(item[9:])<8:
    bh.append(True)
  else:
    bh.append(False)
usb=new2[bh]
print('minimum temp was less than 8 degree in november monnth:')
print(usb)
print('all the days along with the week number in november.. when minimum temp was less than 8 degree in november monnth ')
print(usb[0:,0])

six=[]
for month in months:
  if month=='december' or  month=='january':
    for week in weeks:
      for day in days:
        six.append(True)
  else:
    for week in weeks:
      for day in days:
        six.append(False)
new5=n_array[six]
ko=new5[0:,2].tolist()
ha=[]
for x in ko:
  if int(x[9:])>20:
    ha.append(True)
  else:
    ha.append(False)
    
new3=new5[ha]
print('maximumm temp has crossed a 20 degree in dec and jan: ')
print(new3)
print('in date/week/month')
print(new3[0:,0])

max_list=n_array[0:,2].tolist()
yo=[]
for e in max_list:
  yo.append(int(e[9:]))
max_array=np.array(yo)
print('average max temp for winter mmonths in jaipur city:')
print(np.average(max_array))

nine=[]
for month in months:
  if month=='december':
    for week in weeks:
      for day in days:
        nine.append(True)
  else:
    for week in weeks:
      for day in days:
        nine.append(False)
rdx=n_array[nine]
dip=rdx[0:7,2].tolist()
kik=rdx[7:14,2].tolist()
ok=rdx[14:21,2].tolist()
pop=rdx[21:28,2].tolist()

ao=[]
for a in dip:
  # print(int(a[9:]))
  ao.append(int(a[9:]))
app=np.array(ao)
print('average temp of week1 in dec month:')
print(np.average(app))

jo=[]
for b in kik:
  # print(int(a[9:]))
  jo.append(int(b[9:]))
kiss=np.array(jo)
print('average temp of week2 in dec month:')
print(np.average(kiss))

ji=[]
for d in ok:
  # print(int(a[9:]))
  ji.append(int(d[9:]))
yes=np.array(ji)
print('average temp of week3 in dec month:')
print(np.average(yes))

jinu=[]
for d in pop:
  # print(int(a[9:]))
  jinu.append(int(d[9:]))
no=np.array(jinu)
print('average temp of week4 in dec month:')
print(np.average(no))

zip=rdx[0:,2].tolist()
so=[]
for a in zip:  
  so.append(int(a[9:]))
ip=rdx[0:,1].tolist()
ro=[]
for a in ip:  
  ro.append(int(a[9:]))
# pk=np.array(ro)
so.extend(ro)
pk=np.array(so)
print('average temp of december month:')
print(np.average(pk))

ten=[]
for month in months:
  if month=='january':
    for week in weeks:
      for day in days:
        ten.append(True)
  else:
    for week in weeks:
      for day in days:
        ten.append(False)
wow=n_array[ten]
dog=wow[0:,2].tolist()
di=[]
for a in dog:  
  # print(int(a[9:]))
  di.append(int(a[9:]))
go=wow[0:,1].tolist()
dy=[]
for a in go:  
  dy.append(int(a[9:]))
di.extend(dy)
hy=np.array(di)
print('average temp of january month:')
print(np.average(hy))
fi=so+di
print('overall average temp of december and january month:')
print(np.average(fi))

t1=[]
for month in months:
  if month=='february':
    for week in weeks:
      for day in days:
        t1.append(True)
  else:
    for week in weeks:
      for day in days:
        t1.append(False)
b1=n_array[t1]
h1=b1[0:,2].tolist()
uk=[]
for a in h1:
  uk.append(int(a[9:]))
max_num=np.array(uk)
print('maximum temp in february month: ')
print(np.max(max_num))
print('date of  maximum temp in month/week/day:')
print(b1[np.argmax(max_num),0])

