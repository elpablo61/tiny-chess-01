import os as o,json,base64,urllib.request as u
# v3: PeSTO tapered eval + PVS search + aspiration windows; 0x88 board, 100k nodes/move
H=['AAAAADIyMjIKChQeBQUKGQAAABQF+/YABQoK7AAAAAA=','AAAAADIyMjIKChQeBQUKGQAAABQF+/YABQoK7AAAAAA=','ztji4tjsAADiAAoP4gUPFOIADxTiBQoP2OwABc7Y4uI=','ztji4tjsAADiAAoP4gUPFOIADxTiBQoP2OwABc7Y7OI=','7Pb29vYAAAD2AAUK9gUFCvYACgr2CgoK9gUAAOz29vY=','7Pb29vYAAAD2AAUK9gUFCvYACgr2CgoK9gUAAOz29vY=','AAAAAAUKCgr7AAAA+wAAAPsAAAD7AAAA+wAAAAAAAAU=','AAAAAAUKCgr7AAAA+wAAAPsAAAD7AAAA+wAAAAAAAAU=','4tjYzuLY2M7i2NjO4tjYzuzi4tj27OzsFBQAABQeCgA=','ztji7OLs9gDi9hQe4vYeKOL2Hiji9hQe4uIAAM7i4uI=']
F=['7Pb2+/v29uz2AAAAAAAA9vYABQUFBQD2+wAFBQUFAPsAAAUFBQUA+/YFBQUFBQD29gAFAAAAAPbs9vb7+/b27A==','7Pb2+/v29uz2AAAAAAAA9vYABQUFBQD2+wAFBQUFAPsAAAUFBQUA+/YFBQUFBQD29gAFAAAAAPbs9vb7+/b27A==']
M=[0,82,337,365,477,1025,20000]
P=[0,0,1,1,2,4,0]
def dc(s):
 b=base64.b64decode(s);return [((x+128)&255)-128 for x in b]
def mr(s):
 b=dc(s);return [x for r in range(8) for x in b[r*4:r*4+4]+b[r*4:r*4+4][::-1]]
D=[mr(x) for x in H[:8]]+[dc(F[0]),dc(F[1])]+[mr(x) for x in H[8:]]
T=[0]*3072
for a in range(6):
 for b in range(2):
  t=D[a*2+b];k=(a*4+b*2)*128
  for q in range(128):
   if q&0x88:continue
   T[k+q]=t[(7-(q>>4))*8+(q&7)]
   T[k+128+q]=-t[(q>>4)*8+(q&7)]
Z=[];_x=0x9E3779B97F4A7C15
for _ in range(1696):
 _x=(_x*6364136223846793005+1442695040888963407)&((1<<64)-1);Z.append(_x)
def zk(p,q):return Z[(p+6)*128+q]
ZS=Z[13*128];ZC=Z[13*128+1:13*128+17];ZE=Z[13*128+17:13*128+25]
B=[0]*128;N=[0]*13;U=[];S=1;C=H=G=V=Y=0;E=-1;W=4;X=116
NO=[14,18,31,33,-14,-18,-31,-33]
KO=[1,-1,16,-16,15,17,-15,-17]
RD=[1,-1,16,-16]
BD=[15,17,-15,-17]
def ps(p,q,h):
 return T[((abs(p)-1)*4+h*2+(p<0))*128+q]
def su(f):
 global B,S,C,E,H,G,V,Y,W,X,N,U
 B=[0]*128;N=[0]*13;U=[]
 a=f.split();r=a[0].split('/')
 for k,w in enumerate(r[::-1]):
  f=0
  for c in w:
   if c.isdigit():f+=int(c)
   else:
    j='PNBRQKpnbrqk'.find(c);p=j+1 if j<6 else 5-j
    q=k*16+f;B[q]=p;N[p+6]+=1
    if p==6:W=q
    elif p==-6:X=q
    f+=1
 S=1 if a[1]=='w' else -1;C=0
 if a[2]!='-':
  for c in a[2]:C|=1<<'KQkq'.find(c)
 E=-1
 if a[3]!='-':E=ord(a[3][0])-97+(int(a[3][1])-1)*16
 H=int(a[4])
 G=0;V=0;Y=0
 for q in range(128):
  p=B[q]
  if not p or q&0x88:continue
  G+=(M[abs(p)] if p>0 else -M[-p])+ps(p,q,0)
  V+=(M[abs(p)] if p>0 else -M[-p])+ps(p,q,1)
  Y^=zk(p,q)
 if S<0:Y^=ZS
 Y^=ZC[C]
 if E>=0:Y^=ZE[E&7]
