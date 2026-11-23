import json,os,sys,urllib.request,zlib,base64
X=b'c-oa$TXWh-7JlbfC=Z@)p%#{eJpn20sxZlHww$<ZaOEMaiV{e81V{+AxY$$K-@fN`w?I(Yhk-)s%ej8%(oLEb>#{P$t7v`af0IYzyN<)i1M#~aya({^!h1;kTU>vV`!KjCK0G_{{Mq^g7=htdkxL>^QrO*}txsx`+Mdg7w+}y$**(@{@P?`9nv#v$F6{SNpSid)lq(KUGx$2D6sl-&wXZgS*g^WA!KX3k3pu==NZ5*#x$%)snP7X<ZyED-X~cq6FGiXhlv1g~Nax1hNLC^-sFa6lABo8*2zekOVxT7XIJqY#ic+#rPAqVWQl?{J#UbYu6&!_DFP+tTpOh5%%B0$sx#1p7DFle1D13;*hfiA70B3`z|D$WcK@kr2f2FGg^e#Xv#$aLb_-M=`MA@j}XiFh}Ws4p;60U#IH`F<0dp0XsQt-E6$j4#Jz|A6}DO*UJK<MK7+I7HPuc4tYH>JfJw3s{%2N3mPCn}00k16uAO@m=`w8#WTT)H481b0wi$_f;j<l8JMqbi}(+7h`=jLv^@VgO;$NyQdKfYf(<@6XnGmFC+7Xt%uR=pDtm1>hjprOg~ts$rSy)SgJ}=^RpR&gPb@T!bj3Dhj|uW6tMBl*gxFm|zKw->GG~;5;dCMaCsxR}G76wlk|uQ>&>#R}(Prs4CU?_Zmib&03r_*GX{(r#07rDyYvq{50N%m#$r8*gx_>+yAR@8mA<Er{x-3DewW>#k5SKr6N)pjV6{ewwyB&vvSRny(}9j{9CC0E`z>6J)A&@>>D|~VV>H9a;80;s6E%LlV(=_R?cK_mh-z?$K-sk9a+w;a*c&dN`jP$1{aFdJdp^jbvg3da*TeUI1%4D=n(GN-8vhP4^X4nkHC>+Z(3>yf|@fFhI6wKIH0e06n?s7hq7e9(KnV|7A<03lspTje3gm{Y9%PZ+B6IrH4xwen%6qjf;3d6>sdbgm{Vs3vVeLy=e}3m(NxfdodTjBVtrt*oTgTnrBFNAH||m?fTj?S)OOK~*AR?5gaJO3NU69eWj!|(_z*V!U)pUJs;3)-Y^IF{CFlJf>$}YB;R&Oe-47q2`S)yLUSGfet=j;Ukj`QaOjDC#hD$iX^aT)l7Z5d^bd(*cfqsTC%G?*+`3HTg*`-P@OFNkJ^vZQ?H<<DFHtO@*bNjuihb10WXVHA)jm{VB_;)Divo^Q0pj+4_uDmImOS@~fZ>?F~5P)LV{-g7fRCEh<WYPWwxo5V$Hbr?*48SEUzH1QJyCas(gU1#Un=f?7isR9<vkN5I-Sy!np)uT9YVCvFT$IcsNb{IQY|0AmAc8Ne^)y-;KiFU-6XeGo|N6}zhhqo4{$X)A+76A1Sjzl7*+iBkm@WB7dSHi6n#ak3E_K+=pyJQZ5`{MyXS^DFA+lDQRi%6^6QNR1(0a$!3f=kq3$4a(2;Q1^e0ua)vSAm9F|TJ!nFu@n8En|=6KQu&Z$vzc4m4srGspxVXELQSOdLF_k>fDVK-H;{;!GbmF!n+~L&g@^k)>s1q9fq4N0-SfUq#t8j*QHw8Ru1Iw)^s9QRD=X#BAe5&vC5pW38ypw~&>|E-6LAT@aer=`L-{<V|J6Rc}(BeWV)ziQ(fC?`HPr5V>G5;)9W)q)Eh}RwVQoYbY&yL^mw9T@?mZe$1XSJ7R_9YK7u1@*^%#*e}JvQiN!$s6oId6OmMDm1L6%*iB>h1&Y}&OmM*rbWEmo42@g``xr`1U~9Z&BF~m}Z>Y;6lF2N*4ULX0H`cn0X#~KSz}-&s3MOu7wjMb#NV{(l=n#_c&j&ikq^bD4BZ^g8L7^XbB~$)*kQ3MI-rWBFzDN86KXl5ZSVgl0+<^p<!eeZC%`I|G80avtq-P};+YFmzs@vD>ynT`Tr{#vo)RQ|{9H$og*!C<i+B!(1Ets-OCM4MttVQ&^8h1m<j{`_Do75<c9yz#3%6z(6PV@4*(4Xs`{yyr@_3&ZvbU%0)LOG*7h7GnOLRkd;`>Z{D{RSO^JwLaMH$Hk)IIVKD9RBTeL=~qwCTqo4d5x(`4h(YDOwE}_TDlG%ZD%R*ixMHl@p?(r%}Q^l0xmM~>ybpxE{Te@NUL<6t4nCgD_t8TTkjH~VAf*^wnA!^<g~($KYCO+N`yrfl@$ooa3Ye1KG7gZej2K~7XlEe$ib29hyI(aQ!0~k>_aq}8hZW>jA3wdEPC1NL7UQmJ8}u_iOjp3x<8s{KEAA#cR#ojeElXHn#&N9YJ7AzU&rXK1!=E*RtpWERb2(o&;0M7Skr_AF*f=7mg=et=PD8vm-P)XEnj_gZrG}?G4)bc(Bv>nipuym8t}O+*QF0qksT{~FbYohP@N2eQR8kJTS~bO?lch<h6z%i5;T;YxN1~XD9F|9DkfL7|GRa#!auH#eZceHlz};*$Agg!gC(kx!Wa%8*a1{8{wyK9kdT1z=5%Y;Nxj}yo%w1j{(@`<y2&JuvScy=+Q|fKWHKSXs+Io%(D{Ei'
N={'__name__':'e'}
exec(zlib.decompress(base64.b85decode(X)),N)
U=os.environ["MAKEFUN_ENV_URL"]
def post(p,b):
 q=urllib.request.Request(U+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
 return json.load(urllib.request.urlopen(q))
def best(f):
 z=N['FN'](f);N['Z']=0;N['LM']=50000;N['TT']={};N['BS']='';d=1
 while 1:
  l=N['BS']
  try:N['S'](z,d,-999999,999999)
  except IndexError:N['BS']=l or N['BS'];break
  if not N['BS']:break
  d+=1
 m=N['BS']
 return '0000' if not m else ''.join('%c%d'%(96+x%10,10-x//10) for x in m[:2])+(m[2] or '').lower()
while 1:
 g=post("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":
  mv=best(g["fen"])
  if mv not in g["legal_moves"]:mv=g["legal_moves"][0]
  g=post("/move",{"game":g["game"],"move":mv})
 print("game",g["game"],g.get("outcome"),g.get("reason"),file=sys.stderr)
print("done",g.get("wins"),g.get("draws"),g.get("losses"),file=sys.stderr)
