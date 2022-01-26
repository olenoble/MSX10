10 screen 2,2
20 w=16:h=12:c=0.75:d=0.25
30 s1=h:s2=w:c1=int(c*5*(s1+s2)):d1=int(d*((s1/2)*(s2/2))):dim m(s1,s2)
40 for i=0 to (s2-1):m(0,i)=0:m(s1-1,i)=0:next i
50 for i=0 to (s1-1):m(i,0)=0:m(i,s2-1)=0:next i
100 print c1:print d1