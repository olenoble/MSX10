10 CLS:DIM M(40,20):R=0.4:DIM D(32):for J=0 TO 31:READ D(J):NEXT J:J=RND(-TIME):WIDTH40
15 for K=0 TO 39:locate K,0,0: print CHR$(219):locate K,19,0:print CHR$(219):next K
20 for J=1 TO 18
30 M(0,J)=1+(RND(1)<R):M(1,J)=1:M(38,J)=1:M(39,J)=M(0,J)
31 LOCATE 0,J,0:print CHR$(219*(1-M(0,J)))
32 FOR K=2 TO 37:V=D(31-M(K+1,J-1)-2*M(K,J-1)-4*M(K-1,J-1)-8*M(K-1,J)-16*M(K-2,J))
34 IF V < 0 THEN M(K,J)= 1+(RND(1)<R) ELSE M(K,J)=V
36 LOCATE K,J,0:print CHR$(219*(1-M(K,J))):next K:LOCATE 39,J,0:print CHR$(219*(1-M(39,J)))
40 NEXT J
100 DATA 0,0,0,-1,1,1,-1,-1,0,0,0,0,-1,1,1,1,0,0,0,-1,1,1,1,1,-1,1,0,-1,-1,1,1,1
110 LOCATE 20,10,0:print "X":LOCATE 0,20