def ak(q,y):
 for d in (15,17):
  t=q-d*y
  if not t&0x88 and B[t]==y:return 1
 k=2*y
 for d in NO:
  t=q+d
  if not t&0x88 and B[t]==k:return 1
 for d in KO:
  t=q+d
  if not t&0x88 and B[t]==6*y:return 1
 for d in RD+BD:
  t=q+d
  while not t&0x88:
   p=B[t]
   if p:
    if p==5*y or p==(4 if d in RD else 3)*y:return 1
    break
   t+=d
 return 0
def cc(k,t,r):
 d=1 if t>k else -1
 for q in range(k,t+d,d):
  if ak(q,-S):return 0
 q=k+d
 while q!=r:
  if B[q]:return 0
  q+=d
 return B[r]==4*S
def gn():
 m=[];s=S
 for q in range(128):
  p=B[q]
  if not p or p*s<0 or q&0x88:continue
  t=abs(p)
  if t==1:
   d=16*s;v=q+d
   if not v&0x88 and not B[v]:
    if (s>0 and v>=112) or (s<0 and v<8):
     for r in (5,4,3,2):m.append(q|(v<<7)|(r<<14))
    else:
     m.append(q|(v<<7))
     if (s>0 and q<32) or (s<0 and q>=96):
      w=q+2*d
      if not B[w]:m.append(q|(w<<7))
   for dd in (d-1,d+1):
    v=q+dd
    if v&0x88:continue
    o=B[v]
    if o and o*s<0:
     if (s>0 and v>=112) or (s<0 and v<8):
      for r in (5,4,3,2):m.append(q|(v<<7)|(r<<14))
     else:m.append(q|(v<<7))
    elif v==E:m.append(q|(v<<7))
  elif t==2:
   for d in NO:
    v=q+d
    if not v&0x88 and B[v]*s<=0:m.append(q|(v<<7))
  elif t==6:
   for d in KO:
    v=q+d
    if not v&0x88 and B[v]*s<=0:m.append(q|(v<<7))
   if s>0 and q==4:
    if C&1 and cc(4,6,7):m.append(4|(6<<7))
    if C&2 and cc(4,2,0):m.append(4|(2<<7))
   elif s<0 and q==116:
    if C&4 and cc(116,118,119):m.append(116|(118<<7))
    if C&8 and cc(116,114,112):m.append(116|(114<<7))
  else:
   ds=RD if t==4 else BD if t==3 else KO
   for d in ds:
    v=q+d
    while not v&0x88:
     o=B[v]
     if not o:m.append(q|(v<<7))
     else:
      if o*s<0:m.append(q|(v<<7))
      break
     v+=d
 return m
def lg():
 o=[]
 for m in gn():
  mk(m)
  if not ak(W if S<0 else X,S):o.append(m)
  um()
 return o
def mk(m):
 global S,C,E,H,G,V,Y,W,X
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7;p=B[f];s=S;cap=0;csq=t
 if abs(p)==1 and t==E and not B[t]:csq=t-16*s;cap=B[csq]
 else:cap=B[t]
 U.append((m,cap,csq,C,E,H,G,V,Y,W,X))
 Y^=zk(p,f)
 if cap:
  Y^=zk(cap,csq)
  G-=(M[abs(cap)] if cap>0 else -M[-cap])+ps(cap,csq,0)
  V-=(M[abs(cap)] if cap>0 else -M[-cap])+ps(cap,csq,1)
  N[cap+6]-=1;B[csq]=0
 G-=ps(p,f,0);V-=ps(p,f,1);B[f]=0
 np=pr*s if pr else p
 if pr:
  d=M[1] if p>0 else -M[1];G-=d;V-=d
  d=M[pr] if p>0 else -M[pr];G+=d;V+=d
  N[p+6]-=1;N[np+6]+=1
 B[t]=np;G+=ps(np,t,0);V+=ps(np,t,1);Y^=zk(np,t)
 if abs(p)==6:
  if p>0:W=t
  else:X=t
  if abs(t-f)==2:
   r0=f+3 if t>f else f-4;r1=f+1 if t>f else f-1
   G-=ps(4*s,r0,0);V-=ps(4*s,r0,1);B[r0]=0;B[r1]=4*s;G+=ps(4*s,r1,0);V+=ps(4*s,r1,1);Y^=zk(4*s,r0)^zk(4*s,r1)
 nc=C
 for a,b in ((4,3),(116,12),(0,2),(7,1),(112,8),(119,4)):
  if f==a or t==a:nc&=~b
 if nc!=C:Y^=ZC[C]^ZC[nc];C=nc
 if E>=0:Y^=ZE[E&7]
 E=-1
 if abs(p)==1 and abs(t-f)==32:E=(f+t)//2
 if E>=0:Y^=ZE[E&7]
 H=0 if cap or abs(p)==1 else H+1
 S=-s;Y^=ZS
