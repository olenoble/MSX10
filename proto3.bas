10 C=0:S=0.15:F=22/49:WIDTH40
20 CLS:J=RND(-TIME):DIM M(40,20):FOR I=1 TO 9:for J=2 TO 19
25 M(J,I)=S-RND(1):M(39-J,I)=M(J,I):M(J,19-I)=M(J,I):M(39-J,19-I)=M(J,I)
27 NEXT J:NEXT I
30 FOR I=0 TO 19:for J=0 TO 39
40 V=SIN(F*I*(I-19))*SIN(F*J*(J-39))+M(J,I)
41 V2=-(V>=C):LOCATE J,I,0:print CHR$(219*V2)
50 NEXT J:NEXT I
110 LOCATE 20,10,0:print "X":LOCATE 0,20
