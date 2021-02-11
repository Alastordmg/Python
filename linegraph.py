from matplotlib import pyplot as plt

x =['2000', '2001','2002','2003','2004','2005','2006','2007','2008','2009']
y1=[861,830,809,867,948,1129,1453,1656,1787,1611]
y2=[1196,1176,1269,1240,1307,1435,1601,1654,1803,1734]

plt.plot(x,y1, color='pink',marker='*',linestyle=':') #linestyle --,:
plt.plot(x,y2, color='gray',marker='o') #marker o,*,s

plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')
plt.title('Two Lines on One Graph')
plt.legend(['Deegrees','Incomes'], loc=4)
# plt.axis([2002,2008,1000,1400]) para hacer zoom a determinada parte
plt.show()