def um():
 global S,C,E,H,G,V,Y,W,X
 m,cap,csq,oC,oE,oH,oG,oV,oY,oW,oX=U.pop()
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7;p=B[t];s=-S
 B[t]=0
 if pr:
  N[p+6]-=1;N[(1 if p>0 else -1)+6]+=1;p=1 if p>0 else -1
 B[f]=p
 if cap:B[csq]=cap;N[cap+6]+=1
 if abs(p)==6 and abs(t-f)==2:
  r1=f+1 if t>f else f-1;r0=f+3 if t>f else f-4;B[r1]=0;B[r0]=4*s
 C=oC;E=oE;H=oH;G=oG;V=oV;Y=oY;W=oW;X=oX;S=s
def mn():
 global S,E,Y,H
 U.append((0,0,-1,C,E,H,G,V,Y,W,X))
 if E>=0:Y^=ZE[E&7]
 E=-1;H+=1;S=-S;Y^=ZS
def ev():
 ph=0
 for q in range(1,6):ph+=(N[q+6]+N[-q+6])*P[q]
 if ph>24:ph=24
 if not(N[7] or N[5] or N[10] or N[2] or N[11] or N[1]):
  if N[8]+N[4]+N[9]+N[3]<=1:return 0
 return ((G*ph+V*(24-ph))//24+8)*S
MT=30000;TT={};KI=[[0,0] for _ in range(128)];HI=[0]*32768;ND=0;BG=100000;PC={}
class Ab(Exception):pass
def cp(m):
 t=(m>>7)&127;c=B[t]
 if c:return c
 f=m&127
 if abs(B[f])==1 and t==E:return -S if B[f]>0 else S
 return 0
def hn():
 return (N[8]+N[9]+N[10]+N[11]) if S>0 else (N[4]+N[3]+N[2]+N[1])
def od(ms,tm,pl):
 def sc(m):
  if m==tm:return 1<<20
  c=cp(m)
  if c:return 1000000+M[abs(c)]*10
  if m in KI[pl]:return 900000
  return HI[(0 if S>0 else 16384)+(m&16383)]
 return sorted(ms,key=sc,reverse=True)
def qs(a,b,pl):
 global ND
 ND+=1
 if ND>BG:raise Ab
 if H>=100:return 0
 st=ev()
 if st>=b:return b
 if st>a:a=st
 ch=ak(W if S>0 else X,-S)
 if ch:
  ms=[m for m in gn() if la(m)]
  if not ms:return -MT+pl
 else:
  ms=[m for m in gn() if cp(m) or ((m>>14)&7)]
 ms=od(ms,0,pl)
 for m in ms:
  if not ch:
   c=cp(m)
   if c and st+M[abs(c)]+200<a:continue
  mk(m)
  if ak(W if S<0 else X,S):um();continue
  sc=-qs(-b,-a,pl+1);um()
  if sc>=b:return b
  if sc>a:a=sc
 return a
def la(m):
 mk(m);o=not ak(W if S<0 else X,S);um();return o
def sr(d,a,b,pl):
 if PC.get(Y,0):return 0
 PC[Y]=1;r=_sr(d,a,b,pl);PC[Y]=0;return r
def _sr(d,a,b,pl):
 global ND
 ND+=1
 if ND>BG:raise Ab
 if H>=100:return 0
 if a<-MT+pl:a=-MT+pl
 if b>MT-pl:b=MT-pl
 if a>=b:return a
 e=TT.get(Y);tm=0
 if e and e[0]>=d:
  sc=e[1];fl=e[2];tm=e[3]
  if fl==0:return sc
  if fl==1:a=max(a,sc)
  else:b=min(b,sc)
  if a>=b:return sc
 ch=ak(W if S>0 else X,-S)
 if d<=0:return qs(a,b,pl)
 if d>=3 and not ch and b>-MT+1000 and hn():
  v=ev()
  if v>=b:
   mn();sc=-sr(d-4,-b,-b+1,pl+1);um()
   if sc>=b:return sc
 ms=od(gn(),tm,pl);bt=-MT-1;bm=0;oa=a
 for i,m in enumerate(ms):
  c=cp(m)
  mk(m)
  if ak(W if S<0 else X,S):um();continue
  if i==0:sc=-sr(d-1,-b,-a,pl+1)
  elif d>=3 and i>=3 and not c and not ch:
   sc=-sr(d-2,-a-1,-a,pl+1)
   if sc>a:sc=-sr(d-1,-b,-a,pl+1)
  else:
   sc=-sr(d-1,-a-1,-a,pl+1)
   if a<sc<b:sc=-sr(d-1,-b,-a,pl+1)
  um()
  if sc>bt:bt=sc;bm=m
  if sc>a:
   a=sc
   if not c:
    KI[pl][1]=KI[pl][0];KI[pl][0]=m
    HI[(0 if S>0 else 16384)+(m&16383)]+=d*d
  if a>=b:break
 if bt==-MT-1:return -MT+pl if ch else 0
 fl=1 if bt>=b else 0 if bt>oa else 2
 if len(TT)>65536:TT.clear()
 TT[Y]=(d,bt,fl,bm)
 return bt
def rp(o2,dp,a,b):
 cm=0;cs=-MT-1
 for i,m in enumerate(o2):
  mk(m)
  if ak(W if S<0 else X,S):um();continue
  if i==0:sc=-sr(dp-1,-b,-a,1)
  else:
   sc=-sr(dp-1,-a-1,-a,1)
   if a<sc<b:sc=-sr(dp-1,-b,-a,1)
  um()
  if sc>cs:cs=sc;cm=m
  if sc>a:a=sc
  if sc>=b:break
 return cm,cs
def rt():
 global ND
 ms=lg()
 if not ms:return None
 if len(ms)==1:return ms[0]
 PC.clear()
 PC[Y]=1
 bm=ms[0];bs=-MT-1;ND=0;mk0=len(U)
 for dp in range(1,65):
  try:
   o2=od(ms,bm,0)
   if dp>1 and bs>-MT-1:
    cm,cs=rp(o2,dp,max(-MT-1,bs-40),min(MT+1,bs+40))
    if cs<=bs-40 or cs>=bs+40:cm,cs=rp(o2,dp,-MT-1,MT+1)
   else:
    cm,cs=rp(o2,dp,-MT-1,MT+1)
   bm=cm;bs=cs
   if abs(cs)>=MT-1000:break
  except Ab:break
 while len(U)>mk0:um()
 PC.clear()
 return bm
RL=o.environ.get('MAKEFUN_ENV_URL','')
A='abcdefgh'
def po(p,o):
 q=u.Request(RL+p,data=json.dumps(o).encode())
 with u.urlopen(q,timeout=9) as r:return json.loads(r.read())
def uc(m):
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7
 s=A[f&7]+str((f>>4)+1)+A[t&7]+str((t>>4)+1)
 if pr:s+='nbrq'[pr-2]
 return s
def go():
 while 1:
  try:g=po('/game',{})
  except Exception:break
  st=g.get('status')
  if st=='done':break
  if st!='your_move':continue
  su(g['fen'])
  m=rt()
  if m is None:
   try:po('/resign',{'game':g['game']})
   except Exception:pass
   continue
  try:po('/move',{'game':g['game'],'move':uc(m)})
  except Exception:
   l=g.get('legal_moves')
   if l:po('/move',{'game':g['game'],'move':l[0]})
go()
