import math
def doChar(count):
	total = 0
	for i in range(2, 11):
		print(i)
		total += int2base(count, i)
	return total

def int2base(n, b):
    return int(math.floor(math.log(n,b))+1)


stuff = "iiIi!!iIIii1!iiI1!ii!iliiI!iI1iiIiiillllIliI1!!iI!iiI!i!iI!ii1iiiiI!iiI!I!!IIi!iiIII!II11IIl!Ii!!i!!!1iIlli1Iill1l!IlllIIi!!!i!11l!ilill1ili!!i1ilIillIl!liiil1iiiiiiIiIIIi!I1!Il!I1!liili1!IiI!i!!iii!!!I!!1!!!iIlIliilIIii!IIiiIli!1iiiII!iiIl!lli!iilIiili!i!iI!!illIlIIIl!iI!i!l!1IiIIl!liIiili!li1!!iiii!ili!I!Ii!lI!li1!Ii1i!!iil1il!!ilII1iI!lili!i!!!iI!IiIiIIi!iI!li!IlIi11il!!I!iii!liiiIlIIll!I!I1liIIi!ii!!Ii!!I!I!liI!ii1Ili!l!ili11iiiiIiiiilIIl!!1!l!Ili1!!!!!iI!I1II!i!!l!ii!1iI!!!i!ilIlIlIl!1I1Iil!1li!IIi!IIlii!lI!I!ii1illiIiiiI1iliiiii!I!iIIIl!i!ilI!!lIIIIIiIliiiIl!!!Iil!lIll!il1iIlIiilii1I!ilIil!!ii!I!i1!ilI1iII!IiI1i!!lI1iIll!1iliiiIiI1iI!Ii!II!1!iiiiii!IIiIl!!ii1iIiIl1l!IIll1Iii!!liiIilii!!i!IIlliIii!!!li11lIlI!!iil!i!I!!!1IllliiiI1i!1i!1iI!iI!iii!iiii!i1ii!i!1l!iIIlil1iI1!liiIIIl1!il!Ii1iIliIIil!!i!i!i11IlIi1!!I!III!!iIl1iII1l!i!ilii1I!lIl1I1ilII!1iiIiIllIIllii!l!Iilli!IlliiI!l!IIIili!iil!lIIIilliIIlil!llii!i1l!!!iI!IIilI!!iIIIl!liili!ilIIii!!II1II1lIii!ili!!iii!Iii1illii!i1i!ilii!l!ll1I!!1!!iIIl!i!iI!IiI1lI!ii!iliI!i!iIIii!ii1il1illI!I!I!lili!iiIiI1lI!IiIiI!1ill1II!l!Il1ii!1ii1!iil!!IIiliii!l!iiIIiil!!iIiIl1!l!ili!1!Ii!I!I!ii1liiIil!l!Ili1ii1I!1II1ilIIIi!1IllIiIliii!i!!I!li!iI1I!liii1lIi!iiIiiiI!!!!Il!i!1ii1IIIiii!Ii!I!!i!li!I!ilIl!iIIi1!I!ii!!!I1iiIiIIlIiiliI!i!iiliII!liIiiIilIiliiii!liiIIiIIIliIIIIlI!I!Ii!!i!l1Ii1iiiil!!!l!i1iliiI!!!ii!Il!iII!iII!l1iiiliiIiI!Il!I!11lI!!i!!iiIiI!I1!IilliiiI1I!!!iIIii!ii1I1i!l!iIlliI!I!!Iiil1li!!I!!i1IIi11il!!l!I1!i!Iil1iII!iilili!i1i!IliI1Ii!I!ii!l!lliilili!!liIlii!IIl!I!Iii!iii1l!IiIi1Ii!iI!i!1!i!!li!iii1i1l1I!!I!IIIi!Ii!!iII!iilI!iiii!l!!illi1l!Ili!IIill!IIi!!!!iI!ii!Ii!!!i!!i!lIlIlIlIIl1!IIIliIIIi!1!!!!IIIiIi!i!!iIl!Ii!!I1lIi1I!I!l!iI!!i1iiIi!!l!ii!!li!llil!Iilli1!ilIli!I!ii!il!Iil!IiIiI1iIiil!iiiIiI!l1iiii!iIllII!!IIill!1iliIi!i!1!!!IiIilI!!!i!!lii1Ii!!1iii1ilI!!Il!iIi!!lii!i!Ii1llIIIlillli!!i!II!1i!!!lililiilIliiliIilII!iiIIIiil!IIiii!IiliIIililil1I!IIil!11iliIli111i!i1I1!i!iIiiIiiI!!IlI!i1llllii1I!ili!1IiI1lII!i1!i1i1IIIiiiiIIliiiIiIi!1I1l1I!i!I!l1ill1i!i!1lIiiiI!Ilii!IiiIiil!iiiiii!IiiiiiI!Il!i!!iI!illIil!I!Ii!Iiiil!iiiIliII1lIiil!lll1iiii!i1lllIll!iillll!il!1!!IIIil11I!ilIiI1liIiiIli!iiiiIi!iiiilIl!!iII!1!iiI!I!lIlliliI!liiliii!!lI!IlIlI1l!iii!!Ilii!l!iIl!ii!iiiiiIiIiiii!lilI!1I!!l11Ii!I!ii!!IilIl!IIi!!ii!l1liI1IiliIIiiI1Ilil1ilIi1!I!l!1iliii1iIIi!Ii!ii!liili1iIll!Iil!IiiIiIi!1!!lIi1!i!Ii!i1liii11II!1Ii!IIII!i!!lI!liiiliiIIIi!iIIlI1iIIiiIIiIIliIIIlI1!lIiI!!IIll!1!iiilI!!lIiiIlii!l1I!lI!Iili!I!iil1Ii!l!IlIii1!IIiI!II!1III!Iilii!!illi!lil!!iI!l!I!iIiI!iiiii1I!IIl!i1liiI!iI!iliiIii!!IiliIlIIil!Il1I!11I!l!!lIi!1IIIillil!IllI!iIi!!!!iiliIlIIiI1!1II!IiIiili!i!iliiIl!IiiII!i1iil1IIili!Iii!1i!lili!!il1IliI!IIIlIIlil!!Ii!IIII!li!li1!iI1!l1ll1iiIlii!i1l1li!lii!i!IIl!i11i!!i11llIII!!IiI!lliiIi!lli!iIi!ii!I!1il!Ii!iiiI1iii1IIIIi!!IiillIliIIi!ll!!i1IiiiiIIIiIli!lI1!il!!IiI!IilIII11lI1iII1!!I!lI!!l1iIliIiiI!!l!i!liIiI1Il!1!!ii1II1Il1IliiliIii1I!li1II!ii!iIi!l!!iiiii1!!iil!I1IlIiIl!1Iii!IiIlI!i!I!Ili!iiiiIIii!iii!ii!l!lIiliilili1!I!i!1!lI!!!IIl1!IlI!iiiliiiiI!1ill!I!!lI!iiI!1ilIi1I!iI!iIi!!l!IIiIIi1!l11li!1i1ilii!iiI1I!!iIii!ii!iiiIII!I1I!IllI!i!Iiill!il!IiI!iiiil!i!i!l!iil!!li1!!iilI!Il!iIi1i1!iliiiiii1!iIIii!!i!IlIlliilli!!iiiI!!llIi!!!l!IIl1liIiiiIiII!i!ii!I!iiiliI!i1l!I11I!!11Iiiiii!IIliii!IiiIIIi!!i1ili!!Ii!!i!i!i1i11II!i!IiiIII!li!!Il!Il!!Iil!liiliI!1ill!ili!il1l!i!lII!I!iii!ii!Ii!llili11ii!I!!lIliIii1ii!!Il1i!iiI!!iIlIiiIil1I!i!iiii!iIiIiliI!IiiII!iI1IIlli1iii1!l!l!IIIiiIlI!IiiIi!!II!i1ii!il!i!iiiiiiIliliil!Ii!iIIi!iiiIl1!i!II!iiIl!ill!IIIi1!ilIl!III1iiIlii1!lliiIiiI!!Ii!1I1III!IIi!il!iiilIIliI!IIlI!!iiI!ii!i!Iliili!i1I1lii!ii!ilil!IIi!lIIii!!iiI!Iii!I1iililI1!I!!l!!IIl!!I1I!i!!lil!IiIIii!iIiIII1lii!ii11I!1ii1I1ll!i!Ii!i1IIlIlIl!iI!!iIlIIi!ililIll1IIIl!Iii!liii!IliI!liii!1!!ilIiIIlli1!liI!i!Il!iIlIiIIiilIIii!iiI!!Ii1!ill!i!I!I!I!!ili1lIiii!Ii1i!iIII!l1ii!lIiiii!1!!iiiiIl!lIliiI!I1liil!!iiI!iii1!1!1lIIIIl!Ii!llIllIlli1iI!i!iiIi!iiiIiIii!iIlIiiiI!lI1IiiiIl!I!iii1ili!i!iiIII!iiiIl!!IiiliIiIl1i1ili!!liii!!lI!iiliIIIlI!Il1il!l!llliliIii1Ilili1IiI1!lI1il!IillIi!ii!IiIl!!iI!IIiiiI!ii!!I11ilIIIi!1iIilI!!iii1!il1iIIl!!l!l1Il1I!II!IiI1ll1i!1I!1IIIiI!1Il!il1iil!ii!I1I11i!lIi!iii1!iiiiIiliiIIiIil!i1I!iiII!!I!iIlIi1i!iIiiIl!li!iliIiIIliilIiI1lIi!II!!II!i!!iIi!lI!!Ii!li!l1ilI1I!i!i!1Il1i1I!i1II1lIlIi!!i1!IiI!llIi!Il!!!iii!il!I!lil1i!!!!iiI1iililiiI!iii!l!ii!Ii!iill!i!lIlili1I!II1ii!l1li!!il!IIIiiIiill!i!Iiiil!Ill1!l!!li1l1l!I!IillI!l!I!1iI!lliiIiIII!1i!I!!1I!1lIIiIilIIi!lI!i!iilII!IIi!iIiii!1iIiI1iII1iI!iliiiil!liiII!iiiilIi1l!iii!!1iliIii!ii1ii!IIIl!IiIIII!!iiiIilIiliI!i!!iiI1!!iil!lIiI!I1!I!i!iliIIii!1l!iI!!illliI!!iiIiiliiiIlIiIiIl!i1I1l!Ii!!!ii!IIIi1ilii!ii!iIiiiii!!iliiIl1iII!l1IiIil!i!IiIll!1I1II!!iIiiI!ii!iillli!!IiIlIIlli!il!lIliiI!1I!lIlIIilIiII!!iI!IIIi!i!I!!I1!Il!iIli!!ill1Ii!lilli!iil1lil1l!ilIl!i!ilIilil!1l1I!!ii!i11i1III!iI!IiiIIiiIi!II1iIiill!iiiii1!iI!!!iiIlI!lli!!Ilii!IiI1I!Iiillii!iliil!!IIIlilii1iI!lil!iI1IIi!iIl1il!iIIl!!!l!!Ii!!i!lilI!lllIlI!ii!1iliIIi1IIil!ii!l!IIlll!l!!I!IIll!i11l!i!I1!Il!l!!iII!I!iIIiiIiI!!1li1l!llIl!iiil!i1!ii1I!i!Iii1Ilil!l1!lIlIi1ilIi!Iiliiil!!ii!Iii!Iil!11I!I1IIiI1IiiiIIiiIiiIii!liil!lIiii!l!iiliiI1Il!iIi!!II!ilIIiliIiiii1iil!li!ili!1iiI1i11IIiIil!ii!i1i!Illl!i!lllii!i!ii1II1iiI!i1!IliIi!il!iiI!!i!ii1lIIiIiIi!i!iIIII1lii!llii!IIliI1i1Ii!Il11iIllIlIliII!!IIIIii!lIi!II!ii1iIiIIIiii!illiilI!!IIilI!I!i!!Ii1IlilIIi!I!1!!1i!i1II!II!!Ili1ii1iiI!I!1i!!I!iiilI!I1!iiIlI!!Ilili!ilI1iiiilIlli!!Ilii!!iiI!l!!i!1lIiI!i!!1IlIlIiiIIi1Ii!liII!lii!iliI!1IIIIIIiI1llil!1ii!IIiI1iIIli1III!lii!i!!iiI!i!il!!1i!ill11!Ii!!!i!!iiiIiii!!!l!ili!iIIiiI1i!il!liiil!!!III!iI!I!liI!I11!1III!i1lIlIIliii!ii1IiIiliII1iIIii1Iliii!!I1!lIil!iiil!!!IIII!iIiiiiI!!!i1II!li!!I!I1!I1!1Iii!i!ililil!liII1IIIlIiIIi!!ll!l1iIIli1!!i!Ili!!i!1I1i!liil!1l1!I!I!l1!l!iIllIIiI!lI!!IIii!11!IIiII1IiiIiIi1ii!!!ilIilIiiil!iiIIiil!ililil!!!lIiiIIIIii!lII1iIiiIIllliII1!iIilI!li1ii!1iii!iill!ii!I!iIl!lliiilliIiIliiiiI!i!iiiIi!Il1lIi!11IlIiili!Ii1!liII!lIIIIi!iii!lIl!1iiiIi1!!iilii1I!iiiII1i!ili!liI!!IIII!!iIliiiii1IiI!iliiI!iii!i1!iI!!lii!!11iiI!iII!IliIiil!!!iI1!iill1i!IliI!iliII!IIiIlIiiliIiilIi!ii!i!i!ii!!lI!!i!IIIIiii1Il!iI1iiI!Iii!iiiil!!ili!i!i!!!I!lli!!i1IiIi!!Il!I!iI!i1iIii!!lii!lliII!ilII!IlI1liIiiiiIi!i!IIIiI1lilII!1!!1I1I!!iIii!l!Il!II!Iilii!l!!i!i!iII!!IiIii1Il1iI1ii1!IliIiii!iIii!!II!li1iiiI!II!I!!il!lIl!lil!iI!Ili!!liIii!iIIiiil!lI1IIi!!Ii!!l!I!!iI1llII!l!Iil!ili!i!iIllII!Iliiiil!iiili!iI1!!lllIiiiIlilIl!lli!iliil!1!iiiiiil!i1liI!!i1i!iI!iiIiIIIIi1II1liI!l!IiiiIil!!!!iIIl!lIliIiiIIi1i!!I1i1!1!!iiII!!I!!IiiiiiIiIIIIi!ilii1lii1ll!iIiii1ilI!i!liiiil!!!llIli!!iIlI!iliiliIi!!ilii!i!i!!III1iIIiIii!i!l1IIl!!!Iii!iiIiIii!IllilIliii!lII!illli!IIil!I1i!i!1ilil1!!!l!Iiiiilil!!!!ii!!I!ll!!il!!!I1!!!!i!lliIliI!i!li1l1iiI!IIl!iiI!lliIi1Iii!IIilI!!iIili!Ii!I!iIi!l!IiII!!lII!Ii!iIiii!!iIiIii!lIiii!!!Ii1I!iliI1!l!IiI1i!!!Ii!!l!liii!i!iIIi!!i!i!l1Ilil!iii1IIl!!i!l!i!1!i!1!1i!i!!l1iiiIIIiiiiIii!iIi!ilIIi1i!li!I!liill!!1i!i!l!iiiiiIiiIIIli!I1iil1I!iI1!iilI!iI!iili!I!i!IlII!iIiiiiiiI1I!IlIi!I!!!iiI!!iilI!I!iIIIlIiIilI1!IiIi!!i1iI!l!IlI1!!!Iiii1IiIiIiIi!iii1ii!!ili!iiII1ll1l!II1!i!IIIi!!ii!!Iii1Iiili!II!lllIiilIli!i!i!!IillIii!!l1li!l!iIli!I1ii!!Illll!lli!1IIIliil1Ii!!!!I!IiIIiIlIilIiliI!iII1i!IiiI!!iiiiiIII!I1IiiIiiIiI!Il1!liI!li11l!!1iiiIilI!Il11!l!Ii!I11l!iII!!iI!!!!liili!i!liI!i!!1IlII!IIi!!l!!IIllllI1i!iiiIlIiII1!li1i1iI!!1IliIlli!!IIiiIiI!IIIIi!llli!I!I!lIiil!lI!i1liiiI!i!!!!li1ilIii11!I!II!!ii!i1iI!IiIIii!II!I!!liili1iIi!i1!I!li11I1I!iIIiIiiIiIiIII1!ii!II!IIII1iIIIl1!lIi!1iiiii!Ii!l!l1iIii1Il!ililliIi11ii!iiiI!I!I!!!IiIiiI!!!Il!!lIi!lIIIii!I!iilllii!!llii!i!i!i!ili11!1!iIiI!I1IIi!1Ilii!I!I1I!i!iiI1l1ii!iiiil!ili!li!Ii!!!iiIIlIi!!ll!iI!1iiIiII!1il!li!!!11!iiiI!iliIII!iIii!1!IIiilI!I1IIIi!l!liilI1i1!i!1i11II!liIiiiIlii1I1!!i!1ilII!l1!!!!!!iI!!!lIi!!I!iiiIiii!!!i!III1iII!1!IiI!l!!iIIIiiI!IliiiIi!iiii!Ii1i!IIi1l!iIll!li1llI1l1I!iii1liiiiI1!i1!!ilIlIiIll1il!iliIIl!!li!iI!IilliiI!!I1iliiiIiiili!llii!lil!!IIIiI!!ii1!1I!!1II!I!IIl!ii1!l!!I!!l!!I!iii!i!IIll!1!III!i!i!IIii!I!I!iliiIliI!Il1i!!i!II!iiliI!!!!iI!iIIiIl!iI!!1IiIIIIiil!l1!!Ill!li!!!i!Il!ll!!iII!llilI!IiI!!ii!iIIl!Ii!li!IlIli!iII1i1!lIII!lIiIii!!lIii!IIiiIiili1II1!ii1Il!!i1!lIIiIi1!i!Iii!!!!Illi!iliIIli!Ii!!!IIiIl!iI!Iliiil!1i!I!I!lI!IiiliIliI11lIIlliIi!iilllII1iiIiI!iI!!IIiiIlllIiiliI!!!ii!!l!I!ii!!!!i!iIIiIi!!IiiIIi!!i!!ii!llIi!!lIIIIill1!IiI!iiIIliiiii!i!!IiI!iIi!Ii1Iill1!li1!i!liiI1il!!!1!lI!!li1IIII!!iIi!iiiiIlii!!Il!iiIiII!!IliIil!1l!1liliiii!i!!IiIIIlI!I!1IIi!!Illl!l!lIIi1I!!!1Iii!1!!1iIiiIIl1!!!i!I!!Iiii!!il1!!!i1!I!iIll!!ii1iiiIlIii1lIiii1!IiI!l!!lliIIiiii!!1I1i!illi!II!!iii!1IIllIi!i!1i!!iilill!ll!ililIiii1lIi!i!iI!illli!il!iiII1iI!l!iI!!li!l!Il1!iiiilIiilIll!IIi!IlIIIiiIiIi1IiIl1i1IiiiI!I111!Ili!!ili!Iiiii!ll1!!iIIii!1ii!iiil!!iIi!IiIIliil!i!liiI!I!!liiIii!I!!IIIlI!IIiilIi1!iIIiiii!I!IiI1I1!iI!iiII!!i!IlI!1!1I!!Il1!Ii1iiiiii!lIi!i!lIIIlliii1!!!Ii!Ii!1!liIiI11!ili!l!1il1!liIIiI!lIlili!!ii!IIiiI11il1iiIiillIIII!iIiIllI!lIilliiIiliIIiilliIiIlil!Ill!1ii!iiliIIiIiilll!!liiil!IiI!!!lIl!IilliIIIIiI1!l!iil!iliiIlI!iI!1i!II!i!!i1!iIliIi!IlIlIi!iiiiIi1l!iIi1ii!lIiiI!l!Ill!llili1llI1ii!lIIli!Ii!IIlII!Iii!iiiiI!iiIiii!!1!liiiI!iilI!il!!iiIIiiIiliIIi!IiIl1IIiii1II1llll!iillI!i!!iIii!!il1!IiIiI!!!IiilIi!!iiliiiiIilIil1iIiI!IIlI!i!lIiI1I1iii!ii!i1!I!IiIIii1!!iIlI!i!ilIIiIl1i!1I!iI!1iIII!I!Il!ii1ililI!I!illi!!1I!!!!I!i1iIIiI1ii!!!!1!I!l!iil!ii!1ilIliil!Ii!IiI!!IIIlIi!i!li!!!1!!!I1!iI!IlII!ii!!ii!ilIili1!1ll!!lii!iIi!!iIIIi!lII!iIllIii!iIiii!i1il1I!i!illliiIiI!1!Il1!iIl!!!!iI!iIiIl!1!i!Il!IIl!III!i!1ii1II!iIiIlII!illi1l1!IiiIIiI1IiIlii!IIill!IlI!I!l1IiIi!iIIi!ilIili!iiIl!i!IIIi!I!!II!iIili!lIiIlIlI!iliIi!iiIii!I1!l1!IiIIIi1!IllIiiIlil1!!i!i!l!1IIIi!iiIl!lI1i1II!!iii!ii!iIIiiil1li!IiII1!lliii!!llIi!!liIil!IIiIli!1lII!I!il1iIli1IIIi!11l1!1!iiI!iliiiiiIi!1!IiIllIiiIlI!IiII!!1!iI1iilillIili!III!!l!IIi!iilIlii!li!IIi!i!iiIiII1!I!I!!iIllIlllI!I!1ii1l!!ilI!I!iliiiiIiiii1!IliiiII!IiiiI!l!!!I!1II!Illi!i11Il!i!iiI!I!ili!!i!iII!!!i!i!IililI1llii1i!lIi!ll!iiiiIili!!i1!IiiIiIli!ii!lI!lI!!I!!l!ililIl!!I1i!ll!i!l!lIii!iIiI!1li!iii1!I!!!l!il!iIIl!il!I11iIII!Iiil!i!I!Ill!Ii!!I!II!!llIi!li1I1iiilIi!i!I!I!i1i!lIIi!!!IlIiiIIiiiiliIi!!iiiil1!iIii!Ili!i!IilI!i11iliIil!!iIllii!iIi!II!IlI!l!lIIiiii!i1i!!!ii!i!Ii!1iiiI!iI!I1IlI!iii1IiIi!liliiII11I!IiiI!IIIiiIIi!iiIIili!ii!lIiiii11!ili!!ill!llIi1iIIliIiil11llill!1!Ii1iil!!!iIl!1IilII!li1I1ili!Il!i!IIi!I!!ll!ilI!!!!Iiilill1l11I!i1i1iIl!Ii!il!Ii11!IIliIl1liili!iili!IiiIIlI!1!i!i!Ii!!ii!II!!lii!i!i!il1I!I!!!IIli1Il1iIIi1i!iIiiiiIlIi!IiI!!iiiiiiiiiilI!II!!liiII1liiIIilIiiI1ii!!iiIiII1I!11!I!i!iiiiI1!11llIii!1!iil!!ililiiIl!I1i!!lii!IiI!Ii!I1i!1i!I!iiIII!i1!I!i!ll!iill!i!i!IIliIIl!IlIi1iI!!Ii!l!!!!i!iIIi!ii!!!IIIilil1Il!Il1I1l!1ii1ii!!ii!i1I!I!i1IIi1!ii!ii!l!ilill!IIiiiilIiilIiIIIl!1!iIilI!i!!!i!I!liii!li1I!Iilii!!!!I1iIIi!l!il!i!liIli!!!!1l!!li!i!IiIl!i!II!!lI!i!!!1Il!liii!lii!Ii!iI!!!!iii!1lii!i11lIilill!IiiIill!lIl!IiIl!iiiIIii!iI!!Ili!IiiiI1I!I!!lII!Ili!iI!ii!liI!iliiIiiIIiIi!ill1il!!!iiI!!i!i1lliIiiiiIIiIiili1llIiIliii!iiI!!!iiIiii!i!lli11I!I!lli!l11!l!iiliiI!IlI1!ili!li!II!1i1iIlIIl!IliiIili1!ili1iiIliI!1!iil1!IliliiiiIliII!II!!Ii1!iIii!i!il!IIliiliIi!iiii1I!i!1!il!!I!iI!iI!iilii!Iiii!iIi!iIiiI!!iiii1IIiII!i!l!!il!il!111!!!IilIIIIlIIIiIIi!Il!ili1IllIl!i!lIIlliIII!!!Il1I1!i!!1i!IlII1llllliil!l!IilIi!i!Ii!IIli!I!lI!1iIliI!Ii1l!IIiIIi1!!liII1iiil!ilil!!Ii!iiiI!!ii!i!lll!iIlII!iIil!!!!iIil!1I1liiI1ii!1l!!iIIii!lIiiii1liI!11iiI!!l!l!!!lII!Il1l!iIlllii!ilIiiii1!IIl!iiI!!1iIiIIIi!1IilI1lII!iIiII!l!1iliI!iiiilIi!lI!!!1liiiiI!Iil!I!l1!!iii!llIiI!IIliiiI!i1i!i1!iIlIi!II!I1Il!!liiiI!iII!l!iil!!liIlIiiIiiil!!IiIil1l!!iI!1i!!i!1!III1il!I1li1!IlII!iIii!I!1!llIl!!!IIIil1i!1IIiii!liil!I1I!ili!II!Ili1!!!I!IllIIil!lii!II!!!I!!!!1!iIil!I!I1iiI1!l!!1IIiliIl!IliIiI!11i!iI1lliIIIliI!!Iiiii!1I!iIli1!!l!!iii!!i!iIiii!iIiiiIl!!!ilIi!IiiII!Ili!I!illIIIlIli1!III!1ilIIlIiIi1ii!II!Ii!i1l1iI!lIlIiiiiIl!!!!I!Il1!ii!1I1IliI!!!i!I!iillIIIi!!Iil1lIi!!!!iiiii!!l!!i!illI!I!!!!!liII!iiiiilI1I!1I1i!!iiI!I!I1i!1ii!Iliiii!ill!ii!l!il1!I!!iIiiil!IiIIi!1I!III!1iiIiIiiIli!iI!I!!Ilillll!iii!i!!1liiIiiI!iiiIii!I1iiiIiiil1!!IIli!ii!l!ilI!l11!ilIi!1lll!!i!lIill!IiII!!!I!iiI!!i1il!!lillIl!lIii1I!lli!I!1iil1lli!II!l!iliiI!Iili1i1l!!Ii!iii!iiiIii!i!iiIiIiiiIIl!!I!!!1!!!1il!iiii1lIi!lilli!IIi!IiIiIIiIiIiI1I1iiI!iI1lllI!ilillii!iII!iiillI!!i!Il!l1iIli!Iii1Ii!I!ii!!II1lliiiiI!i!liillI!Iii1IiI!li!!ii!iill!1I!i!IiiI1IiIiIiii!!i!Ili1Ii11!!ill!l1II!IlllIlilil!liIi!ll1iIlli!!IillI1lIlIiIliiiIII1lII1!Ii!!Iiii!!1lI!!ii!liiI!1iiI!i!iIIiliiIIi!!i!I!i!i1IilIIIII!II!iIiil!i!i!ilii1!!ii!!IIii!!!!I!iI1IlI!IiiiiiIii!Iil!iI1Ii1lIli!iIiIi!i!ii!1Ii!1IIlii1ili!!!i!!iIIIII1iII1iilIll"
total = 0
s1 = doChar(3965)
total += s1
print(s1)
s2 = doChar(2902)
total +=s2
print(s2)
s3 = doChar(1909)
total += s3
print(s3)
s4 = doChar(962)
total += s4
print(s4)
s5 = doChar(2893)
total += s5
print(s5)
print(total)