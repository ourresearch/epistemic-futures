---
title: "Mapalester:Powerful, East-to-Use GIS Software Under Development"
person: brent-hecht
attendance: unconfirmed
section: by
type: journal-article
year: 2005
date: 2005-01-01
venue: "DigitalCommons-Macalester (Macalester College)"
authors: "Brent Hecht"
source_url: https://digitalcommons.macalester.edu/geography_honors/5
fulltext_url: https://content.openalex.org/works/W30104137.pdf
openalex_id: W30104137
oa_status: green
cited_by_count: 0
retrieved: 2026-08-13
content: full-text
notes: "Full text retrieved via the OpenAlex Content API (https://content.openalex.org/works/W30104137.pdf); no binary stored"
---

# Mapalester:Powerful, East-to-Use GIS Software Under Development

## Full text

Macalester College

DigitalCommons@Macalester College
Geography Honors Projects

Geography Department

May 2005

Mapalester:Powerful, East-to-Use GIS Software
Under Development
Brent Hecht
Macalester College

Follow this and additional works at: http://digitalcommons.macalester.edu/geography_honors
Part of the Geography Commons
Recommended Citation
Hecht, Brent, "Mapalester:Powerful, East-to-Use GIS Software Under Development" (2005). Geography Honors Projects. Paper 5.
http://digitalcommons.macalester.edu/geography_honors/5

This Honors Project - Open Access is brought to you for free and open access by the Geography Department at DigitalCommons@Macalester College.
It has been accepted for inclusion in Geography Honors Projects by an authorized administrator of DigitalCommons@Macalester College. For more
information, please contact scholarpub@macalester.edu.

'jMopolesten Simple, Powerfu, GrS Softwore
Under Development"

GlSsoftwsre

powerful > eosy-to- use> free
Geography Honors Prolect
ComputerScience
Capstone

Brent Hecht
Advisor:Dr. LauraSmith,Geography
Comp.ki. First Reader:Dr. SusanFox
Comp.Sci.SecondReader:Dr. LibbyShoop

l.INTRODUCTION
PRoJEcr
l l. PuRposEoF THEMAPALESTER
1.1.1 ANrr,vsrs oF rHE K-12 EDUcArtoN TARGETMARKET........
TARGETMARKET
I.I.2 ANALYSISoF THENON-PROFITS
UsE TARGETMARKET........
l.l.3 ANALysrsoF THEPERSoNAL
OFMAPAL8ST8R...............
To THEGISCIENCEENGINEERING
I.2 INTRODUCTIoN
1.3 INrRoDUcrroNro GIS ...............

2. BASIC ENGINEERING OT'MAPALESTER..................

.............................2
...................3
....,.,...8
.......................9
...............I3
.................13

t6

2.1INrRoDUcrroNrorHEENGINEERINGoFMAPALESrER..................................................16
...........
16
2.2 WHAr rs REALBASTC?
.......,.....I9
ARCHITECTURE
OFMYCHOSEN
2.4THECHALLENGES
3. THE OBJECT-ORIENTED STRUCTURE OF MAPALESTER
3.1ANOveRvrEworrHEOBJECr-ORJENTEDSTRUCTURE...
SysrEM.........
3.2TnnINTERFACE
Sysrsu
3.3 THBDATAINTERAcTToN
3.4 THBPnoD
SysrEM.........
3.5Tse DATABASE

.................23
.........................23
......................23
................28
......................36

4. THE DESIGN AND IMPLEMENTATION OF MAPALESTER'S FEATURE SET........................45
..................
oF FILEFoRMArs
oF A vARrETy
4.1. SuppoRT
To FILEFonuer SuppoRT..................
4.1.I GeNsnnLIssuEsRELATED
FILEFORMAT
RELATED
IO VECTON
SUPPORT
4.I .2 GrNrNnLISSUES
4.I.3 SHAPEFI
4.1.4SuppoRron THr ".PRJ"ExrENsIoN...............
FoRcEAppRoAcH
4.2.1TP.eBRUTE
4.2.2T*tsR-TnrnAppnoAcH..............

.............................45
..............................46
...,......48
...............56
..................61
...............64

4.3.1DoucI-n
........73
AppRoAcH....................
4.3.2THETRTVTAL
.................73
SPEED-UP......
4.3.3Tsn HrnsHsencsR"/SNoEYINK
..........74
FUNCTIONALITY...............
DATABASE
4.4 ITUNES.LIKE
on, "THnGIS THATAcrs LIKEA GLoBE,Nor A MAP"....................75
CoNVERsIoN
4.5 PprueMBRTDTAN
.........................76
4.5.1PoINrSuppoRrNGISPIN
..'......'......78
ANDPoLycoNSupponrIN GISpIN
4.5.2PoLYLTNE
.,..,...79
CONVERSIONFUNCTIONS
4.6 PROJECTION
.....................'........84
PLANNED
FEATURES......
oF OTHER
4.7A SrrlerrSUBSET
oF rHe NarroNnr MApAppLIcArroNPnocneMMINcINrennece(APD..............85
4.7.I INcoRpoRArroN
...................85
EAsyAccnss ro Cnsus Dere
4.7.2PRovrDrNG
'.......85
Usnc rHn GuurELLANETWoRK................
4.7.3Dnrt FrLE-SHARTNG
........86
4.7.4INIBnNnrIoNALIZATIoN....................

'........89

5.2 ACKNoWLEDGEMENTS..
6.l BIBLIOGRAPHY

MapalesterResearchProject

PageI

1. Introduction
1.1. Purposeof the MapalesterProiect
Over the pastnine monthsnI havebeendevelopinga new GIS software
applicationnamedMapalester,aftermy soon-to-bealma mater. The goalsof the research
projectwith Mapalesterasits productare definedby the threetargetmarketsof the
product:K-12 education,non-profits,and individual/personaluse. I identifiedthese
marketsas marketsthat had one or more needsfor GIS softwarethat is/are currently
unmetby the body of cunently-availableGIS software. Theseunmetneedsvary widely
amongthe markets,and I struggledat first to identiff a reasonablesetof development
goalsthat would equipMapalesterwith the functionalitythat would meetall threeof
thesemarkets'needs. In the en4 however,I was ableto constructfour broad
developmentgoalsto which I alignedmy designandprogrammingefforts. First,
Mapalesterneedsto be powerful. In otherwords,if Mapalesteris not ablehave some
basicsetof GIS functionality,Mapalesterwill be more or lessuselessto all threeof
Mapalester'stargetmarkets. Second,Mapalestermust be easy-to-use.Thir4 Mapalester
must work on both the Mac and PC platforms. Finally, Mapalestermust be availablefor
free.
partsof the introduction,I will discussthe specificunmetGIS
In the subsequent
needsof eachof the targetmarketsandwill explainhow thesefour developmentgoalswhen fully implementedin Mapalester- will enableMapalesterto meetthoseneeds.A
diagramof the needsand marketsis found in figure 1.Ia. To confinethis discussionto
merelythe inhoductionof this paperis to falselyreducethe complexity and,in many
cases,the immenselytroubling natureof the unmetGIS needsin the threetargetmarkets.
However,the focusof this project- at leastat this stage- is not to explorein depththe
and free GIS on thesetargetmarkets.
effectsof a powerful,easy-to-use,Mac-compatible,
Rather,this project is by and largea GlSciencesoftwareengineeringproject. The
discussionis intendedto provide somecontextfor my GlSciencesoftware
subsequent
engineeringwork. A very valuabledirection of future researchwould be to examine
thesetarget marketsand developmentgoals in greaterdetail. My hope is that this future

MapalesterReseaxchProject

Page2

will eventuallybe enabledwith empirical datafrom observingthe effectsof
reseaxch
Mapalesterafter its release.

Target Market

Unmet Need

K-12 Education

Softwareto increaseadoption of GIS as a
method of teachingexisting ourriculum

Non-profits

Softwareto empowernon-profitswith the
sameGIS capabilitiesas for-profit
companiesand government.

PersonalUse

Softwareto facilitate the long-overdue
transition of GIS from the lab to the
consrrnerdesktop.

Figure 1.14- The unmet needsof Mapalester'starget markets.

Moreover,beforethis moredetaileddiscussionof the reasoningbehind
Mapalester'sbasicdesign,it is importantto notethat embeddedin the goalsand target
marketsof Mapalesteris an inherentcommitmento helpingleveling the socialplaying
barriersto the incrediblypowerful tool that is GIS.
freld by removingsocioeconomic
This commitrnentis similar to that presentin an Al Gore speechcited by Elwood (2002)
"[GIS will] help communitieshelp themselvesby putting more
control, more information, more decision-makingpower into the
handsof families, communities,and regionsto give them all the
freedomand flexibility they needto reclaimtheir own uniqueplace
Office 1998)
in the world." (StateCartographers

1.1.1 Analysis of the K-12 EducationTarget Market
At fust, it may seemridiculousto think of GeographicInformationSystemsin the
contextof primary and secondaryeducation.Today,GIS is often thoughtof as acomplex,
level,
professional-and academic-leveltool. After all, GIS is taughtat the undergraduate
and mastersdegleesin GIS arebecomingwidely availablein most countrieswith
Hecht

MapalesterResearchProject

graduate-levelGeographyprograms.Indeed,for most of its uses,GIS is a very powerful
- and correspondinglycomplex- tool. Howeveroas documentedby Kerski, Baker,
Bednarz,and others,GIS can havemany helpful applicationsin primary and secondary
educationcurriculum. "Since the First National Conferenceon the Educational
and educatorshave
Applicationof GeographicInformationSystemsin t994, researchers
repeatedlyidentifiedthe merits....of includingGIS in elementaryand secondary
classrooms."(Baker,Bednarz2004)Kerski skillfully distinguishesthe applicationsof GIS
that arehelpful at aK-I}level from the applicationsat higher levelsof educationthrough
aremy own):
a simplecategorizationmethod(emphases
"GlS is used in three major ways in education at the
elementary,secondary,and university level. First teachingabout
GIS dominatesat the university level, where coursesin methods
and theory of GIS are taught in geography,engineering,business,
environmentalstudies,geology, and in other disciplines. Every
major university and most communitycollegesin the USA host a
GIS program. Second,teachingwith GIS is emphasizedat the
elementaryand secondarylevel, whereGIS is increasinglyusedto
teach conceptsand skills in earth science,geography,chemistry,
biological science,history, and mathematicscourses.Finally, GIS
is used as a fundamentalresearchtool in all institutesof higher
education in geography, demography, geology, and other
disciplines."(Kerski 2004)
Despitethesewidely acknowledgedbenefitsandwell-definedrole of GIS in the
K-12 market,all thosewith knowledgeof GIS in educationagreethatefforts to
incorporateGIS into the K-12 curriculumhavemostly failed thus far. In the contextof the
infamous"InnovationAdoption Curve," Bakerand Bernardznote that GIS in education
hasnot madeit pastthe early adopterphasein K-12 education.In otherwords,"GIS
educationis still strugglingto win a wider audienceamongthoseeducatorswho serveas
role modelsand opinion formersfor the majority of teachers,characterizedby respectable
early adopters"(Baker, Bednarz2004).

MapalesterResearchProject

Sanr'adon

T*eItl
GISadoplion

E!.ly Arbpt rr

Figure 1.1.1&- The Ionovatiotr Adoptiotr Curve for GIS ys. col|lput€rr io K-12 educrtioo'

Therefore, statedbroadly, the unmet needof the K-12 educationGIS marketa
GIS technologythat will enableschoolsto successfullyteachwith GIS, forcing the
progressionof GIS technologyalong the innovation adoptioncurve in the K-12 market.
In other words, the goal for Mapalesteris to facilitate the incorporation of GIS into the KI 2 curriculum. Each of the four developmentgoalsmentionedaboveis designedto
empowerMapalesterwith the characteristicsand featuresnecessaryto fill this void in the
K-12 GIS market. In the subsequentparagraphs,I will elaborateupon the exact mannerin
which the four designgoalsof Mapalesterhelp to meetthis need.
The frst designgoal - that Mapalestermust be a reasonablypowerful GIS - is an
absolutelyessentialprerequisitefor any GIS softwarethat attemptsto help incorporate
GIS into the cuniculum of K- 12 education. In order for Mapalesterto be an option for K12 GIS, it musthavethe entiresetof basicGIS functionalityrequiredin the useof GIS in
the K-12 curriculum. Ratherthen identiff the exact set of functions necessaryfor K-12
education,I haveassumedthatK-12 requiresthe samebasicsetof functionalityasthe two
other target maxkets. I have defined this basic set of fimctionality as all of the featuresthat
I was taught in two semestersof undergraduateJevelGIS. This includes featuresranging
from basicrasterand vector GIS tasksto raster-basedspatial analysisto geocoding. After
Page5
MapalesterResearchProject
Hecht

this basicsetis completed,it would be an interestingextensionof researchto try to fine
tune Mapalester'sfunctionality for the needsof the educationmarket. I have done some
initial thinking - basedon the literature and on my own assumptions- on what this finetuning would entail,a descriptionof which canbe found in section4.6.
Judgingfrom existingliterature,the most importantdesigngoal for the K-12
market is ease-of-use,my seconddesigngoal. From the literature, it seemsthat the largest
barriersto incorporationof GIS into the K-12 marketlie in the complexityof currently
availableGIS software. This complexityinhibits the adoptionof GIS in nearlyall phases
of the educationprocess- from in-serviceprofessionaldevelopmento the development
and implementationof lessonplansto students'learningof the curriculumthroughGIS.
The third designgoal is almostexclusivelyfor the K-12 educationmarket.
Accordingto Quality EducationData(QED), in 2003,28 percentof the installedbaseof
the computersin K-12 schoolsin the United Statesis madeup of Apple Macintoshes.
While more recentdatasuggeststhat Dell is far outsellingApple in this market(41
percentto 14percent),Macs will remaina largeportion of the K-12 educationmarketfor
a long time to come. Moreover,Apple hasmaderegainingthe lead in the K-12 education
marketa high priority in recentmonths,andhashad somesuccessat doing so. As such,
the designgoal that Mapalestermustbe ableto work on both PCsand Macs is an essential
designgoal for the educationmarket.
When fust investigatingthe K-12 GIS marketand its unmetneeds,I assumedthat
the most importantdesigngoal would be extremelylow cost. However,at leastaccording
to the K-12 GIS literature,costdoesnot seemto be the pre-eminentbarrier to adoptionof
GIS into the curriculum. Rather,as mentionedabove,the complexity of use of currently
availableGIS softwareseemsto be the largestsuchbarrier. In fact, in Kerski's seminal
paperon GIS in the K-12 market,he doesnot identi$ costat all as a significantreason
why GIS hasnot madeit pastthe early adopterstagein the innovation adoption curve.
This omissionprobablyrevolvesaroundhis relianceon a surveysamplethat only included
registeredownersof the top threeGIS applicationswho listedtheir occupationasK-12
educators. A helpful path of future researchwould be to delve into the immensebody of
literature covering the "digital divide" in educationand to apply findings from this
literatureto a GIS context. Kerski doesmention,however,that only 5 percentof
Hecht

MapalesterResearchProject

American high schoolshave accessto GIS software. As such,while the "free availability"
developmentgoal may not have much of an effect for these5 percentand the likely
smaller percentageof American middle schoolsand schoolslocated in other countriesthat
implement GIS, it will play at leastsomerole in GIS adoptionin the vast majority of this
target market. It is no doubt a lot easierto convincea school administrationto invest in
GIS whenit costsnothingto do so. Figure LLIb showsthe approximatecostof
implementingGIS using in a K-12 environrnent. Note that the prices are essentiallyrental
fees;the softwaremust be renewedeachyear for the price seenin figure l.l.lb.

Approrimate ANI{UAL Cost to
Equlp 3O ComputenoIn K-12 Lab
$1,000
$900
$800
$700
$600

$s00
$400
$300
$200
$r00
$0
Idrisl Killmaniaro

ESRI
GIS Product

Maplnfo

Figure l.l.lb - Cort to equip 30 coaputen i[ s K-12 computcr lrb or chtrroon for onc ycar. Cllrk
Lrbs, dcveloperofldrisi, hrs I diffcrrtrt priclrg schemethrn thc ESRI (Envirotrmc rl Systems
Rcs€erch ltr3titutc) and Maplnfo, rnd thc $900 figure is an ertimrte b8scd on thc mrny pricing plans
ofered by Clar|( Labs.

If we localize the innovation adoptioncurve to a sampleindividual school, it is
easyto seethat it would be irnpossibleto make it pastthe early adoptionphasewilhout the
administrationmaking the very basicelementof GIS adoption- the GIS softwareits€lf availableto the early and late majority population of teachers. Indeed, in a personal

Hecht

MapalesterResearchProject

Page7

interview, SaraDamon, ateacherat StillwaterHigh Schoolin Stillwater,MN indicated
that while there are relatively steepdiscountsavailablefor schoolsthat want to buy GIS
software,a free softwarepackagewould be a hugeboon to schoolsand school districts
that havenot yet investedin GIS software.

1.1.2Analysisof theNon-ProfitsTargetMarket
According to Elwood (2002), authors in the GIS literature have found that
"information technologiesand GlS...benefit [non-profits and community groups] by
expandingparticipationin decision-makingprocessesand by increasingtheir political
power." (Elwood 2002).Although Elwood identifiessomenuancedproblemswith their
analyses,Elwood more or lessagreeswith theseauthors'conclusions.However,Elwood
also notes that for GIS to allow for true empowermentof non-profitsr, there must be
some way to free the non-profim that use GIS from the external power structuresthat
often accompanythe use of GIS. For instance,for many non-profits to utilize GIS in
their activities, they must either obtain funding to purchaseGIS software or they have to
rely on GIS "shops"and collegesanduniversities.Thanksto its core developmentgoals,
Mapalesterwill be able to simultaneouslybenefit the non-profit community in the ways
identified aboveand free non-profits from the external oversight and confol that usually
GIS adoption.
accompanies
Becauseof my dedicationto making Mapalesterinto a "powerful" GIS software
application,Mapalestershouldbe able to benefitnon-profitsin the ways identified in the
GIS literatureby Elwood. As long as Mapalestercanprovide most, if not all, of the GIS
features and functionality required by non-profits, Mapalester will inherent$ result in
thesebenefits,accordingto the literature.
MapalesterprovidesGIS powerto non-profitswithout the negativesideeffectsof
currently available commercialGIS softwareapplicationsthrough the "free" and "easyto-use"developmentgoals. Obviously,by makingMapalestera freedownload,nonprofits wishing to utilize GIS no longerwill haveto rely on outsidefunding sources.
' I wiil group togethernon-profits and community groupsunder the umbrella title ofnonprofits for the remainderof the paper.
Hecht

MapalesterResearchProject

Page8

However, anotherbarrier to GIS usagein non-profits is likely the complexity of existing
GIS software. Even free GIS softwareis uselessto a non-profit unlessthereis someone
in the organizationwho knows how to use it. Lack of GIS experiencecould drive nonprofits back into the armsof externalgroups,evenif free GIS software is available.
Therefore,similar to the benefitsof the "ease-of-use"goal for the K-12 educationmarket,
Mapalestershouldboth decreasethe amountof training necessaryto useGIS and,in the
process,increasethe numberof peoplein a given organizationwho arecapableof using
GIS. Hopefully, Mapalesterwill be ableto do so enoughthat a largenumberof nonprofits will be ableto internalizetheir GIS operations.

1.1.3 Analysis of the Personal Use Target Market
Despitehavingbeenwidely usedfor over thirty years,GIS hasyet to makethe
jump from the businessoffice, governmentcenter,and laboratory of academiato the
desktopof the consumer.Simply stated,the goal of Mapalesterin the contextof this
target market is to be the springboardon which GIS can make that jump. The two main
reasonsthat GIS cannotbe usedon the personalcomputerare price and compatibility.
The "free" and "Mac-compatible"developmentgoalsdirectly targetthesecauses.Also,
the "powerful" developmentgoal is a prerequisitefor the other two goals. Ease-of-use
doesnot generallyplay a role for the GIS fan who wantsto useGIS for her or his
paragraphs,
I will discussthe impactof the "free" and
personaluse. In the subsequent
"Mac-compatible"developmentgoalson this targetmarket.
BeforeI engagein this discussion,however,an examinationof hardware
requirementsof GIS in the context of the averageconsumer'spersonalcomputer is
appropriate.In otherwords,onepossiblereasonthat GIS could not be usedon personal
computersis that personalcomputersgenerallydo not have the "horsepower" to handle
GIS. This possiblerernon,however,is completelyrebuffedby the table in figure 1.1.3a.
This table showsthat there is nothing specialaboutGIS that makesit require extra
hardwarecomparedwith a sampleof standardconsumerPC applications.The table also
showsthat nearly all homePCs madein the last severalyearsor so should be able to run

MapalesterResearchProject

GIS satisfactorily.In otherwords,the installedbaseof consumerPCsis more thanready
for GIS.
)O0o or iP

tErt6l
iDCflIlr

trrlo flr t(P

IA!HH?

vT. 2000,or l(P

IDDTIHU

8/f6E hT- 2OC{ or lP

rrr

rB/tlF. hT- lORl or XP
VP

UE

D6.Etl.o

l?urs{.7
IrElEls 3

rcrtrfo 7.8
t3E9E

SDatrB

llamorr

Elilrlr

I56MB
I?AHE

rtr

i56t{8
taME
t2HE

r/r

gtTtt B

103$tB

atGll,

Figure 1.1.3a- Systemrequirementsfor a sampleof consumersoftwareapplicationsand the leading

Thecurrent:trilllffJC
applications.
GISsoftware

for
fromDellis included
configuration

Figure 1.1.3bdisplaysthe price of the leadingGIS softwareapplicationsfor the
consumersoftwareapplications
averageconsumer.The costof severalindustry-standard
areprovidedfor comparison.It is easyto seethat,at best,GIS softwareranksamongthe
most expensiveof consumersoftwareapplications,and at worst, well outsidethe
consumersoftwareprice range. Note that ESRI (EnvironmentalSystemsResearch
Institute)chargesthreetimesasmuch for ATcGIS9 with SpatialAnalyst asAdobe does
for its entiresuiteof creativeapplicationsthat includessuchpowerful tools as Photoshop,
Illustrator,InDesign,Golive, andAcrobat. Obviously,costis a very importantbanier to
the adoptionof GIS on the consumerdesktop.As such,the "free" designgoal will make

MapalesterResearchProject

Page

Mapalestera very appealingproduct within this targetmarket.

Full Pric€ for a Single Lic€ns€ of Leadang GIS Apps
and Other Consum€r Software Appllcatlons
$4,s00

$ ++,ooo

R $3,soo
=; Se.ooo
S,$z,soo
I $z,ooo

I sr,soo
E $1,ooo

E $soo
$o

Product
Figure l.l.3b - Priceswcre gathcred from s vsricty ofsources includilg tbe manufacturer and thc
nanufrcturcr's pricc on AEazoD.coE.

Even for students,for whom software is cheaperthanksto academiclicensing and
who will likely make up an important portion of the personalusetarget market,
Mapalester'spricewill be very appealing.Figure l.l.3c is the studentpricing analogyto
figure 1.1.3b.Despitethe significantstudentdiscountsprovidedby someofthe GIS
providers,Mapalesterwill still savestudentsat least$250. In additiotustudentsusing
Mapalesterwill not be subjecto someofthe restrictiveusagepoliciesthat often
accompanystudentdiscounts. For instance,the academicdiscount for REALbasic, the
softwareusedto program much of Mapalester,demandsthat no commercialsoftwarebe
producedwith the copy ofthe softwarepurchasedwith the academicdiscount.

Hecht

MapalesterResearchProject

Page I I

Stud€nt Price for a Slngle Llcense of Leading GIS App3
and Oth€r Consum€r Software Appllcatlonc
$4,s00

?
$4,ooo
o
R $3,soo
E
$3,000
q

S,$2,soo
I fz,ooo

? sr,soo
g $1,000

i

$soo
$0

*Eg
E'€

'69
EE
o

Y

6"gE

€F

= d

E
E
l ! o

TEE

Eg

E E

o 0 | E
o ! =
-9 toh l ) E

Ioa E
(J

Product
Figure Ll.3c - Priceswerc grthcrcd froD e variety ofsourccs ildudirg the manufrcturcr rod thc
manufscturer's price on Grrdwrre,com, t lcadbrgdiltributor ofstudqrt-discoutrtod softw8re.
Mrpltrfo studert discount pricirg wrs |rot casily svsilsble,

The "Mac-compatible"developmentgoal is alsoessentialto the personaluse
target market. As of this writing there are no viable, modem GIS software applications
availablefor the Macintosh platform. At one poinl ESRI developedGIS software for the
Mac, but the last version was releasedwith Mac OS compatibility is ArcView 3.0.
MAPublisher ($999, Avenza Software)is still regularly updatedand released,but it is
distributed as a plug-in for Adobe lllustrator and MacromediaFreehand, In other words,
MAPublisher is intendedalmost entirely for cartographicpurposes,not GIS purposes. As
such,the MacintoshGIS marketis essentiallyopenfor Mapalester'staking. According
lo marketresearohfirm IIrc (Dalrymple2005),Apple had about2.88 percentofthe
United Statesdesktopmarketshareand 4.99 percentofthe United Statesportable
computermarketsharein the fourth quarter of 20(M. The oorrespondingfigures for
Apple's globalmarketshare
were 1.75percentand2.93 percent,

Hecht

MapalesterResearchProject

Page12

1.2 Introduction to the GlScience Engineering of Mapalester
Now that the contextfor Mapalesterhasbeenestablished,most the remainderof
the paperis dedicatedto the GlScienceof Mapalester.The paperis divided into four
parts. The first sectionis this introductionto the paper.In the secondsection,I will
discussthe basicengineeringstructureof Mapalester,the decisionsbehindthis sffucture,
and my reasoningbehindeachof the decisions.The focusof the third sectionis a
descriptionof the heavily object-orientedstructureof Mapalester.The fourth sectionis
dedicatedto detailedanalysesof the computationalgeography,computerscience,and
softwareengineeringbehindsomeof the key functionalityof Mapalester.This section,
which cov€rsboth completedandwork-in-progressfunctionality,is quite largeand is
eachof which coversa specificfeatureor featureset.
subdividedinto subchapters,
Finally, the fifth sectionwill concludethe paperwith an analysisof the successof the
Mapalesterresearchprojectthusfar anda discussionof the project's future.
However,beforelaunchinginto a discussionof technicalaspectsof Mapalester,it
is helpful, due to the computersciencecontextof this paper,to engagein a brief
discussionon the history,use,promise,and currentstateof GIS technology.

1.3 Introduction to GIS
In the shortestermspossible,a GIS, or GeographicInformation System,provides
a "technologyand method"(Kerski 2004)to "visualize,analyze,and display" (ESRI
2005) spatialdata,or datathat canbe linked to a location. Someestimatessuggesthat
up to 80 percentof all datahassucha component(ESRI 2005). Much in the sameway
that graphshelp peoplevisualizenon-spatialdata"a GIS allows its usersto view and
analyzedatalinked to a locationwithin its spatialcontext. Applicationsfor GIS exist in
nearlyeverysingledisciplinewithin the socialandnaturalsciences,as well as in a large
numberof commercial,government,andnon-profit operations.Obviously,with sucha
largeand diversegroupof users,importantexamplesof applicationsof GIS arequite
aroundthe world areusing GIS to improveand
common. Fire andpolice departrnents
Hecht

MapalesterResearchProject

Page13

makemore efficient their provisionof emergencyservices.Political campaignsuseGIS
to analyzesocioeconomicspatialdatain orderto more accuratelytargettheir limited
funding. Similarly, the major nationalnewsservicesall usedGIS to aid in predictingthe
turn-outof the 2004 U.S. presidentialelection. Thousandsof companieshaveusedGIS
to assistin locationplanninganddeliverymanagement.The United Statesmilitary uses
GIS for a vastarrayof tacticalactivities. More relevantto the targetmarketsof
Mapalester,non-profit organizationsthat canafford GIS areusing it to empower
themselveswith a meansof visualizingand analyzingdatain way they were neverableto
before. Civic Builders,a non-profitin New York that is dedicatedto locatingnew
charterschoolswherethey will servethe New York communitythe best,hasusedGIS to
"greatly facilitatetheir analyses.'?(Keohane2005) Also in New York City, The Robin
Hood Foundation,which is dedicatedto helpingrid the city of poverty,"initiated a major
redirectionof resources"(CNrIr{P2005) afterusingGIS to analyzecurrentfunding sites.
Moreover,CMAP, or CommunityMappingAssistanceProject,is aNYPIRG project
entirely dedicatedto helpingnon-profitsempowerthemselveswith GIS. The immense
potentialof GIS hasbeenmakingnewslately. 1n2004,the U.S. Departmentof Labor
listed GIS as one of the three"most importantemergingand evolving fields" (Gewin
2004). The othertwo listedwerebiotechnologyandnanotechnology.
How exactlydoesGIS enablesucha diversearrayof uses? In the contextof this
paper,the bestway to answerthis questionis throughseveralexamples.A business
would useGIS to help locatea new storeby combiningdatalayersof all of the variables
it would considerimportantto sucha decisionandthen finding the site that optimizesall
of thesevariables.For example,a personwishingto opena small retail businessthat sold
ethnicfoodstuffsin a largecity would get ethnicitydataby block group from the U.S.
censusand zoning data from a local zorungauthority, and would use GIS to find the
optimumlocationfor her or his storein the city. A largercompanyor franchisewould
probably have a much larger array of datato optimize. In anotherexample,for a study on
Christiancontemporarymusic,I usedGIS to significantlyenhancemy knowledgeof the
subject. By creatinga databaseof over 500 largeconcertsby famousChristian
contemporarymusiciansand referencingthoseconcertsby their locationin a process
called"geocoding,"I was ableto developa map of the densityof the popularityof
Hecht

MapalesterResearchProject

Page14

Christiancontemporarymusic. Using the samemethodology- but with already-existing
spatially-referenceddata sets- I createdmapsfor a variety of demographicvariablesand
churchesof a variety of denominations. I then ran regressionson thesedensity grids and
the Christian contemporarymusic density grid" and was able to determinewhich of these
factorshad a causalrelationshipwith the locationof Christianmusic concerts.Although
GIS is most oftenusedwith datain the contextof small and large-scalelocationson the
surfaceof the Earttr,it hasalsobeenemployedin suchdiverseapplicationsas studying
the humanbrain(Zwlavsky et. al.2004). Any datathat canbe definedas attributesof a
location,no matterhow large-scaleor unrelatedto the traditionaldisciplineof geography
(like informationaboutareasof the brain),canbe visualized,analyzed,and displayedin a
GIS.
GeographicInformation Systemsare commonly defined in the literature as having
four components:hardware,software,data,and personnel. The personnelin the system
ask the geographicquestion,the hardwareand softwareprovide the technology for
answeringthat question,and the dataprovidesthe information. Mapalesterprovides the
softwareand,to someextent,the datapartsof the system;the userof Mapalesteris
expectedto supply any datanot includedwith Mapalester,hardware,and the personnel
part of the system.GIS is commonlymistakenlythoughtto refer to "geographic
information software," but in fact, the softwareis only one of the four essentialparts of
any geographicinformationsystem.Similarly, GIS is often confusedwith GPS,or
Global PositioningSystems.Although GPSunitsaxeone of severalways in which the
spatialcomponentof datais collected,GPSis a field separatefrom that of GIS.

MapalesterResearchProject

Page15

2. Basic Engineeringof Mapalester
2.1 Introduction to the Engineering of Mapalester
The most critical aspectof the core engineeringstructureof Mapalesteris the
division of codinginto trvo very distinctpartswith a very specificand limited interface
betweenthe two. Most of the front-endwork and someof the algorithmiccodeis in a
programminglanguagecalledREALbasic. The majority of the algorithmiccode,aswell
as all of the lower-levelfunctionality,isin C++. The REALBasicintegrateddevelopment
environment(IDE) offers an impressivebut somewhatlimited C++ plug-in interfacethat
allows most C** codeto run in the REALBasicfront-end,but the communication
betweenthe REALbasicinterfaceandthe C+r codeis restrictedby the application
programminginterface(API) for the REALbasicplug-in. The interfaceis also limited by
developmentstyleinherentto plug-in architectures.
the abstraction-oriented
In the remainderof this section,I will providea brief descriptionof REALbasic
and the REALbasicplug-in API. I will also discussthe reasoningbehindthe decisionto
usethis REALbasic/C++ two-part architecturegiven the original goals and target markets
of Mapalester.This discussionwill includea responseto criticismsover my choicenot to
useJavafor the project.I will alsodiscussthe specificchallengesencountereddue to the
architecture.

2.2 Whatis REMbasic?
In the wordsof REAL Software,the developerof REALbasic,"REALbasic is the
powerful, easy-to-use
tool for creatingyour own softwarefor Macintosh,Windows,and
Linux." In otherwords,REALbasicis an integrateddevelopmentenvironment(IDE) that
allows prograrnmersto generatenative code for Macintosh, Windows, and Linux from a
singlesetof codein the REALbasiclanguage.Probablythe closestanalogyto the
REALbasiclanguageand IDE is Microsoft's VisualBasiclanguageand IDE, although
elementsof Java(especiallythe heavily object-orientedfocus)and C++ canbe found in
the REALbasiclanguageaswell. For thosereadenwho areunfamiliar with these
products,figure 2.2a showscodethat sumsthe squaresof the first l0 integersandreturns
Hecht

MapalesterResearchProject

Page16

the valueto the user. While REALbasicand VisualBasichavenearly identicalcodein
this case,they divergesignificantlyin more complicatedalgorithmsand when objects
becomeinvolved.

VisualBasic

REALbasic

Sub firstlOlntegers0
Dim i, sumAs Integer

Sub firstl0lntegers0
Dim i, sumAs Integer

sum=0
Fori=0To9
sum:sum*i^2
Next

sum:0
Fori=0To9
sllln:sum*i^2
Next

MsgBox (sum)

MsgBox (str(sum))

End Sub

End Sub
C++

Java

#include<iostream>

publicclassSumSquares
{

int main (int argc,char * constargv[]) {
int sum,i;
for (i = 0; i < 10;i++X
sum=sum+i*i;
)

public staticvoid main (String args[]) {
int i, sum;
sum= Q;
for (i = 0; i < 10;i++X
sum=sum+i*i;
)

std::cout<< sum;
return0;
System.out.println(Integer.
toSting(sum));
)
)

)

Figure 2.2s - The four setsof code all do the samething, but they are written in different languages.

2.3 lVhyRB/C++?
Oneof the primary engineeringgoalsof Mapalesteris to makeit cross-platform.
The reasoningbehindthis goal arisesprimarily out of the needof the K-12 schoolstarget
market.The goal is alsorootedin two elementsnot as centralto the missionof the
researchproject. Firsf thereis no viablg modernGIS availablefor the Mac besidesa
Hecht

MapalesterResearchProject

Page17

non-userfriendly port of the UNIX-basedGRASSopensourcesystemthat is notoriously
difficult to use. Second,while I am by no meansinexperiencedat using and developing
softwareon a PC, my designsensibilitiesaremuch more suitedto Macintosh
development.
The cross-platformdevelopmentgoal left me with threeoptionsfor my
developmentplatform. First,I could attemptto producea maximally portablecoresetof
codeandthen developthe portionsthat areplatform dependent(interface,drawing
engine)for eachplatform. Second,I could useJava,alanguagewith which I was very
familiar. Thir{ I could useREALbasic,and its C+r plug-in architectureif necessary.I
eliminatedthe first option quickly, as I was not familiar enoughwith the Mac or
WindowsAPIs to not forcemost of my developmenttime into learningthoseAPIs.
Also, asthis was a fundedresearchproject,I neededto havesomethingto show for my
not just a pile of portablecodewithout an interfaceor an interface
work as I progressed,
without much GIS functionality. This left me with the choiceof eitherJavaor
REALbasic. In the end I choseREALbasicover Javafor the following reasons.First,
Javais notoriouslyslow andwhile REALbasicis alsosluggishcomparedto someother
languages,the C++ plug-in architecturewould allow me someleeway. Many functions
in GIS requirethe processinganddisplayof millions of piecesof datain microseconds,
and thusspeedis a very importantfactor. Second,with REALbasic,I could develop
interfacesthat were native to eachplatform, whereasJavainterfacesalways look
is one of the threeprimary
somewhatforeign and awkward. Consideringthat ease-of-use
goalsof Mapalester,a comfortableinterfaceis a very importantfactor.
However, beforeconsideringinterfacefamiliarity as a factor, I went looking for
programsthat would be usedextensivelyby any non-profit,K-12 school,
any Java-based
or personalusers. After all, if theseusersare familiar with the quirks of the Java
interface,thenJavamight providean equallycomfortableinterfacefor Mapalester's
target users. While it is hard to predict the activities of the personaluser category,the
only application that I could find that I assumedthat my other target marketswould use
that was programmedin Javawas Limewire, a music-sharingprogram. REAL Software
realizesthat it sharesa certainmarketwith Javaandpublishesa "REALbasic vs. Java"
comparisonon its website. On this site,it lists the problemswith Java'sinterfacesin
Hecht

MapalesterResearchProject

Page18

more detail. REAL Softwareis correctto point out that "unlike Java,REALbasic
provides fully native controls with native behavioron all supportedplatforms." It also
statesthat "REALbasic compilesto native machinecodefor eachplatform elirninating
the need for virtual machines,specialinstallersand environmentalvariable settings" and
that "REALbasic provides accessto the uniquefeaturesof eachplatform such as ActiveX
andthe Registryon WindowsandApple EventsandKeychainon Mac OS X." For these
two reasons,despitebeingmorefamiliarwith Java,I decidedto choosethe REALbasic
route.

longuntilpu evohc?

yourevolution
today.
C' Begin
Clkk lo go lo our odln! store.

Figure 23a - REAL Softlyare has e high opinion of its project comp.red with competioglanguages.
It w8s the target markets of Mapalestertbst determitredmy choiceof progr8mmitlg hnguage more
thatr any sort ofjudgment oftbe lsnguagesthemselves.Image from
http://www.r€alsoftw&re.com/realbrsic/compare/

2.4 The challenges of my chosen architecture
I encounteredthreemain problemsdue to my choice of engineeringarchitecture,
althoughI believethat the collectionof obstacleswould be greaterin numberand
difficult if I had chosena different architecture. In order of difficulty the problemswere
(l) I neededto refamiliarize myself with REALbasic and learn nearly every aspectof the
contentwould be
language,(2) I neededto negotiatewhat algorithmand object-oriented
Hecht

MapalesterResearchProject

Pagei9

in the C++ plug-in format and what would be in the pure REALbasic format, and (3) I
neededto learnC#.
While I had engagedin minor programmingprojectsusing REALbasic prior to
Mapalester,I had never worked extensivelyin REALbasic. In additio4 it had beenquite
a while sinceI had usedthe REALbasic integrateddevelopmentenvironment.As such,
prior to starting on the Mapalesterproject I spentseveralweeksworking with the
REALbasicenvironmentandrefamiliaizingmyself with the language.I also spentmuch
time in the REALbasic languagereferenceguide, a text that becamea greatresourceas
the project continued. When I startedprogrammingMapalester,I did not have the depth
of knowledgein REALbasicto completethe REALbasicportion,but I had the
backgroundand familiarity with the necessaryresourcesto learn most anything I needed.
The secondproblem, deciding what I would implement in REALbasic and what I
would implementin C**, plaguedme for a long time. Essentially,the REALbasicplugin API allows me to $eate a MapalesterAPI with which to work in REALbasic. But
what do I implement in the API and what do I leave in REALbasic? My initial guideline
involvedthe factorsof speedand low-level access.Due to the fact that REALbasic
performs automatic garbagecollection, its code tendsto run slower than native C+r code
in the REALbasic format. As such,my initial venturesinto C++ coding were motivated
by the runningspeedof severalimportantfunctions,suchasprojections(section3.4) and
datadrawing(section3.2). Additionally, REALbasicstruggleswith recursivealgorithms
(algorithmsthat call themselves)that reachdepthsof around50 or more function calls.
Sincemany of the important algorithms are recursive,it was faster to run these
algorithmsin C++ codethanin REALbasic. Theoretically,sinceall of thesealgorithms
aretail-recursive,I could havemadeiterativeversionsof all of them. In fact, I did
implementiterativeversionsof somerecursivealgorithms,mostnotably,the line
generalizationalgorithms(section4.3). However,it becamequite tediousand difficult to
make theseconversions,especiallysinceI could run the recursiveversionsin C++ and
achieveacceptableperformance.
I soondiscoveredthat I could speedup somealgorithms,especiallythosethat
load in andprocessdatafiles, by accessingmemoryand disk dataata low level.
However,REALbasicoffersno byte-levelor bit-level accessto binary data,eitheron
Hecht

MapalesterResearchProject

Page20

memoryor on disk. The lowest-levelaccessREALbasicprovidesis at the word level.
As such,the level of memoryanddisk accessbecamean importantfactor for the
programminglanguagedecisionaswell.
It turnedout that thesetwo factors- speedand low-level access- in combination
with Mapalester'sobjectorientedstructure,led to a simpleand very importantrule for
codeseparationthat I now useas a successful"rule of thumb". As is discussedin gxeater
detail in section3.3, Mapalesterconsidersspatialinformationon the shapelevel andon
the datalayerldatasetlevel. The shapelevel dealswith individual shapes(points,
polygons,etc) andtheir vertices. The datalayer level representsan entiresetof shapes
suchas,for instance,the setof polygonsthat representcountiesin Minnesota.
Conveniently,all of the algorithmsthat haveneededC++ speedthus far only concern
datarelatedto the shapelevel. Likewise,the low-level accessfunctions,while possible
to implementat the datalayer level,canalsobe run at the shapelevel. As such,I
establisheda firm rule in orderto avoid switchingcodeback and forth betweenthe
"MapalesterAPI" and the REALbasicuseof that API. All classesand associated
algorithmsthat dealwith the shapelevel mustbe codedin C++. All classesand
algorithmsthat dealwith the datalayeras a whole must be prograrnmedin
associated
REALbasic. The REALbasicC*+ plug-in interfaceis usedto navigatebetweenthe two
layers. This navigation is quite complicated,and too intricate and tangentialto describe
herein detail.
It is interestingto notethat evenin topicsthat are seeminglyrelegatedexclusively
to the realm of softwareengineering,the basicsof geographybecomea factor. Prior to
establishingthe aforementionedrule, my code was split betrveenREALbasic and C+r
through educatedguessingand intuition. Once I groundedthis software engineeringin a
GlSciencecontext,the choiceof programminglanguagebecomemuch simplerandwell
defined.
The final andmost difficult challengerelatedto the chosendevelopment
architectureinvolved learningC#. While this processis by no meansworthy of a long
descriptionin this context,it is importantto notethat evenjust the C# portion of
Mapalesterhasbeenthe largestprogrammingproject I have ever attemptedin a language
otherthan REALbasic,or VisualBasic. A largeportion of developmentime was spent
Hecht

MapalesterResearchProject

Page21

reseaxchingand learning appropriatememory managementechniques,gaining a
functionalunderstandingof pointersto pointersto pointers(etc), and comprehending
templates.

MapalesterResearchProject

Page22

Structureof Mapalester
3. The Object-Oriented
Structure
3.1 An Overviewof the Object-Oriented
In its current state,Mapalesteris comprisedof over 10,000lines ofcode in four
languages(REALbasic, C+, SQL, XML) that are organizedinto an elaborateclass
structure. In order to help the readermake senseof this structureand better understand
the overall architectureof Mapalester,I have divided the classstructwe into several
subsections.The subsectionsoperatemostly independently,but havekey interactions
with eachother. The four subsections,which I will discussin the subsequentparts of this
chapter,are the interfacesystem,the datainteraction system,the projection systen! and
the databasesystem. In eachpart, I will describeand analyzethe architectureand basic
functionality of the subsectionof the classstructurebeing discussed.I will also detail the
primary interactionswith othersubsections.
subsection's

3.2 TheInterface System

tu!a.dr'.(-l

-* t-n

Hecht

MapalesterResearchProject

Page23

Figure 3.2e. The object-oriented nature ofthe interface ofMapalesfer can be seenin the above
screenshot. Notice the replication of windows and maps. Due to use of the object-oriented
architecture, such replicotion required almost no additional coding.

The REALbasic IDE containsa large variety of interfaceelementsorganizedin an
efficient and logical classstructure(Brandt 2004). In order to take advantageof the
benefitsof this hierarchywhile still modifuingthe userinterfaceelementsto fit the needs
of Mapalester,I primarily useda subclassingmethodologyfor most of my interface
classes.In total, Mapalestercurrentlyhasmorethantwenty individual classesthat are
subclassed
from REAlbasic's interfaceclasses.Most of theseclassesprovide a very
specificfunctionalityto a standardinterfaceelement.For example,Mapalesterhasmany
bevel buttonsthat, when pressed,bring openthe operatingsystem'scolor chooserand
displaythe color chosenas a buttonicon. To implementthis functionalityin a portable
REAlbasic's bevel button and input the
and reusablemanner,I havesimply subclassed
necessarycodeinto the draw0 and actionQmethodsof the subclass.
There are, however,severalvery important classesin the interface classstructure
that haveextensivealgorithmscontainedwithin them:the GISWindow class,the
GlSMapElementlist,andthe GlSFormatWindow.The GISWindowis the most
dominantfeaturein the user'sexperiencewith Mapalester.EachGISWindow contains
aswell as elementsthat
elementsthat interactwith all threeotherclasssubsections,
accessother parts of the interfaceclasssubstructure.From GlSWindows, the number of
instancesof which is only limited by availablememory,userscan accessthe spatialdata
database(section3.5),performmany GIS operations,and engagein layout,input and
exportoperations(section3.3). Moreover,eachGISWindow containsan instanceof the
GlSMapElementlist(later in this section). The GlSFormatWindowis the only other
major site of programcontrol (later in this section).
In additionto its key role in userinteraction,the GISWindow also servesasthe
documentunit of Mapalesterand is roughly analogousto a "project" in ESRI's GIS
products. When a userperformsa load or saveoperation,it is the GISWindow that takes
control. Using an XMl-based format,the GISWindowrecursivelygoesthroughall of its
membersthat needto saveinformation, requestingthat eachmembersaveits information
in a nestedsectionof the resultingXML document. The reverseis donewhen the user
wishesto load a savedXML file. Thesemembersinclude everything from
Hecht

MapalesterResearchProject

Page24

(seesection3.3) and,when completed,all of its
BackgroundlayerCanvas
GlSlayoutElements(seesection3.3). Not all of the savefunctionality is complete,but
the basicsystemis establishedand is functioningfor the GISWindowclassitself, along
with a subsetof its members.In figure 3.2b,Lhaveincludedan exampleof the XML
contentof a savedGISWindow. The structureof the XML file reflectswell the objectoriented structureof the interfacesystemand other parts of the progftrm. It is also
important to note that when Mapalesteris released,this structurewill be releasedas an
openfile format. The extensionof files in this format is ".mmap."
< ?xmlversion--"I .0 " encoding:'UTF-8 "?> <plist
version=n1.0"><dict><key>gislYindow</key><dict><key>Left</key><integer>
334</integer><k"yrT
op</l<ey><integer>55</integer><key>Ilidth</key><integer>853</integer><key>Height</key><integ
er> 694</integer> < key>Background Layer< /key> <dic t> < key>Fill
Color</key><dict><key>R</key><integer>255</integer><ley>G</key><integer>255</integer><key
>B </key> < integer>255</integer> </dict> <key>Border
lfidth< /key> < integer>0< /integer> <key>Border
<key>G</Ieey><integer>0</integer><key>B<
Color</key><dict><key>R</key><integer>0</integer>
/key><integer>O</integer></dict><key>UseColor Fill</key><true/><key>Picure
Transparency</key><real> I </real> <key>Picture Display
Method</key><integer>2 </integer></dict> <key>Llbrary
Browser</key><dict><key>Map</key><dict><key>1</key><integer>I4</integer><key>2</key><int
5
eger>2O</integer><key>3</key><integer>
I5</integer><key>4</key><integer>22</integer><key>
</key><integer>26</integer><lcey>6</key><integer>
I8</integer><key>7</kq><integer> I I</intege
r><key>8</key><integer>28</integer><key>9</key><integer>29</integer><lcey>
I0</key><integer
> 30</integer><key>I I </key><integer>3l </integer><key>I2</key><integer>24</integer><key>I j<
/kq><integer>2</integer><key> I4</key><integer>3</integer><key>I5</key><integer>4</integer>
<ley> l6</ley><integer> 5</integer><key>l7</key><integer>6</integer><key>l8</key> <integer>7
</integer><key>I9</key> <integer>8</integer><key>20</key><integer>g</integer><key>21</key>
<integer>I0</integer><key>22</key><integer>I2</integer><kqt>23</key><integer> I3</integer><
key>24</key><integer>I6</integer><key>25</key><integer>l7</integer><key>26</key><integer>
19</integer><key>27</lrey><integer>21</integer><kqt>28</key><integer>25</integer><key>29</k
I </kcy><integer>I 55</integer><k
e1t><integer>27</integer></dict><key>Widths</key><dict><key>
ey>2</key><integer>76</integer><key>
3</key><integer>84</integer><key>4</key><integer>94</i
nteger><key>5</key><integer>54</integer><key>6</key><integer>82</integer><key>7<ft,ey><inte
ger> 52</integer><key>8</key><integer>
I l4</integer><key>9</keyr<integer> 109</integer><key>
10</lcey><integer>
104</integer><key>I I </key><integer>106</integer><ley> 12</key><integer>l7
S</integer><key>I j</key><integer>&0</integer><key>l4</ley><integer> l0l</integer><key> l5</k
ey><integer>129</integer><key>l6</key><integer> 138</integer><key>I7</key><integer> 144</int
eger><lrey>l8</key><integer> 13?</integer><key>l9</key><integer>83</integer><kq> 20</key><i
nteger>78</integer><key>21</key><integer>65</integer><key>22</key><integer>5?</integer><ke
<integer>50
y> 23</key><integer>S0</integer><key>24</key><integer>50</integer><key>25</key>
</integer><key>26</key><integer>5?</integer><key>27</key><integer>
100</integer><key>28</ke
y><integer> 124</integer><key>29</key><integer>47</integer></dict></dict></dict></dict></plist

Figure 3.2b. This XML code representsa Mapalester saveddocument.

MapalesterResearchProject

Page25

The primary function of the GlSMapElementlist, which is only instantiatedinside of
GlSWindows,is to provideaccessto a list of the VectorThemesof the currentlyselected
GISCanvas.From this list, via the GlSFormatWindow,userscan makecritical changes
to the contentand display of eachVectorTheme. Additionally, it is through the
GlSMapElementlist that usersare able to manipulatethe ordering of the data layers,a
key aspectof GIS functionality.To enablethis orderingfunctionality,the
GlSMapElementlistcontainsa heavilymodified implementationof abubble sort
algorithm that interactswith both the host GlSMapElementlist and the affected
GISCanvas.Usersarealsoableto enableanddisableVectorThemesthroughthe
GlSMapElementlist, functionalitywhich comprisesyet anothercornerstoneof GIS.
The GlSFormatWindowis a Mapalester-onlyfeature. As a GIS lab assistant,it is
my perceptionthat one of the gleatestfailings of currently available GIS softwareis the
hiding of a vast anay of important featuresin non-contextsensitivewindows that can
only be accessed
from deepwithin menusor throughobscurebuttonson the toolbar.
This failing, which is partially a resultof the extension/module-based
developmentof
many GIS packages,hastwo major ramifications.First and foremost,inexperienced
usersare often unawareof important and powerful operationsand settingsthat can be
appliedin a given context. For the educationmarket,this ramificationis particularly
important. Wilder et. al. (2004),for instance,notethat teacherslearningGIS during inservicesessionscantendto view GIS as simply a "digital map" devicefrom which they
can print referencemaps. Second,problemsare often harderto solve as the important
informationis not immediatelyavailableto the user. While someGIS packageshave
madestridesforward in solving theseproblemsthrough the use of the contextualmenu,I
believethat the GlSFormatWindowdoesa betterjob at providing quick and contextsensitiveaccessto all of the importantoperations,settings,and information. It doesso by
makingits largenr:rnberof panelsvisible or invisiblebasedon the currentlyselected
elementof the userinterface. For instance,if the userhasa GISCanvasselected,the
GlSFormatWindowwould only displaythe panelsthat function with a GISCanvas.If the
userselecteditems in a GlSMapElementlist, the GlSFormatWindowdisplaysall of the
panelswith controlsthat relateto the modificationor displayof VectorThemes.If the
userhasselectedseeminglydisparateuserinterfaceelements,the GlSFormatWindow
Hecht

MapalesterResearchPdect

Page26

only displayspanelsrelevantto all selectedelements.In otherwords,
GlSFormatWindowdisplaysthe panelsin the setresultingfrom the intersectionof the
panelsrelevantto the selectedelements.Both Microsoft Word 2004 for the Mac and
OmniGraffle by OmniSoft have similar, but not identical, features.
The GlSFormatWindow'sfunctionalityis implementedthroughthe extensiveuse
of the classinterfaceconstruct.Eachand everypanelthat canbe displayedin the
GlSFormatWindowhasa correspondingclassinterface. For instance,the
which is implementedby the
is linked to the ProjectionPanellnterface,
ProjectionPanel
with the
corresponds
GISCanvas.Similarly, the BackgroundPanel
which is implementedby both the GISCanvasand the
BackgroundPanellnterface,
BackgroundlayerCanvas. Each interfacerequiresthat classesthat implement it have the
full setof the methodsrelatingto the optionsin thepanel. For instance,classesthat
must be able to changethe contentof the
implementthe BackgroundPanellnterface
backgrounddisplayof the class. The beautyof the classinterfacemethodologyis that the
definition of what is the "backgrounddisplay" is entirelyup to the contextof the class.
(and severalothers)
The classmust simply havea methodcalledsetBackgroundDisplay0
that canbe calledfrom the panel.
The five panelsthat are finished are the ProjectionPanellnterface,which is the
interfaceto the coordinatesystemfunctionality, the PicturePanellnterface,which is
exclusivelydedicatedto featuresin the PictureElementclass(section3.3); the
NamePanellnterface;which is central to nearly all aspectsof the interface that usethe
which is describedabove.
GlSFormatWindow;andthe BackgroundPanellnterface,
Cunently under developmentis the LayerFormatPanellnterfacefrom which userswill be
able to make a large portion of basicchangesto layer symbology. Many more interfaces
are plannedand will be implementedas I implementthe featuresthat the interfaceswill
contain.
How doesthe GlSFormatWindowknow what user interface elementsare
selected,and thuswhat panelsto display? The forefrontGISWindow is in chargeof
maintaininga stackof all selectedelementsof theuserinterface. This meansthat the
GISWindowalsodecideswhat is meantby "selected." For instance,if nothing is
selected,the GISWindowplacesthe instanceof the Backgroundlaye€lass on the stack,
Hecht

MapalesterResearchProject

Page27

becausethis is the most intuitive choicebasedon the interface. Also, if the userselectsa
memberof the list in the GlSMapElementlist,the GISWindowpopsall otherelementsof
the stackand pushesthe correspondingVectorThemeon the stackbecausethis is, given
the interface,intuitively what should occru. Eachtime the stackchanges,the
GISWindowsendsa messageto the GlSFormatWindow,which is in effect a global
variable as only one instanceof it may occur. The GlSFormatWindow then examinesthe
stack. Whenthe GlSFormatWindowfinds an instanceof a classthat doesnot implement
an interfacecorrespondingto a panel,it makesthat panelinvisible. The panelsthat
remain are the panelsthat are implementedby all of the selectedelementsand are thus,
context-sensitive.
Otherkey classesrelatedto userinteractionwith Mapalesterare the MenuBar
classand the contextualmenuclasses.At the moment,all of theseclassesoffer a rather
mandateset of featuresand a correspondinglystandardset of algorithms. However, when
Mapalesteris released,they will be semi-criticialto userinteractionwith Mapalester.
Both the menu bar and contexfualmenuswill provide accessto important features
inaccessiblethroughothermeans.For example,the insertionof a GISCanvasclassinto
(section3.3) - otherwiseknown as addingan additional
the BackgroundlayerCanvas
map frame to the document- will be a function exclusively available through the menu
bar and contextualmenus. Also, becauseboth the menu bar and contextualmenushave
content,the classesthat providetheir functionalitywill probablyshare
context-sensitive
codewith the GlSFormatWindowin a mannerthat is yet to be established.

3.3 The Data Interaction System
To the user,all data interactionoccurswithin the context of the GISCanvas,the
classthat provides the connectionbetweenthe interfaceclassstructureand the data
interactionclassstructure.I will beginby discussingthis classand its relatives,andwill
then delve deeperinto the classstructurebehind the functionality of what actually is
displayedin the GISCanvas.
The GISCanvasis a subclassof the GlSlayoutElementclass. In each
GISWindow(section3.2),the BackgroundlayeCanvas(section3.2) maintainsan array
Hecht

MapalesterResearchProject

Page28

of GlslayoutElements placedinside the BackgroundlayerCanvas. Currently, there are
only two classesof the type GlSlayoutElement: the GISCanvasand the PictureElement
class. The PictureElementclassrepresentsa picture placed in the
BackgroundlayeCanvas by the user. As I implementmore firnctionality in Mapalester,
the number of classesofthe type GlSlayoutElemant will drastically increase. For
instance,soonunder developmentwill be a LegendElementand MapscaleElement,
which will be responsiblefor handling functionality relatedto the display and
manipulation of map legendsand map scales,respectively.Figure 3.3adepicts the
relationship betweenall of the aforementionedclassesin a semanticnetwork.

Flgure 3.3a- Th3 Interfacebetwsenthe data Intsractlon system and the Intorfac€ cla38
3tructure. MapscaleElemcntand LegendEl€menthave yet to be impl€mentedare are
deplcted as sample$ of futurs clsses of tyPe GlsLayoutElemsnt'

Hecht

MapalesterResearchProject

PsEe?9

A BackgroundlayerCanvaswith all of the aforementionedGlSlayoutElements (and any
future ones)will be ableto be printed and exported. As a side note, this meansthat I
havechosento eschewthe layout vieddata view constructcommonto ESRI products.
Now that the contextin which the GISCanvasclassoperateshasbeenestablished,
it is necessaryto explainhow the GISCanvasdisplaysspatialdata. The largestchallenge
in designingthe GISCanvaswasmaking its functionalityuniversalto all typesof GIS
datathat will eventually be supported.The answerto this challengewas making the
GISCanvasinteractwith the datait containsonly on the layer level. Basically,each
GISCanvashasan arrayof VectorThemeso
eachof which areresponsiblefor returningto
the GISCanvasan image(essentially,just a picture- like any JPEG)of what it looks like
given the extentof the GISCanvas.WhenI implementthe RasterThemeclass,this class
will alsobe responsiblefor simply returningan imageof what it looks like in the given
extent. Whenthe GlSCanvas'sextentchanges,say,becausethe userhaszoomedinlout
or panned,the GISCanvasrequestsnew picturesfrom eachof the VectorThemes(or,
later,RasterThemes
as well) containedwithin its VectorThemestack.Essentially,every
time the GISCanvasredraws,all it doesis pancakeall of the returnedimagesfrom the
VectorThemeson top of eachin the correctorder. This ordercorrespondsto that which
the usermanipulatesusing the GlSMapElementlistclass(section3.2).Layersthat have
been"turned ofP'in the GlSMapElementlistare skippedin this "pancaking"process.
How do the VectorThemesdraw an accurateimage of themselvesin any given
extent?Eachinstanceof the VectorThemeclassis responsiblefor askingits C++ parent
classto queryall of its VectorObjects(Pointobjects,PolylineObjects,or PolygonObjects)
to createthe appropriatedisplay. This querywill eventuallyutilize an R-treeindex (see
section4.2) which is attachedto everyVectorTheme,but for now usesthe brute force
approachoutlinedin section4.2. Note that this interactionbetweenthe VectorThemeand
the correspondingVectorobjectsis the singlemostimportantinterfacebetweenthe C++
plug-in codeandthe REALbasiccode. In fact, astouchedupon above,the VectorTheme
is actuallya subclassof a VectorThemeBase
classimplementedin the C+r plug-in. This
subclassingis the constructby which the two codebasesinteract. When the REALbasic
VectorThemeneedsto updateits cachedpicture, it simply calls the updateQfunction,

MapalesterResearchProject

Page30

which hasbeenprogrammedin the Q+* superclassand only dealswith C+-r elementsof
Mapalester.
Oncethis update0function,which is provideda two-dimensionalextentas a
parameter,has identified which VectorObjectsit needsto draw using the spatial indexing
methodsasnotedabove,the actualdrawingprocessis quite simple. Sinceall coordinate
systemsaretreatedastwo-dimensionalCartesianplanesin Mapalester(seesection3.4),
the update0 function first makesa new image the samesizeinpixels as the GISCanvas0
in which the VectorObjectis located. The functionnext determinesthe scaleof the
imagein the form of a uniVpixel ratio. This unit can be any angularor linear unit
becauseby the time the drawing processhasbegunand the update0 function hasbeen
called, the projection enginehasmadeall necessaryarangementsto convert all of the
VectorObjectsand their constituentpoints in all the VectorThemesto the correct twc.
dimensionalcoordinatesystemfor the GISCanvas.Next, using the scaleas a guide,the
update0 function draws all the VectorObjectscontainedwithin the extent onto the image.
Finally, the imageis returnedto GISCanvas.This processis showngraphicallyin figure
3.3c. Figure3.3b showsthe whole datainterfacesystemclassstructure"behind" the
GISCanvasin a semanticnetwork.

MapalesterResearchProject

Page3l

I

ti

E
E

5

Flgure 3.3b - A semantic network depicting the data Int€raclion systEm that operates
'b€hlnd" I GlSCanyas. Noto the dlvlsion of programming betYtesnC# and REALbasic.
Also note that VectorPointsand VectorPolygonsaro both subclassos of othel
Vectorobjects. I have lmplement6dthese tYvoclasses In this manner In ord€rto maxlmally
ahars cods. In effect, a VectorPoint i6 a VectorMultiPointwlth Just one polnt In it.
Slmllady, a VectorPolygon is a special case ofa VectolPolyline In whlch the flr3t and ths
last point are the same. lmplomentingthe four Dssic georDetrlctypes in a hleralchical
mann€r has saved me from writing thousands of linss of code throughout the program.

Hecht

MapalesterResearchProject

Page32

SampleGIS CanvasLayer
CmrdlnaleSystem:UTMZone1S
Scale:100metBrs/pix6l

Y-atdE
l0 plxels
INO n?€iters

X"axlg
15 plxels
1ffi0 meters
Figure3.3c- Thebasicsof the actualdrawingpartof the update$function.

3.4 The Projection System
Every spatialdatasethassomesort of coordinatesystem.This coordinatesystem
canbe a projectedcoordinatesystemor an unprojectedcoordinatesystem. Spatialdatain
a projectedcoordinatesystemhavecoordinatesthat are in somesort of x,y coordinate
systemwherex andy representvaluesin a Cartesianplane. Projecteddatahavebeen
transformedusing one of manyprojectionequations,suchas that for the Mercator
projectionor the LambertConformalConic projection. A commonunit for projected
coordinatesystemsis the meteror the kilometer;all projectedcoordinatesystemsutilize
units of length. Spatialdatain unprojectedcoordinatesystemshavecoordinatesthat
representdegreeson someellipsoid(or spheroid).A commonunit for unprojected
MapalesterResearchProject

Page33

coordinatesystemsis decimaldegreesof longitudeand latitude;all unprojected
coordinatesystemsutilize angularunits. Unprojectedcoordinatesystemsare sometimes
incorrectly referredto as a data's "datum." Every projected coordinatesystemhasan
underlying unprojectedcoordinatesystemor "datum", as the x and y valuesmust be
generatedfrom original degreevalues.
In orderto be a viable GIS, Mapalestermust havea robustprojectionsystemthat
can convertbetweenall of the coordinatesystemsin standarduse. This is an immense
task. Thereare over thirty commonprojections,eachwith its own highly complex
equation. Many of the equationsacceptfive or more variablesin addition to the standard
latitude and longitude coordinateparameters.Additionally, there are an equally large
numberof unprojectedcoordinatesystemsbasedon a variety of ellipsoidapproximations
of the Earth. In order to display dataaccuratelyin the sameview frame, Mapalestermust
be able to convert datain any coordinatesystemto eachand every ofthe other coordinate
systems.In orderto implementsucha projectionsystem,codemust be organized
efficiently in a simplebut robustclassstructure.
The structureI eventuallysettledon for Mapalesteris basedon my researchinto
coordinatesystemsand my investigationinto how coordinateinformationis stored,such
as in the ".prj" file discussedin section4.1.4. Becauseall coordinatesystemshavesome
sort of projection- evenif that is'trnprojected"- the primary classof the projection
systemis the ProjCSclass.The ProjCSclassis responsiblefor changingthe projectionof
the coordinatesystemwhereasthe GeoCSclasstakescareof converting the underlying
unprojectedcoordinatesystem,a processthat mostly involvesthe scienceof "datum
conversion"but hasotherimportantaspectsaswell. No datumconversionfunctionality
hasbeenimplementedin Mapalester.As such,an error of about800ft at largescalesis
possiblewhile currentlyviewingdata in Mapalester.Thereare four more classesthat
makeup the projectionsystem:the Spheroidclass,the PrimeM(eridian)class,the Datum
class,and the Unit class.Eachis responsiblefor convertingthe elementsof the
coordinatesystemthat correspondto its name. The basicrelationshipsamongthe classes
is depictedin figure 3.4ainthe form of semanticnetwork.

MapalesterResearchProject

Page34

u36
r!€3

amongths claEtosof ths
Flgure3.4a-A simpllfledsemanticnetwo* of the relationshlPs
prolectlonsy3tem.Noiethatthe projectlonsystsmmakeaextonslvEuse of C+++oded
functlon8,but no C++codedcla3ses.Thls ls a malordeparturefrom the ollglnalvsrsion
of the projectlonsystem,whlchhadall of the codeIn REALbaeic.TheREALbaslcode,
provgdtoo slowfor the morscomplicatedfunctlonsand algorithms,andthu8,a
hoyrever,
switchto C++waan€oesaary.Thl3changewas also madgto fudhel enforcethe rulethat
REALbasicneyerhaveacceasto the Vectorobiectsof a VcctorThsme.All of the
accessto the sPatialInfolmatlonof a Vectolobjgct,
algortlhmsshownroqulrsvertex-level
andthus mustbe in C++codeaccordingto the rule. TheC++codlng13not c,omPbte.
Every VectorThemehasan instanceof a ProjCS class. In addition, the GISCanvasclass
also has a ProjCS member. In order to accuratelydisplay the infonnation (or display the
information at all in many cases),the GlSCanvas'sProjCS and the VectorTheme's
ProjCS must rnatchcompletely.Meeting this condition is the prirnary function of the
projection systemand is an excellentdemonstrationofthe effectivenessoftle system's
object-orientedstructure.
Hecht

MapalesterResearchProject

Page35

The processof meetingthe conditionis as follows: when a VectorThemeis
loadedinto a GISCanvas,the GISCanvaspassesthe VectorTheme'sProjCSinstanceto
the convertQfunctionof its own ProjCSinstance.The convert0 function is the
commandcenter for the projection conversion. If the projection, parametersof the
projection,or the GeoCSof the inputtedProjCSdiffers from that native to the
GISCanvas,the convertQfunctiontells the inputtedProjCSto unprojectitself. Before
doing so, if the inputted ProjCS hasa unit other than meters,the inputted data's unit must
be changed,as all the constantsin the forward and reverseprojection algorithms are in
meters.The inputtedProjCSthencallsthe appropriatereverseprojectionequation
function (section4.6). If the GeoCSdiffers, the convert0 function thenpassescontrol to
the convert0 functionof the ProjCS'sGeoCS. In the GeoCS'sconvert0 function,the
datum(andits spheroid)andthe primeM of the inputtedProjCS'sGeoCSareconverted
using the datum conversionfunctions and the prime meridian conversionalgorithms
(section4.5). The angularunit of the GeoCSmay alsobe convertedin the GeoCS
convert0 function,if necessary.The GISCanvas'GeoCS'sconvert0 function then
returnscontrol to the GISCanvas'ProjCS0 function. If the inputtedspatialdatawas
unprojectedusing the reverseequations,thenthe datamustbe projectedusing the
forwardprojectionalgorithmsof the GlSCanvas'sProjCS. Finally, it may be necessary
to convertthe unit of the forwardprojecteddatato matchthat of the GISCanvas'ProjCS.
The two coordinatesystemswill then match.

3.5 The Database System
There are two important determinantsof the object-orientedstructureof the
databasesystemin Mapalester. The frst is the dual usesof the systemat a fundamental
level. The databasestructureis not only usedto manageattribute data inherentto every
GIS file, but alsoto managethosefiles themselves.Section4.4 is dedicatedto the
descriptionof this secondfunctionality.Not only did this dualismin intendedfunction
reinforce the needfor a clean and efficient object-orientedstructure,but it also shapedthe
designof the structure. The secondmajor determinantof the structureof the database
objectsis my choiceof the Valentinadatabaseby ParadigmaSoftwarefor the core
Hecht

MapalesterResearchProject

Page36

databaseinfrastructure2.Implementationof the iTuneslike GIS data file management
hasbeengreatlyfacilitated
system,aswell asprovisionof supportfor atfributedatabases,
by my choice of the Valentina databaseinfrastructureas the framework for Mapalester's
object-orienteddatabasestructure. As an object-orientedrelational databaseframeworlg
Valentinaprovidesall of the low-level databasefunctionalitythat would be too tangential
to GIS to programfor this project.Valentinais availablefor a largenumberof
programminglanguagesand it providesamazingsupportfor REALbasic. In the
paragraphs,I will discussthe database
subsequent
classstructureof Mapalesterin the
context of thesetwo determinants.
The classstructureprovidedby Valentinafor REALbasicforms the basisof
Mapalester'sdatabaseclassstructure.Thereare severaltypesof classesin the Valentina
framework. The VDataBaseclassrepresentsa completedatabase.In its current stateof
development,Mapalesteronly interactswith a single completedatabase,the library
file locatedin the samefolder asthe application.The library databasefile holds
database
threedifferenttypesof tables- the library browsertable,the projectionbrowsertable,
and all the attribute datatablesassociatedwith the files availablethrough the library
browser. The library browsertablehandlesthe iTunes-likelibrary functionality
discussedin section4.4. The projectionbrowserstoresall the coordinatesystem
information ever loadedinto the program. In general,there will be as many of the third
type of tablesas there are recordsin the library browser. In the caseof shapefilesin the
library browsertable,for instance,the associated
tableis copieddirectly from the DBF
portion of the shapefile.Eachof thesetables,no matterwhat type is represented
by
eitherthe VBaseObjectclassor a subclasswhen loadedinto the program,. In orderto
give eachof theseclassesfunctionalityspecificto Mapalester,it was necessaryto
subclassnearlyall of the classesprovidedby Valentina. The VDataBasesubclassusedin
Mapalester,for example,is the appropriatelynaned LibraryVDatabase. The subclasses
of the VBaseObjectthat are usedhandle the two specialtablesin the LibraryVDatabase:
are the library browsertable (BrowserVBaseObject)and the projection browser table
2 Note: in late March, 2005,ParadigmaSoftwarereleasedValentina2.0, avery major
upgradeto the databaseframework that promises"incredible speedmultipliers"
(ParadigmaSoftware2005)over former versionsof Valentina. The currentversionof
but future versionswill.
Mapalesterdoesnot implementthis database,
Hecht

MapalesterResearchProject

Page37

(ProjectionVBaseObject). The tableslirked to the recoids in the BrowserVBaseObject
are acoessedusing the core VBaseObject.

Figure 3.54- A semrntic tr€twork ofthe drtrbsse clsssstructure rbove the VField level

Each field in eachofthe objectsof the VBaseObjecttype is derived from one of
Valentina'smany field classes.Eachof thesefreld classeshandlesa specifictyPeof
field; thereare classesfor Booleanfield types (VBoolean), date field types (VDate)' all
sortsof numberfield types (double,integer, long, etc.), and string freld types (Vstring).
More interestingly, Valentina also provides classesfor the blob (VBlob), object pointer
(VObjectPtr) and text datatypes (VText). The VBlob field allows Mapalesterto store
large chunksof data in the database.This is particularly important becauseMapalester
storesall of the spatial information for eachrecord in the BrowserVBaseObjectin a
VBlob field. Essentially,Mapalesterstoresall of the datain the ". shp" frle of a shapefile
MapalesterResearchProject

Page38

in this field. The VObjectPtrenablesthe object-relationalfunctionalityin Valentinaand
is usedin Mapalesterto link eachrecord in the BrowserVBaseObjecto the record in the
ProjectionVBaseObjectable that storesthe information relating to the coordinatesystem
is stored. Finally, the VText field is a
in which the recordin the BrowserVBaseObject
subclassof the VBlob field intendedspecificallyto storetext. A completeschemaof the
two specifictablesare found in figure 3.5bandc. The reasoningbehindthe inclusionof
is found in the descriptionof the library
eachof the freldsin the BrowserVBaseObject
canbe
functionalityin section4.6. Detailson the fields in the ProjectionVBaseObject
found in section3.4.

Name

Type
VLono

Size
(bvtes)

32
TableNumber
8t92
AbstractField
.Wext
LO24
VText
ContactlnfoField
64
GatherEndDateField VDate
64
GatherBeqinDateFieldVDate
RelevancyBeqinField
VDate
64
RelevancvEndField VDate
64
Wext
128
RestrictedField
Wext
128
LeqalField
Wext
8192
GeneralField
Wext
8192
EditionField
Wext
LO24
URLFieId
Wext
r024
KevwordsField
VStrins
LO24
NameField
8192
VTeXt
PublisherField
LOz4
VText
DataSourcesField
Wext
8192
DataGroupField
8192
VText
GenreField
L024
Wext
IDCodeField
VShort
16
ContentTvoeField
VBoolean
1
VectorRasterField
VShort
16
FileFormatField
variable
VBlob
SpatialDataField
VDateTime
tt2
DataAddedField
VStrino
256
FileNameField
VLonq
FileSizeField
32
32
RecordNumberField VLono
VDouble
64
minXField
VDouble
64
maxXField
VDouble
minYField
64
MapalesterResearchProject

Page39

maxYField

VDouble

64

oroiectionField

VObiectPtr

32

Figure 3.5b - The schemafor the BrowserVBaseObject.

Size
Name
PEStrinq
ProiectedCoordinates ystem
Projection
Geooraoh icCoordinateSvstem

Datum
AnqularUnit
LenothUnit

Type

(bvtes)

Wext

to24

VStrinq
VStrino
VStrinq
VStrino

100
100
100
100
100
100

Vstrinq
VStrinq

Figure 35c - The schemafor the ProjectionYBaseObject.

No schemafor the third type of tableis specifiedbecauseschemaswill vary greatly
dependingon the attributedatabaseof the GIS file being represented.However,the
schemasof this type of tableare currentlyrestrictedto fields incorporatedin the DBF file
format becausethe only type of attribute databasecurrently supportedis that of the
shapefile,which is in the DBF file format. The DBF file format only supportsfields of
the types "character" (interpretedas the VSting type), "numeric" (interpretedas the
Vlong type), "floating point binary numeric" (interpretedas the VDouble type), and
"logical" (interpretedasthe VBooleantype). As an example,the schemafor an attribute
databaseof a shapefilecontainingcountiesin the United Statesis given in figure 3.5c.

Name
Name
State Name
State FIPS
Cntv FIPS
FIPS
Area
Poo1990
Poo1999

Tvpe
VStrinq
VStrinq

VStrins
VStrinq
VStrinq
VDouble
VDouble
VDouble

MapalesterResearchProject

Size
(bvtes)

32
25
2
3
5
64
64
64

Figure 3,5d- An exampleschemafor the attrlbuaedatabss€ofa thaPelilecotrtafulngcountis in the
UnitedStstes.
Because the database system is quite intricate and difficult to explain out of its
programmatic context, figure 3.5fexplains what happens when a user adds a GIS file to
the library (see section 4.6) in a highly abstracted mamer.

18In

Figure 35f - The database cla88structure in action!

How doesthe user interact with the databaseclassstructure? In addition to the set
of classesfor storing databaseinformation, there is a lesselaborateset of classesfor
viewing and modiffing that information. This set of classesprovides the intersection
Hecht

MapalesterResearchProject

Page41

betweenthe databaseclassstructureand the interfaceclassstruch[e, and the remaining
portion of the sectionis dedicatedto its description.
Like the foundation of the databaseclassstructure,the databaseinterface class
structureis basedon a thid-party product. In this case,the product is DataGrid by
Einhuger Software,which is distributed in the form of a REALbasic plug-in. DataGrid is
a small set of REALbasic classesdesignedto provide programmerswith an easyway to
implement the visualization and modifrcation of Valentina databases3.
Due to the third-party natureof the databaseinterfacesystem's framework, the
databaseinterface classstructureis also heavily reliant upon subclassing.Primarily, the
three imporbnt classesin this structue axeall subclasses(either directly or indirectly
through anothersubclass)oflhe DataGrid class. Figure 3.5g showsthe classstructureof
the databaseinterfacesystemin more detail.

Figure 3.5g- The classstructure of Mspalcster's dstsbaseitrterfsce system.

3 My reasoningfor adoptinga third-party solution is identical to my reasoningfor
adoptingthe Valentina database:it would not havebeena good use ofmy GIS honors
project time to spendseveralweeksto recreatea Valentinadisplay outlet, probably with
worse resultsthat\n I could get with DataGrid.
Page42
MapalesterResearchProject
Hecht

The MapalesterDataGridclassprovidesall of the functionality sharedbetweenthe
LibraryBrowserDataGridand the hojectionTableViewer, which at the moment is about
90 percontofall the firnctionality in thesetwo classes.All of theseclassesinteract with
the LibraryVDatabaseclassthrough the useofSQL (structuredquery language)queries.
Thesequeriesreturn a classin Valentina for RealBasiccalled VCursor, which contains
all ofthe databas€infonnation relevantto the given query. In Mapalester'scurrent state,
most of the queriesthat af,econductedare simple'teturn all" from a specific table
queries. Sincethe classstructurecorrespondsdirectly with the table stuctue of the
LibraryVDatabase,whenevereachclassneedsto display data from the table to which it
'teturn all" query on that table. Figure 3.5h explains
corresponds,it simply performs a
this processgraphically.

Hecht

MapalesterResearchProject

Page43

Figure 3.5h- A graphicalview ofthe useof SQL as an interfacebetweenthe databaseand the
datebaseinterface classstructures.

As I implementmore functionalityinto Mapalester,thesequerieswill become
more complicated.For instance,the library will soonoffer a context-sensitivespatial
searchfeature. In other words, the library will be able to operatein a mode in which it
only showsdatarelevantto the specialextentbeingviewedin the selectedGISCanvas.
For example,if someoneis zoomed-into the Twin Cities metro area"the library will hide
files that only includeinformationaboutEuropeor Asia, etc. This will obviouslyrequire
greatercomplexityof searchqueries,possiblyrequiringme to implementa subsetof
spatialSQL via a C# plug-in to Mapalester.Similarly, asI implementsimpler,textbasedsearchesfor the LibraryDataGrid and the ProjectionDataGrid,much more
extensiveSQL queries(hiddento the userthroughan easy-to-useinterface)will be
necessary.

MapalesterResearchProject

Page44

4. The Designand lmplementation
of Mapalester's
FeatureSet
Supportof a varietyof file formats
A primary characteristicof availableGIS data is its extremely heterogeneous
nature. GIS datacome in a variety of file formats,and even data in the samefile format
GIS file formatscanbe looselydivided into two
canvary significantlyin representation.
groups,vectorand raster. This sectionwill focuson vectordata,as it is the most difficult
to implementandhasbeenthe focusof the Mapalester'sfile format supportthus far.
Additionally, it shouldbe notedthat the term "file format" is usedlooselyin this context,
as the specificationfor the currently dominantGIS vector data file format, Environmental
SystemsResearchInstitute's(ESzu)shapefile,describesthreeseparatefiles that makeup
eachshapefile.Moreover,sincethe shapefilespecificationwas publishedin 1998(ESRI.
1998),manynew GIS featureshavenecessitated
the additionof more files to the de facto
specification,resultingin situationsin which eachshapefilecan includesupwardof nine
individual files, eachsupportingits own specificsetof features.
Any GIS softwarepackagethat aims to be "easy to use" must make the user
completelyunawareof the complexityof GIS file formats. Ideally, a Mapalesteruser
shouldnot needto know what type of file format sheor he is using, or even if the file is a
vectoror rasterfile. I havemadesomeprogresstowardthis goal. As of this writing,
Mapalestersupportsthe shapefile,which, asmentionedabove,is the most commonfile
format for vectorGIS data. Mapalesteralsosupportsthe ".prj" expansionof the shapefile
specification.A ".prj" file containsthe metadatafor the coordinatesystemof the
correspondingshapefile,making".prj" files vital to the accuratedisplayof spatial
information. I have also madeprogresstoward supportingseveralother file formats,
includingthe formerly ubiquitousArcllnfo exchangeformat,or ".e00" file, and the upand-comingXMl-based file formats.However,I haveonly doneinitial researchinto
rasterfile format support.
In the first part ofthis section,I will explainissuescommonto supportingany
spatial data file format. In the secondpart, I will do the samefor vector data formats. I
Hecht

MapalesterResearchProject

Page45

will discussthe technicalissuesand techniquesinvolved with supportingshapefilesin the
third part. The fourth part will coversimilar issuesfor the ".prj" extension.

4.1.1 General IssuesRelated to File Format Support
In order to supporta spatial datafrle format, Mapalestermust be able to convert
datan the file format to Mapalester'sinternaldataformat. A consistentandpermanent
internal data format enablesme to easily add new data formats as the project progresses
and,later on, asthey becomenewly available.In otherwords,the internalstructure
enablesan architecturewith a type of abstractionsimilar to that of plug-in architectures
of programslike REALbasicandPhotoshop.Becausethereare few similaritiesbetween
of vectorandrasterdata,I havechosento give Mapalestera two-part
representations
internal representation,with onepart dealingwith vector information and the other
handling rasterdata. A diagram of the file format supportarchitecturecan be found in
figure4.I.Ia.

MapalesterResearchProject

Page 46

fufly *N

rb lorffi srFFort modrst

Figule 4.l.la - A generalizeddiagram of ilapaleste/s flle format 8uPport atchitecture.

As mentionedin the introduction, every spatialunit ofGIS data - vector or raster
- hastwo pads: spatial information and atFibute information. Mapalestermust
understandboth ofthese types of infonnation for both vector and rasterat two levels.
The higher of the two levels is the object-orientedstructurediscussedin preceding
sections. The lower of the levels is wordlevel representationstoredin memory or on
disk, dependingon the situation. In the currentimplementation,the word-level
representationis always in memory. However, I havebeencarefrrl to use only
algorithms and structuresthat work just aswell with data from a disk, or ftom a
combination of disk and memory. For now, given the relatively small sizesof the data
Hecht

Project
MapalesterResearch

Page47

setslikely to be usedby the target markets,disk-baseddata accessis not a huge concern.
More detailson disk andmemoryaccessof datacanbe found in the discussionof
indexing later in the paper.

4.1.2 General Issues Related to Vector File Format Support
Becauseshapefilesarethe dominantandmost coilrmonvector file format,I have
basedthe word-levelvectorinternalrepresentation
very closelyon the shapefile
specification. This appliesfor both spatial and attribute information. The similarity
betweenthe two representations
allows Mapalesterto very quickly convertshapefiles
into the internal representation,thus minimizingprocessorcost for the most commonof
suchnecessaryconversions.The shapefilespecificationwill be discussedin detail in the
subsequentsection. However, for now, it is important to note that the internal
representation
is an exactcopy of the shapefilespecification,with two major
modifications. First, while the shapefilespecificationrequiresa mixing andmatchingof
high and low byte order words in the spatial information portion, all words in the internal
representation
must be in the byte orderthat is nativeto the hostplatform. In other
wordsoin the Mac OS X version,all wordsmustby high-to-low,and in the Windows
version,all wordsmust be low-to-high. To leavethe byte orderin its original statewould
meanhaving to perform a bye order conversionevery time any data storedin a nonnativebyte orderis accessed,
significantlyslowingdown critical processes.Second,the
internalrepresentation
ignoresall shapeheadersand shapetype specificationsin spatial
information. This allows the useof thesebyes for otherpurposes,suchas linked list
addressinformation. All of the important information in the record headercan be stored
in the object-orientedhigh-levelrepresentation,
whereit is more convenientlyaccessed
by Mapalester.While the shapetype specificationsfound beforeevery shaperecordin a
shapefilearetheoreticallynecessary,
ESRI makesclearthat shapefilesshouldnot include
more than onetype of shape.(ESRI 1998). Seefigure 4.I.2a for a comparisonbetween
the shapefilerepresentationof the spatial information of a polyline and the representation
of the samedata in Mapalester'sintemal format. As of this writing, the internal
specificationfor attributeinformationis an exactcopy of the shapefile'sattribute
Hecht

MapalesterResearchProject

Page48

specification.This meansthat Mapalesterusesthe xllase file format for its internal
sectionon shapefilesfor more
attributioninformationstructure.Seethe subsequent
information.

Spatlal Inloimallon In a Shspeflls

Spsilal InformatlonIn Mapalealsr's
Inlamrl R€pt€aenallon

Figure4.1.2a- The left side of this diagramshowsthe internallayoutof the spatialpart of
a shapefile.The correspondingdiagramon the right demonstratesthe layoutof the spatial
part of the same sampleshapefilein Mapalester'sinternalspatialdata format. A much
moredetailedexplanationof this formatcan be found in the next part of this section.
Once the word-level configuration ofthe data matchesthat of the Mapalester
intemal specification, the secondlayer of file format support the object-oriented level takes over. While this level is describedin much more detail in the preceding sectionsof
the paper dedicatedto the object-orientedstructure of Mapalester,I will briefly discuss
here how Mapalester builds the objects basedon the word-level configuration. Because
the intemal specification holds with the shapefile's requirement that each file have only

Hecht

Project
MapalesterResearch

Page49

one tl,pe of shape,Mapalesterstartsbuilding objectsby creatingthe subclassof
VectorTheme(PolylineTheme,PointTheme,etc.) appropriateto the data in the file just
loaded. It then sweepsthroughthe word-levelspecification,addinga new objectof the
subclassof VectorObjectappropriateto the shapetype of the data for eachnew record
encountered.The constructorfor VectorObjectsrequiresa pointer to the start of the
spatial data and a pointer to the attribute data in the word-level specification, so as
Mapalestersweepsthroughthe new data,it providesthosepointers. Mapalesteralsoadds
the appropriatebounding box information to eachVectorObject.Finally, Mapalester
providesa linked list of the new Vectorobjectsto the new VectorTheme,which then
createsan RTreeindex of the new objects.

4.1.3ShapefileSupport
The shapefile(.shp)specificationwas developedandmadepublic by ESRI in
1998. The companycreatedthe format in responseto criticismsof the shapefile's
predecessor,the Arc/Info exchangefile format. The Arc/Info format is basedon a
topological frameworh which is rooted in an entirely different spatial school of thought
than that of the shapefile,which is strictly nontopologicalin nature. The topological
structurewill be discussedin a furure sectioncovering the Arcllnfo format, but for now,
all that is important is that the topological structureof spatial data storageis inherently
expensivein both storageand in processingspeedsof commontasks(ESRI 1998). As a
structurein which eachshapeis
result, in the shapefile,ESRI adopteda shape-based
comprisedof one or more vectorcoordinates(ESRI 1998). This structurehasmany
performanceand storagebenefits.
"Becauseshapefilesdo not have the processingoverheadof a topological
data struchrre,they have advantagesover other data sourcessuch as faster
drawing speedand edit ability...They alsotypically requirelessdisk space
and are easierto readandwrite." (ESzu 1998)
The shapefrlespecificationdescribesthreeseparatefiles for eachshapefile.The
first andmost importantfile is the ".shp" file, which containsall of the spatial
informationfor eachshapefile.To put it simply, the ".shp" file is what makesshapefiles
geographic.A shapefilecan describeinformationfor one of fourteentypesof shapesthat
Hecht

MapalesterResearchProject

Page50

rangefiom zero-dimensionalto three-dimensional.However, Mapalesteronly works
with four ofthe thtteen shapetypesfor the following threereasons:(l) Mapalesterdoes
not yet supportthree-dimensionaldata (2) only a portion ofthe one- and twodimensionalshapetypes areusedin practice,(3) and zero-dimensionalshapetypes are
neverused. It is the author's belief that restricting supportto the fow shapetypespoints, polylines, polygons, and multipoints - will result in very little if any functionality
loss for usersin Mapalester'stargetmarkets.A descriptionof the four supportedshape
typescanbe found in figures4.1.3a-d;thesearecritical to manyaspectsof Mapalester's
GIS capabilitiesdue to Mapalester'srelianceon the shapefilefor its internal
representationof spatial information.

Dst! Frcordt
l'

a
€'

a
Figure4.1.3a-Four spatialobjectsoftho POINTshap€type are shown above. Notethat
each polnt has its own data rgcold.

Ddr Recordr
a'

o
Flgure 4.1.3b- Two spatlal obiects ofthe MULTIPOINTthape tyPe are shovvnabove. Each
multlpoint lecord contains one or more point€. Multlpoinb are usefulwhen multlple
points have the samo atttibute information. For oxamPle,a flle of stores in a town could
be divlded Into multlpoint records, each of a certaln store type (laundry, rostaurant,
Curves,otc.)

MapalesterResearchProject

Page5l

DrbFrcon|l

Flgu.e 4.1.3c- Two spatlal objects oftfie POLYLINE3hapetype are shown above, Notea
polylng i3 not ths 6amo geometdc conoept as a llno, Each polylln€ 13made up of one or
morc llne segmenb. Also notlce tiat each polyllne can be made of on€ or more part6
(ESRI,1998). A part ls defln€d ai a serles of one or more lln€ tegm.nts (ESRI,1998).
Parts ars generally only d€fln€d rvhentyjo llne Bogment3erlct arc dlijolnt but must reter
to the same attrlbute record. A slngle polyllne can have mllllon3 of parts that all refar to
the same rocord In tfie attrlbute Informatlon database,although In Practlco polyllnes raroly
havs more than tw€nty or so pans, At fl]tt, many peoPlewonder why the concept of part6
la necossary. A good example of a multlplefarts polyllne record would be a flle of toll
roads on tho East Coast of tho Unlted Stateg.Toll roads often have no.toll sectlons, but a
good polyllne shapeflle of thg3e road3 would keop all the toll part3 of a tfi€ same road In
tho 3ame polyllne. A descrlptlon In ths ca3e of polygons can b€ found In the subsequ€nt
dlagram. Also, tako anoth€r look at flgur€ 4"12si lt should b€ easier to undorstand why
the structurg of tho shapoflle ls tho way that lt b now that polyllnes have b€en descrlbed.

MapalesterResearchProject

Page52

Figure4.1.3d- Three objects of the POLYGONtype are shown above. ESRIdescribes
shapefilepolygons as "one or more rings" (ESRI1998). The ring concept ls analogousto
the part concept in polylines. Notethat the two parts of Mlchigan are separaterings, but
are part of the same polygon record. The points In a polygon are etored in an order such
that if someonewere to walk along the lines connectingthe vertices,the interlor of the
polygon would be on her or his right. Interestingly,the spatial Informationfor a polygon is
stored identicallyto that of the polyline; the last vertex in each ring is simply assumedto
connectto the first vertex.

The secondfile, the ".dbf' file, is a databasefile that containsall of the atfibute
informationfor eachof the shapes.The ".dbf'file is in the standardxBaseformat,and
to a shapein the ".shp" file. Finally, the ".shx" file is
eachrecordin the file corresponds
an index of the ".shp" file. Eachrecordin the ".shx" file pointsto the beginningof a
recordin the ".shp" file. BecauseMapalesterdoesits own spatialindexing,the ".shx"
file is of limited use,althoughI haveincludedcodein Mapalesterto readandutilize this
file if the needarisesin later development. A diagramof how the spatial information is
split betweenthe threefiles of a shapefileis shownin figure 4.L.3e.

MapalesterResearchProject

Page53

3a!6nD

F4dord lor l{€lada

31b:l!

REaor{tlcr u/asnlrElon

t439?

P c y r p n | { 0 , o ,| ( 1 , - 1 } | ( 5 , 5 |) ( s , 5 |1 ( 1 , 5 1| O , 4

l5r"l't

RecDIdlqr i4|nnescia.

ReF.rdrtlon ol B|mry
Itstr h lh.'.!hf flb

204

3t 6S2

2la

3{|e

Rep..r.fltrton of BIr|| I

.rii+ ll

B4a,!rCl!r Wasfrr{lon

R.p.asrt|tlot| ot Bltury
Ilrtr ln the 'rltf

Itltr h [t.'.dbtr

flb

flb

erz/fl

lidr

| 8dr lrhr cn,

I l'soqm

5flnoi

Figure4.1,3e- Spatialobiectin a sampleshapefileand lts datadlstributionacrosstho
threerequiredflles in the shapefilespecification.
All threefiles arebinaryfiles. The word-levelayoutofthe ".shp" and ".slx" are
ESRI whitepaper.The ".dbf'format is a memberof the
describedin the aforementioned
xBasecomplex of files, whosestructureis modeledexactly off that of the dBASE format
designedby Ashton-Tate,and later continuedby Borland (Bachmann2000). The wordlevel structureof the xBaseformat is public and is widely available online tkough a
number of sources(Bachmann2000, others). In the C++ plug-in portion of Mapalester,I
havedevelopedrobustfile readersfor eachof two ofthesethreefiles (theDBF file reader
Hecht

MapalesterResearchProject

Page54

is currently under development,althougha REALbasic version of the readerhasbeen
implementedas a temporarymeasure). File writers are a trivial expansionof the reader
functionality.
Because,as mentionedabove,the internal data representationis very similar to
the shapefilespecification,the word-level transformationfrom shapefileto internal data
is quick and simple. The most difficult part of this transformationinvolvesthe
conversionfrom multiple byte-ordersto the byte order native to the platform. As
that is platform-specific.
discussedin previoussections,this is oneof the few processes
For Intel processors(Windows),all byte-ordersmust be switchedto little endian. For
IBM PowerPC (Mac OS X), all byte ordersmustbe switchedto big endian. For Mac OS
X versionof Mapalester,the threefiles mandatedby the shapefilespecificationmustbe
run through the byte order swapper. BecausexBase files are already little endiaruthe
Windowsversionmust only processthe .shxand .shpfiles.
Perfonning this switch upon the first openingof the shapefileis much less
expensivein processorcost over the long run than leaving the data in its original format
and switching the byte order on the fly over and over again. The pseudocodefor the brief
algorithmusedto swapbyte orderscanbe found in figure 4.1.3f. It must be appliedon
all files that needbyte orderconversion.
ptr-to-end-of-data\
(ptr-to-start-of-data,
functionMAKE-CORRECT-WORD-ORDER
ptr_to_start-of_data
is pointerto thefirstbyteof thedatiafile loadedinto
input:
memory.
ptr_to_end-of_data
is a pointerto thelastbyteof thedatafile loadedinto
memory

for each longjtr or doublejft in the shapefilespecificationbetween ptr_to_start-of-dataand
ptr_to_end_of_data
It is_Mac= true and specSayslslittleEndian (long_ptror double_ptr)= true then
SWAP-ENDIAN(/ongJotr,4) or SWAP-ENDIAN(doubIeJttr, 8l
if is_PC= true and specsayslsBigEndian((longjtr or doublejtrl = true then
4) or SWAP-ENDIAN(doubleitr,
SWAP-ENDIAN(long--ipfr,

MapalesterResearchProject

8)

Page55

Iength_to-swap)
DIAN(l?rstByfe,
f unction SWAP-EN
is theaddressof thefirstbyteof theseriesof bytesthatis to be
inputs:
firstByte
swaPPed
seriesof bytesthatis to be
is thelengthof thecontiguous
Length_to_swap
swaPPed
ptr= frrstByte
- 1
for i = 0 to length_to_swapl2
=
+
temp value_of(ptri)

is definedas increasing
thepointerby
// pointeraddition
in C++by usingchar
onebyte;thisis implemented
pointers
- i - 1')
vafue-of(pfr+ l) = value-of(ptr+ length-to-swap
- i- 1l = 1s110
value-of(ptr+ length_to_swap

return
algorithmusedto
for the MAKE-CORRECT-WORD-ORDER
Figure4.1.3j- Pseudocode
byteorders.
orders.
convertbyte
convert
MAKE-CORRECT-WORD-ORDERis a fast algorithm;it is O(n) if n is consideredto be
the numberof byte serieswhereconversionis necessary.If we considerthe numberof
bytesto be swappedas n, the algorithmis only O(tlz)l The algorithmis fast in practice
in a
aswell. It convertsmillions of four-byte(long) and eight-byte(double)sequences
negligibleamountof time that is barelynoticeableto the user,evenon the Mac OS X
platform on which more conversionsmust be performedbecausethe majority of datain
the shapefileis storedin the little endianbyte order. Only on abnormallylarge shapefrles
on the Mac OS X platform doesMAKE-CORRECT-WORD-ORDERtakemore than one
second.This is not a problem,however,asMAKE-CORRECT-WORD-ORDERwill
only be performedonce for every shapefileloadedinto Mapalesterthanksto the database
structuredescribedin previoussectionsofthe paper.

4.1.4Supportfor The " .Prj" Extension
The ".prj" extensionof the shapefilespecificationincludescritical metadata
describingthe coordinatesysteminformation for the shapefilewith the samenonextensionnamein the samefolder. In order to supportthe ".prj" extension,Mapalester
must be able to convertthe datain ".prj" files to Mapalester'sobject-orientedprojection
enginedescribedin previousportionsof this paper.
Hecht

MapalesterResearchProject

Page56

Unlike the ".shp," ".shx," and".dbf'files of the shapefilespecification,the ".prj"
file is a text file. Becauseof the high variability of text encodingsand REAlbasic's
built-in ability to handlesuchencodings,the parserfor the ".prj" file is programmedin
REALbasiccode. (The projectionengineitself, asmentionedabove,will soonbe
convertedinto C+r.) While text files in REALbasicmay be easierto readand write due
to the lack of binary dataproblemsdescribedabove,the parserof the ".prj" files involves
muchmore computersciencethan the ".shx", ".shp," and *.dbf'readers. Before
discussingthe detailsof the parser,however,it is first necessaryto describethe structure
of a standard".prj" file.
The ".prj" file, dueto the metadatait describes,exhibitsa much more complicated
files. While the *.shx", ".shp", and ".dbf' files
structurethanthat of the aforementioned
can be describedwith a simple linear definition of bytes and what they represent,the
".prj" file describesinherentlyhierarchicalinformation,andmust thus havea more
convolutedstructure.Similar to the specificationof many programminglanguages,the
".prj" specificationis basedaroundan EBNF (extendedBachus-Naurform) grammar
(ESRI,2000). Figure4.I.4adepictsthis definitionusing a very slightly modified syntax
of pureBNF. Terminalsymbolsaredepictedin bold.
<PRJ_FILE>
::=<PROJ_CS>
I <GEO_CS>
<PROJ_CS>
lT>l
::= PROJCS[<NAME>,<GEO_CS>,<PROJECTION>,<PARAMETER>,<UN
<UNIT>l
<GEO_CS>
::=GEOCSI<NAME>,<DATUM>,<PRIMEM>,
<DATUM>
::=DATU
M[<NAME>,<SPHEROID>l
<SPHERIOD>::= SPHEROID[<NAME>,<DlGlT>,<OlGlT>l
<DlGlT>l
<PRIMEM>
::= PRIMEMI<NAME>,
<NAME>"= "<ALPHA>"
<PROJECTION>
::= PROJECTIONI<NAME>I
<ALPHA>II PARAMETERI<NAME>,
<PARAMETER>
::= € | PARAMETERI<NAME>,
<ALPHA>1,<PARAMETER>
<ALPHA>I
<UNIT>::= UNIT[<NAME>,
<ALPHA>::= any characterexcept quotes I any characterexcept quotes <ALPHA>
<DlGlT>::=<TERM_DlGlT>
I <TERM_DlGlT><DlGlT>
< T E R M _ D I G:I:T=O
> l1 l2l 3 l4 | 5l 6l 7l 8l 91.

MapalesterResearchProject

Page57

Figure4.1.4a- The slightly extendedBNF for the ".prj" file specification. Based on ESRI's
".prj" specification(ESRI2000).
Becauseof the similarity between the ".prj" file specification and that of
programming languages,Mapalester's ".pq" file reader uses techniques similar to those
used in programminglanguage compilers. The reader first "tokenizes" the text from the
".prj" file using a discrete finite automata derived (DFA) from the one in figure 4.1.4b.

PIGIDIUIS

Figure4.1.4b- The above discretefinite automatais implementedin the REALbasic".prj"
file parser. Noticethat the right bracket and comma charactersare the only true token
delimiters.
The program then applies the grammar described in the EBNF in figure 4.I.4ato
organize all of the information in the tokens. This organization has the end result of

MapalesterResearchProject

having an instance of the ProjCS class, which is described earlier in the pape\ with all of
the necessaryparameters to understand the coordinate system in the ".prj" file. An
example of an inputted string from a ".prj" file and the resulting ProjCS class instance
can be found in figure 4.1.4c.

PROJCSfNAD-1983_UTM_Zone_l5N',GEOGCSf'GCS-North-American-l983',DATUMt'D
_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]I,PRIMEM['Gre
enwich',0.0l,UNlT['Degree-,0.0171532925199433]I,PROJECTION['Transverse_Mercator"],
PARAMETER["False_Eastrng',500000.0l,PARAMETERI"False-Northing',0.0],PARAMETER
Latitude_Of
["Central_Meridian",93.0],PARAtnETERI"Scale_Factor",0.9996J,PARAMETERf'
_Ori gi n',0.01,UNlT[ "Meter",1.0]l

has_a

I
f--'*'*_-l
,rW*
|---7--\-

has-a
nrnc ='Felsa_Easfif
velra = i0mo00.o

t-

doulh
tr'

I

|
\

\

|I

t_____)_)_/ '-/
nrnF .'cdtrNl-Mcddlfll"
v|lr! = .t$.o

namc='sc8lr-Faclol'
ftrJa ! 0.9996

Ir,o/a
(r

)

oouu*
oouu*
II
||
||L---l-_-J
--------l-

I q378137.0|

f

\=
has_aI

equats
equals
t
?98.25722101
|
|

dqrbtc
I
lfuottsetrnnorenwtatl
€quals

I
+
lE:--]
29,8.257?22101
I

MapalesterResearchProject

|

Page59

Figure4.1.4c- Thefigureabovels the resultlngclassstructuregenerated
fromthe ".prl"
file containingtextabovethe figure.
It is interestingto note the similarity betweenthe classstructureof the projection system
and the categoriesin the BNF gmrnmar. As mentionedin precedingsections,the class
structurefor the projection engineis basedon the natureof the data that the class
structurerepresents,and the ".prj" grammarvery well representsthe nature of the data it
structures.This meansthat one could learnaboutprojectionmathematicsvia the
grammarand someonewho understandsprojection mathematicswould understandthe
grarnmarimmediately. For example,a spheroidcanbe definedby the major axis andthe
flattening,both of which arerepresented
in the BNF. The detailsof projection
mathematicsarebeyondthe scopeofthis section,so I will not discussthem further. See
sections3.4 and4.6 for more information.

4.2 SpatialIndexing
In any GIS softrvarepackage,a searchthrough spatially referenceddata for a
particularspatiallocationis an extremelycommontask. For instance,any time a user
pansor zoomsin an instanceof Mapalester'sGISCanvas(section3.3), Mapalestermust
searchthrough all of the data layers in the GISCanvasto identi$ which objectsto draw
in the canvasand which fall outsideof the canvas'sextent. While it may be trivial to
searchthrough a small numberof spatial objects,GIS softwareoften must scanthrough
thousandsor millions of spatialobjectsin orderto find all objectsthat fall within a
specifiedzone. As such,the issueof how to mostefficiently performthesesearches
usedin
arises. This sectionis dedicatedto severalspatialindexingapproaches
with a differenttechniquefor performingthese
Mapalester,eachof which corresponds
searches.Eachpart ofthis sectiondescribesa different indexingapproachand discusses
the time and storagecostsof the approach.At the time of this writing, most of the
developmentefforts arein this portion of the program.

MapalesterResearchProject

Page60

4.2.1 The Brute Force Approach
The positives and negativesof the brute force approachare easyto describe. The
biggestadvantageis that it is extremelyeasyto implement. It alsocanbe somewhat
storage/memoryefficient, dependingon the specificsof the implementation.The sole,but
important, drawbackis that it is very slow comparedto other approaches,at least in
theory. The brute force approachto spatial indexing is simple: there is no index. When a
spatial searchis performed,the searchalgorithm must simply go through all of the
availableandrelevantspatialobjects,checkingeachobjectto seeif it falls within the
spatialparametersof the search.Obviously,this is an O(n) process.When n is small,
this is not a problem, but when n is, sayna million or more - a cornmonhappenstancein
the world of GIS - slowdownsoccur.
The brute force approachwas the frst spatial indexing methodusedin
Mapalester. It was implementedas a temporarymeasure,as somesort of spatial search
methodis a necessarystepping-stone
to many otherGIS processes.Surprisingly,
however,performancewas satisfactoryfor all but the largestdatasetsin the collectionof
samplevectordatasetsdesignedto echothe setof datasetslikely to be usedby my target
markets.
I believethis gapbetweenthe theoreticalslownessandthe relative speedin real
world testsis explainedby my extensiveuseof the effective"boundingbox" heuristicin
the implementationof the brute force method.The bounding box of a spatial object is
defined by the maximum and minimum coordinatefor eachdimensionof the object. In
the contextof the current,2D-only versionof Mapalester,this meansthat the bounding
box is the rectangledefinedby the minimum x-coordinate,maximum x-coordinate,
minimum y-coordinate,andmaximumy-coordinate.Seefigure 4.2.Lafor an illustration.

MapalesterResearchProject

Page61

{Grzl

(1t,0l
Flgure4.2.1a- Theboundlngbox of a samplsspatlalobJect.Notethat the box can
be definedby the upperleft and lowerrlghtvertices.Ths x-coorClnate
of the uppsrleft
vertexls the minlmumx-coordlnateof the spatlalobjsci. They-coordinateb the
maximumy-coordinateof the Bpatialobject. Forthe lowerlight vertex,the x-coordlnatels
definedby ihe maxlmumx.coordlnateofthe obloctandthe y-coordlnateis deflnedby the
mlnlmumy+oordlnateot the obJect.
For all of the spatialindexing approaches,the bounding box is usedas an
approximationfor spatialobjectswhen running the searchalgorithm. While this heuristic
canresultin falsepositives,asdepictedin figure4.2.1b,it will nevercauseany lalse
negatlves.

Hecht

MapalesterResearchProject

Page62

Figuro4.2.1b- Despitethe fact that the rectangleareaof searchovorlapswlth the
boundingbox oftho spathl objectfromflguro4.2.1a,the areaof aearchdoesnot actuatly
ovsrlapwith the spatlalobjectltsef. ThesPatlalobJectwill be roturnedas a matchtor the
search,but lt wlll bEa falsopositlve.
The false positives are a small price to pay consideringthe massivereduction in
calculationsper shapethat results. Ifthe boundingbox were not used,all of the search
algorithrns,no matter to which indexing approachthey correspond,would have to usea
polygon intersectiontest algorithm in the caseof polygonal and polylinear spatial objects'
Each iteration of this algorithm would be O(4p) (O'Rourke 2002), where p is the number
of points in the polygon or polyline and assumingthe searchareais always a rectangle
(with four vertices).This would makethe searchalgorithm associatedwith the brute
force indexing approachO(4pn) in the caseofpolygon and polyline datasets, where p is
the maximum numberofvertices of the polygonVpolylinesin the datasetand n is the
number ofpolygons/polylines in the dataset.Even tlte faster searchalgorithms associated
with the other spatial indexing approaches,in which n is replacedwith smaller functions
of n, would stall extensivelyunder sucha heavy computationload. It is interesting to note
that the boundingbox heuristic, due to its optimistic nature,is quite similar to the
admissibleheuristic for heuristic searchalgorithms like A*.
Most likely, it is the impressivereduction in calculationsper n that causesthe
brute force searchalgorithm to perform so well againstits competitors for all but the
Hecht

MapalesterResearchProject

Page63

largestdatasets.Essentially,the numberof calculationsnecessaryto checkif a
rectangularareaof searchoverlapswith a boundingbox is so few that it takeshundreds
of thousandsof suchcomparisonsin order for the time taken to be noticeable. Figure
versionof the very simplealgorithmneededto perform the
4.2.Ic is a psuedocode
comparison.
function OVERLAP?(rect1, rect2) returns Boolean

inputs:

rectl is the searchrectangle
rect2 is the boundingbox ofthe spatialobjectbeingqueried

if maxX(rect1\ < minX(rect 2)
return false
if minX(rectl) > maxX(rec9)
return false
if maxY(rectl) < minY(rec2)
return false
if minY(rectl) > maxY(rec0)
return false
return true
Figure4.2.1c- Thealgorithmto determineif two rectangles(in this case,the search
rectangleandthe boundingbox of a spatialobject)overlap.Thisalgorithmis so simplein
in singletwo-lineInlinefunctionin the C++
theoryand In practicethat it is lmplemented
plug-inportionof Mapalester.

4.2.2TheR-TreeApproach
In orderto provide goodperformancefor the key low-level functionalitythat is
spatial searchingfor all file sizes,it was necessaryto abandonthe brute force approach
and researchother approachesto spatial indexing for futtre implementationin
Mapalester.The seminalpaperby Guttman(1984)forms the foundationof most spatial
indexing researchstill done today. In this paper,Gutffnandefinesa constructhe calls the
"R-tree." While there have beenmany proposedimprovementsto the R-tree in recent
years,I decidedthat Guttman's constructwould be a good place to start and implemented
Hecht

MapalesterResearchProject

Page64

R-treeindexing. Becausethe R-treedealswith the spatialobjectsthat makeup data
layers(below the VectorThemelevel, seesection3.3), and becauseR-treesrequirethe
extensiveuseof recursivealgorithms,all R-treeprogrammingwas done in the C+r
language.
The basicideaof the R-freeis simple. The treeis comprisedof threedistinct
objects:non-leafnodes,leafnodes,and spatialobjects. Every object in the tee hasa
boundingbox identicalto thosedescribedin the precedingsection. Every objectin the
tree'sboundingbox is containedwithin the boundingbox of its parent. Additionally,
Guttman(1984)identifiessix moretechnicaland specificpropertiesof the R-treeas
follows (adaptedto fit context):

(1) Every leaf node containsbetweenm and M spatialobjectsunlessit is
the root, where m is the minimum number of entriesper node, M is the
maximum numberof enffiesper node,and m is greaterthan or equal to
one half of M.
(2) Every spatialobject has a boundingbox that is the smallestrectangle
that spatiallycontainsthe object.
(3) Every nonleaf nodehasbetweenm andM entriesunlessit is the root
(4) Every non-leaf node and leaf-nodehas a bounding box that is the
smallestsuchbox that containsall of the children of the non-leafnode
or leafnode.
(5) The root hasat leasttwo childrenunlessit is a leaf.
(6) All leavesappearon the samelevel.

All of the algorithmsusedto operateon the R-hee are designedto maintain and
query a tree that conforms exactly to the aforementionedspecific and broad requirements.
Obviously,sincethe R-treeis designedto makespatialsearchesmore efficient,the most
important of suchalgorithms is the searchalgorithm. This algorithm happensto be the
simplestof all the algorithms connectedwith the R-tree. In short, the algorithm scans
recursively through the tree startingwith the root and returns all the spatial objectswithin

MapalesterResearchProject

Page65

the bounding box input into the search algorithm. The algorithm is described in more
detail in the following psuedocode:

function SEARCH(bounding_box)
returns list of spatialobjects
inputs:

bounding_box
is the inputof the spatialsearch
SEARCH-REC(root,
bounding_box,list)
return /lst

function SEARCH-REC(node,
bounding_box,
list)
inputs:

bounding_box
is the inputof the spatialsearch
node is the node to be examinedin this spatialsearch
/isfis the "global"listto whichall positiveresultswill be added
for each child in node
if overlaps(bounding_box, getBoundingBoxOf(chlld))= true then
= falsethen
lf isLeafNode(child)
SEARCH-REC(ch
ild, bounding_box\
else
append(/lst,child)
end lf

Figure4.2.2a-TheR-treesearchalgorithm
While the R-treeworks beautifullyandquickly evenon polygon andpolyline
files, the massivenumberof objectsto insertin the R-treewith evena small point file
quickly overloadsthe R-freecapabilities.Point entriesare loadedinto R-treeby making
their boundingboxesdegenerate
rectangleswhoseextentis a singlepoint. While polygon
and polyline files may havemorepoints total due to the massivenumberof verticesfor
manypolygonsandpolylines,they generallyhavelessthan 10,000or so polygonsor
polylines,which is the level at which boundingboxesare established,and thusthe level
at which the R-tee indexes.As mentionedabove,the R-tree is a data sffucturewhose
processes
get increasinglymore expensivetime-wiseas more and more items are
Hecht

MapalesterResearchProject

Page66

inserted. As a result, in preliminary tests,the R-tree was up to twenty times slower than
the bruteforce approachfor a point file with around165,000points. It is not uncommon
for point files to have that many points or more.
As such,it wasnecessaryto find a way to reducethe numberof boundingboxes
to accomplishthis goal, all of
indexedfor point datasets.I attemptedthreeapproaches
which eitherhad little impacton the numberof boundingboxesindexedor made
boundingboxesthat were so largethat they eliminatedmost of the benefitsof using the
R-treeto beginwith. The frst approachsimply groupedfrpoints that were adjacently
storedin the points file. For all valuesof fr tested,the resultingboundingboxeswere
eithertoo largeor the insertalgorithmwas too slow, or both. Obviously,I neededa more
intelligentapproach.I next lookedinto point clusteringalgorithmsin an effort to more
accuratelygroupthe pointsandthusminimize boundingbox rectangles.The most
coflrmontype of clusteringalgorithmis the k-meansalgorithm,but this algorithmis
O(n') in the worst case. While it is often muchbetterin practice,it would involve
rururingthrough all of the points at leastseveraltimes and comparing eachpoint with the
numberof clustersdesired. Suchan algorithmwould take more time than it takesto
insertthe points individually. As such,I implementeda standardvarianton the k-means
algorithm, often referredto as the one-passk-meansalgorithm. The algorithm, modified
for the contextof Mapalester,is depictedin pseudocodein figure 4.2.2b.
returnslistof clusters
c/usters)
functionONE-PASS-K-MEANS(points,
epsilon,
poinfsis thesetof pointsto cluster
inputs:
epsilon
is themaximum
a pointcanbefromthegeometric
meanof a
distance
cluster
(implemented
c/usters
is anarrayof clusters
as MultipointObjects),
initially
empty
for eachp in points
= false
foundCluster
for each c in c/usfers
p\ < epsilon
lf disfance(geometricMeanO\c),
addPointToClustedc,p)
adjustMeanOEluste(c)
foundCluster= true

MapalesterResearchProject

Page67

= false
if foundCluster
cl= makeNewClustefl\
addPointToCluste(c,p)
adjustMeanOfCIuster(c)
cl)
addToAnay(c,
implementation
Figure4.2.2b-A psuedocode
of a one-passk-meansalgorithm.
In the worst case- when no point is within epsilonof anotherpoint- this algorithmis
O(n'), a significantimprovementover the basick-meansalgorithm. Additionally, the
worst caseis very unlikely to occurif epsilonis chosenwisely. Note, however,that this
algorithmhasmuch lessaccuracythanthe basick-meansalgorithm aspoints are not
reassignedas the geometricmeansshift. However, becausethis algorithm walks the line
betweenspeedand accuracyvery well, it wasworth trying in Mapalester.Unfortunately,
despitea largenumberof tests,I wasunableto find a context-sensitivequationfor
epsilonthat would not eithercausethe nearworst-caseperformanceto occur (andthus
alsonot reducethe numberof boundingboxesto index) or that would not generate
boundingboxesthat were so largethat therewas almostno point in using spatial
indexing. The final approachto clusteringthat I attemptedwas to combinethe first two
approaches
into my own algorithm. This algorithm'spsuedocodeappearsin figure
4.2.2c.
functionSLOPPY-K-MEANS(pornfs,
c/usters)
returnslistof clusters
epsilon,
polnfsis the set of pointsto cluster
epsilonis the maximumdistancea pointcan be fromthe geometricmeanof a
cluster
initiallyempty
c/ustersis an arrayof clusters(implemented
as MultipointObjects),
cl = makeNewClusteo
for each p in pornts
p) < epsilon
lf distance(geometricMeanO(c),
addPointToClu ster(c, p)
adjustMeanOfCIu ster(c)
foundCluster= true

Hecht

MapalesterResearchProject

Page68

cl= makeNewClustefl)
addPointToClusfe(c,p)
adjustMeanOfCIu ster(c)
addToAnafic, cl)

returnclusters
Figure4.2.2c- A synthesisof thetrivialand intelligentone-passpointclustering
algorithms.
Unfortunately,for all logical epsilonvaluesattempted,this algorithmresultedin far too
many clusters,which meantthat the numberof boundingboxeswas too great to have
much of an impacton the index insertiontime. While I havenot given up on the
combinationof the R-tree with the point clusteringapproach,I have switchedmy
attentionto the implementationof the R*-tree,which claimsto handlepoints much more
efficiently thanthe basicR-tree. The R*-tee seemsto be the most popular2D-focused
derivativeof the R-tree(Manolopoulouset. aL,2003),so I am hopefulthat it will provide
goodresults.

4.3 Line Simplification
Line simplificationalgorithmsarea portion of the computationalanswerto the
age-oldart of generalizationin cartography. Early cartographershad to determinethe
level of detailin polylines(both thosethat standon their own and thosethat arepartsof
polygons)basedon the scaleof the map they weregenerating.For example,mapsof the
entire United Statesgenerallydo not needthe detail of every tiny nook and cranny of the
easterncoastline.The idea behindline simplificationalgorithmsis to automatethis
processfor the hugeincreasesin availablespatialdata. In their book Generalizationin
Dieital Cartoeraphy,McMasterand Shea(1992)describeline generalizationalgorithms
with the following definition: "As a generaldefinition, simplificationalgorithmsweed
from the line redundantor unnecessarycoordinatepairs basedon somegeometric
criterion,suchas distancebetweenpointsor displacementfrom a centerline."(McMaster
and Shea 1992).
Hecht

MapalesterResearchProject

Page69

McMasterand Sheaidentifr four main benefitsof line simplification in digital
cartography:(l) reducedplotting time for (now antiquated)digital plotters,(2) reduced
storagespace,(3) fastervectorto rasterconversiorqand (4) fastervectorprocessingfor
operationssuchas translation,rotation,andrescaling.However,in my research,I have
found that, in the time sinceMcMasterand Sheawrote their book, processingspeeds
haveincreasedenoughto nulliff most of the benefitsof simplification. In fact, in my
experience,many of the algorithmspresentedin their book add computationcostsand
resultin slowerdisplayanddataprocessingspeeds.As a result,Mapalesterimplements
only the most trivial of line simplificationalgorithms. The fust part of this section
identifiesthe resultsof multiple implementationsof the classicDouglas-Peucker
algorithm. The secondpart describesthe ftivial algorithmactuallyusedin Mapalester.
Finally, the sectioncloseswith a descriptionof the possibilities that lie with an enhanced
versionof the Douglas-Peucker
line simplificationpresentedby Hershbergerand
Snoeyink.
algorithms,however,
Beforediscussingthe efhcacyof variousline-generalization
algorithmsfor
it is importantto discussa recentlydiscovereduseof line-generalization
which an accuratelygeneralizedline, and not speedof algorithm, is the most important
factor. This use- reducingthe sizeof extremelydetailedvectordatalayersto a digital
capacitythat is distributable,say,on the Internet- is an extremelyhigh-levelfunction,
howeverand may not evenmakethe first versionof Mapalester.The most famous
applicationof this useof line generalizationhasbeenthe productionof reasonablysized
U.S. censusboundaryfiles from the TIGER database(U.S. Census2004).

4.3.1 Douglas-Peucker
One of the hallmarksof early GIS softwareand one of the most famous
line simplification
algorithmsin computationalcartographyis the Douglas-Peucker
algorithm. I initially assumedthat an implementationof the algorithm would be a
necessaryelementof Mapalester.Additionally, early implementationsof Mapalester
suffered from slow graphicsdisplay speeds,a problem that presumablywould be solved
by having lessdetail to display,which is the resultof line simplificationalgorithms. I
Hecht

MapalesterResearchProject

Page70

initially implemented a recursive version of the algorithm, described by the pseudocode
in figure 4.3.Ia,which is adapted from Sunday (2002). Figure 4.3.1b shows the effect of
Douglas-Peucker on a sample line.

Iine\returns generalizedline
function BEGIN-SIMPLIFY(folerance,
tolerancefor the algorithm,whichin the caseof
toleranceis the approximation
is measuredin pixels
the Mapalesterimplementation,

inputs:

llne is the line to be generalizedand containsa list of all of the pointsin the line.
lastVertexln(/lne))
DP-SfMPLfFY(tolerance,/rne,firstVertexln(/rne),
for each veftexln line
= truethen
If isMarked(vertex)
add(veftex,newLine)
end if
next
return newLine
(tolerance,line,a, b)
function DP-SIMPLIFY
ifa=bthen
return
end if
lineAB= getSegmentOfLine(/rne,
a, b/
for each veftexin lineAB
if distanceFrom(ve rtex,IineAB) > maxDi stanceSoFar
= vertex
maxVertexSoFar
From(vertex, IineABl
maxDi stanceSoFar= distiance
end if
next
> tolerancethen
it maxDistanceSoFar
DP-SIMPLIFY(tolerance,Iine, a, maxVertexSoFar)
b)
DP-SIMPlIFY(tolerance,Iine, maxVerlexSoFar,
end if
Figure4.3.1a- High-levelpsuedocodefor the Douglas-Peuckeralgorithm.

MapalesterResearchProject

PageTl

Prc.Slmplilflcaflon

Poat€knpll[catlon

on an examplepolylinewith four vertices.
Figure4.3.1b- Theresultof Douglas-Peucker
While simpleand short,this algorithmhassurprisinglyhigh processorcosts. The step
that requiresthe most computationis illustratedby the distanceFromfunction in the
psuedocode.To determinethe distanceof a point from a line, it is necessaryto use
vectorarithmetic,which slowsthe algorithmsignificantly. In additiorqthe distanceFrom
calculationmust be performedn2times in the worst case,wheren is the numberof
verticesin the input polyline. (The algorithmis O(n*m), wheren is the numberof
verticesin the input polyline andm is the numberof verticesin the outputpolyline. The
caseis that in which no simplificationoccursdueto all vertex distances
aforementioned
exceedingthe tolerance.)Moreover,for a largedatalayer,this algorithmmust be
performedon thousands,or eventensof thousands,of polylines.
into consideration,it
Taking the computationalrequirementsof Douglas-Peucker
is no surprisethat the time costsof performing the algorithm outweighedthe
computationalbenefitsof simplification,at leastin the contextof datadisplay. The
performanceof the algorithmis highly dependenton the tolerancevaluethat is chosen.
However,for all tolerancevaluesthat resultedin reasonablyaccuratedisplay,the
algorithmaddedtime to the datadisplayprocess.
In an effort to decreasethe computationalcostsof the algorithm, I implemented
an iterativeversionof the algorithm. To do this, I employedstandardtechniquesusedto
convert tail-recursive algorithms like Douglas-Peucker.However, eventhe iterative
version proved more costly in the context of datadisplay than no generalizationat all.

MapalesterResearchProject

Page72

4.3.2 The Trivial Approach
Due to the failure of Douglas-Peuckerto speedup data display and severalother
operations,Iinsteadimplementeda trivial line simplificationapproachwhenever
simplificationwasneededfor speedreasons.For instance,in the caseof datadisplay,the
most expensiveoperationis the actual drawing of pixels. As such,my tivial
simplificationdatadisplayalgorithmis as follows:
PLIFY(ltne)
functionTRIVIAL-SlM
inputs:
/ineis thelineto begeneralized
andcontains
a listof allof thepointsin theline.
lastPoint= firstVertexl
n(line)
for eachveftexln line
Foint= getAppropriatePlotPoint(/rne)
then
if pointdoes not equal/asfPolnf
poi
drawLine(/astPoint,nt)
end lf
lastpoint= point
next
Figure4.3.2a- The trivial line simplificationalgorithm implementedin Mapalester.

4.3.3 TheHershbergerlSnoeyinkSpeed-Up
In 1994,Hershbergerand Snoeyinkproposedan improvementon the classic
Douglas-Pueckeralgorithm that improvesthe worst caseperformancefrom O(n2)to
exceptit replacesthe
O(n*log(n)). The algorithmis identicalto Douglas-Puecker
distancecalculationstepidentifiedaboveas a key performanceissuein Douglas-Puecker
with a more advancedmethodof distancecalculationthat usesconvexhulls. The
implementationcost of this speed-upis much higher and Hershbergerand Snoeyink
themselvesadmit that "the statisticalpropertiesof cartographicdata usually meansthat
the straight-forwardimplementationis slightly fasterthan the convex hull
implementation."(Hershberger,1994)While Hershbergerand Snoeyinkclaim that their
simplifrcationalgorithm"may be interesting"for parallelor interactiveapplications,none

MapalesterResearchProject

Page73

of theseapplicationscurently exist in Mapalester.As such,no attemptto implementthe
speed-upin Mapalesterwill be madein the nearfuture.

4.4 iTunes-IikeDatabaseFunctionality
Throughmy teachingassistantwork, I determineda major weaknessof existingGIS
softwareto be its relianceon WindowsExplorerasthe dominantdatafile organization
framework. The useris expectedto more or lessmaintaina systemof foldersand files
that organizesher or his data. There are two main problemswith this frameworlg
however. First, especiallyin a lab context,it is easyfor this systemto be invalidatedby a
carelessor creativeuser. Second,the usermay misscertainsimilaritiesandpatternsin
someof her or his datasetsthat could be identifiedby a more intelligentdatafile
organtzationsystem. As a result, I set out to developa new systemof data file
organization.Utilizing similar methodologyto the mannerin which I developedthe
GlSFormatWindow- identiffing what hasworkedin otherprogramsand modiffing it
for my purposes- I singledout two possiblemodelsfor providing the userwith the best
possibledatafile management
features.
The first of thesemodelswas found in photo managementsoftware,the secondin
musicjukebox software. How do photo andmusic files relateto GIS datafiles? The
answerto this questionlies in the fact that photo,music,and GIS files all carry a large
amountof metadata. Whereasa photo may have the capturedate,the capturelocation,
andthe resolution;anda music file may havethe artist,album,and genre;a GIS file has
the data author, field descriptions,legal restrictions,edition, data group, and a great
number of other metadatafields. I was not pleasedwith how existing photo management
softwareallows its usersto navigatethrough the metadataof photo files, primarily
becauseusersof photo managementsoftwareplacea much highervalue on previewsof
the dataalongwith displayof attributedatathan do GIS users. While previewsare a
satisfactorysupplementalfeature,they neednot be a core elementof GIS datafile
management.Music jukebox sofhvareapplications,therefore,provide the better model
for GIS data. Out of a field of severalexcellentcasestudies,I identifiedthe wildly
popular iTunes softwaremadeby Apple as having what I believe to be the best supportof
Hecht

MapalesterResearchProject

Page74

metadata.I madethisjudgmentfor two reasons.First, iTunesby default loadsmusic
files into a cental databasewhen they are fust opened,and doesnot require original files
after that point. This freesthe user from having to use Windows Explorer or the Mac OS
X Finder to organizedata"andassuresthat the user's only interaction with music files is
through the iTunes metadatabrowser,not through location on the hard drive. In other
words,the userneverneedsto know wheresheor he storeda music file, just, for
example,who singsthe song. Second,I believeiTunesstrikesa good balancebetween
simplicity of interfaceand datamanagementpower. Primarily through a combinationof
the useof the "playlist" and "library" concepts,iTunesprovidesrelatively quick accessto
music files while still supportingstringentorganizationand searchingfor music by
metadatafields.
Mapalester'sGIS datafile managementsystemis heavily influencedby that in
iTunes. An additionalbenefitto the adoptionof iTunes' systemis that usersfamiliar
with iTuneswill feel right at homein Mapalester. The basisfor the GIS file
managementsystemis complete;userscanview and edit metadataof loadedGIS files,
for example.The metadatafields supportedin the library featurewere determined
through the study of a sampleof GIS file metadataand through consultationwith
the fields, the
ProfessorCarol Gersmehl.While it is very easyto add/delete/modifu
fields are likely stayas they are for the first release(seesection3.4 for more details).
Supportfor searchingand data"playlists" will be simple to implement and will be in
the first releasedversion.

4.5 Prime Meridian Conversion or,

GIS that Acts Like a Globe, Not a

Mep"
A significant amountof developmentime hasbeendedicatedto implementing a
featurethat allows usersto interact with Mapalesteras they would with a globe, replacing
the map-basedinteractivityfound in currentGIS software. More specifically,this
feature,which is nicknamed"GISpin," enablesusersto interactwith the world as a
continuoussurface;userspanningextentswill neverencounteran "edge" of the world, so
to speak. A key resultof GISpin is that Mapalesterwill not requirethe world to be
"split" at a certainmeridian. This "split" is very familiar to map viewers,and hasbeen
Hecht

MapalesterResearchProject

Page75

identified in personalinterviews with teachersas a meansof marginalizing the portrayal
of certain areasof the world. For instance,most rnapsmadein the United Statessplit the
globe at the meridian that runs betweenAlaska and the easternreachesof Russia. This
createsthe impressionthat geographicprocessesare not continuousacrossthe split
meridian. Given that one of Mapalester'stargetmarketsis the educationmarket,it is
importantfor Mapalesterto avoid supportingthis impression.
GISpin is not yet complete,but will appearin the final version of Mapalester.
Implementationof the featurehasbeenan interestingmix of projection and datum
mathematicsand computersciencetechniques.This sectionis dedicatedto describing
thesetechniques.Becauseof the natureof spatialdata,implementationof this featureis
essentiallycomprisedof two very differentcomponents.The first component,which has
beencompletedbut not yet incorporatedinto the Mapalesterinterface, involves
implementingthe functionality for point datalayers. The second,and more difficult,
doesthe samefor polyline andpolygondatalayers.

4.5.1Point Supportin GISpin
In principle,supportingpoints in "GISpin" is quite simple. Thereare many
technical, detail-orientedimplementationdifficulties surroundingthe incorporation of
point GISpin into the projectionsystem,but theseare outsidethe scopeof this paper. As
such,the simpletheorywill be the only elementof the point supportdiscussed.
Similarly, I will limit the discussionto datain'lrnprojected" or "geographic"coordinate
systems,becausethesesystemsusecornmonlyknown angularunits like longitudeand
latitude. It is important to note, however,that the sametechniquescan be adaptedto
projectedcoordinatesystems,with onemajor differencediscussedat the end of this
subsection.
In their native form, unprojectedcoordinateshave a latitude and longitude relative to
the equatorand a given prime meridian,respectively.While the equatoris definedasthe
intersectionbetweenplane x and the surfaceof the earth where x is perpendicularto the
line segmentthat containsboth poles (non-magnetic)and intersectsthis line at its
midpoint, the prime meridian is an arbitrary construct. In fact, the currently predominate
Hecht

MapalesterResearchProject

Page76

prime meridian * the meridian that passesthrough Greenwich,England- was not agreed
upon as the default prime meridian until the InternationalMeridian Conferencein 1884,
and certainotherprime meridiansare still usedon occasion.
It is this arbitrary natureof the prime meridian from which GISpin derivesits power.
Statedsimply, GISpin makesthe prime meridian the centerof the current view extentand
adjuststhe longitudinal coordinateof eachpoint accordingly. In this way, if the current
view extentcenteris in easternRussi4 aroundt79.5" Eastlongitudeusing the Greenwich
meridian,Mapalesteris ableto easilyprojectthepointsin, say,Alaska,on the right of the
180oline, accuratelyrepresentingwherethey exist in the real world. Mapalesterdoes
this by establishingthe 0o line asthe 179.5' Eastline, and adjustingall otherpoints
accordingly. In currentGIS software,thesepointswould appearon the oppositesideof
the possibleview extent,just as in a world map.
It is importantto considerthe issuesinvolved in transferringthis methodologyto
projectedcoordinatesystems.The most importantof theseissuesinvolvesthe infinite
distortion inherentto the periphery of the rangeof many projection equations. For
instance,in the standardMercator projectiorLthe southand north poles are projectedto
infrnity. While this particularcaseis not problematicto GISpin becausethe latitudinal
display restriction can be maintainedwhile rotating longitudes,the corresponding
drawbackin transverseMercator (which can be describedas Mercator flipped on it side),
is highly problematic. Left unchecked,this problemcould resultin usersscrolling
through infinitely extendedextentsat the periphery of the rangeof the projection
equation. This problem has an interestingsolution, which hasthe convenientside effect
of helpingto eliminatemuch of the confusionsurroundingprojectionsfor new users.
Essentially,Mapalestersimply changesthe centralmeridianof the projectionequationto
the centerof the view frame. In the caseof equationswith trvo central meridians,
Mapalesterusesthe meridiansthat divide the view frameinto threeequalparts. This
methodologyhasthe effect of reprojectingall pointsin the view frameto maximizethe
benefitsof the chosenprojection, averting a commonand hard+o-catchproblem for new
GIS users. Interestingly,if this methodologyis extended,it would be very easyto
implementan auto-projectionsystemin Mapalesterthat would choosethe bestprojection
for any given view frame. However, sucha systemwould require a large amountof
Hecht

MapalesterResearchProject

Page77

human-computerinteractionresearchor the constructionof an expert systemin order to
determinethe bestprojection for every categoryand scaleof view frame extent.
Nonetheless,
it would provide an interestingavenuefor graduateschoolresearch.

4.5.2Polylineand PolygonSupportin GISpin
The conceptsbehindpolyline andpolygon supportin GISpin areidenticalto that
for points. After all, polylinesandpolygonsarenothing but a seriesof orderedpoints
that are connectedwith lines. However, the mannerin which computersconstructand fill
polylinesand connecthe points in polylines,createsan enonnousroad block to
implementingsupportfor thesegeomefficforms in GISpin. This problemappearsonly
when the view extent is large enoughthat a polyline or polygon that appearson the right
sideof the view frame alsoappearson the left sideof the frame. For instance,sucha
situationwould occurif the view frameis themaximumpossiblewhile using GISpinthe whole world - and the centerof the frame is aligned suchthat the United Statesis cut
off on the right side. In thesesituations,whenMapalestertries to draw a line segment
from the last vertex on the right side to the first vertex on the left side (or vice versa),
insteadof drawing a line to the edgeof the view frame on the right side and beginning
again on the left, Mapalesterjust draws a line all the way acrossthe view frame.
Obviously, althoughthe context for this bug is somewhatuncolnmon,the bug is still a
major showstopper.
After attemptingmany tivial and complicatedworkarounds,I determinedthe
solutionto this bug to lie in one of the severaline andpolygon "spliffing" algorithms
available. Suchalgorithmswill generatethe setof polylinesor polygonscreatedby the
bisectionof a polyline or polygonby a line. Mapalesterwould draw the polylinesand
polygons output by this algorithm insteadof the original polylines and polygons
describedin the data layer. Unfortunately, thesealgorithms have high implementation
costs,especiallywhen speedis suchan enonnousfactor. As such,I havenot yet been
successfulimplementingthesealgorithmsand,asa result,Mapalesterstill usesa mapbasedview frame.

MapalesterResearchProject

Page78

OnceI havecompletedthe implementationof thesepolyline and polygon
bisectionalgorithms,they will haveuseswell outsideGISpin. For example,as
mentionedabove,a small number of data setscomein geographiccoordinatesystems
that incorporatea prime meridian other than the Greenwichmeridian. In order to convert
suchdata setsto display correctly in a dataframe with any other prime meridian, I will
needto usethe algorithms to reconfigurethe original coordinatesof suchdata sets.
Additionally, the algorithm implementationswill come in handy when I am
implementing such standardGIS featuresas layer intersectionsand clipping.

4.6 Projection C onversion F unctions
While I have discussedthe structureand function of the coordinatesystemstructure
in Mapalesterin previoussections,I haveyet to explainin detail the actualprocessof
projectionconversion.This processis conceptuallysimplerthanthe structureof the
coordinatesystem,but just as complicatedto implement. Projectionconversionfunctions
canbe separatedinto two broadcategories,thosethat "project" and'hnproject." Each
map projection hasone of each.The functions that "project", often referred to as
"forward direction" projection functions,take two angular-unit inputs (the longitude and
latitude, often abbreviatedas ?,,and Q,respectively)and return two length unit outputs
(Cartesiancoordinatesusuallyin meters,often abbreviatedas x and y, respectively).The
functionsthat *unproject,"often called"reversedirection" projectionfunctions,take
length coordinatesas inputs and return angularunits as outputs. The functions,
regardlessof direction,often take otherparametersas well. Commonsupplementary
parametersinclude the central meridian, latitude of origin, and standardparallels.
Projection conversionfunctions can also be categorizedbasedon whether or not they
dealwith the Earth as a sphericalor ellipsoidalobject. Thosethat view the Earth asa
spheroidare only usedin very small-scalemaps. The vastmajority of commonly-used
projectionconversionfunctionsarethoseof the ellipsoidalpersuasion.
WhencompletedMapalesterwill supportthe setof projectionconversionfunctions
found in table4.6a.The boldedfunctionsare thosethat arealreadycompleted.The table
is basedon the equivalentablefor ESRI's AToGIS9. Sincedatais sometimes
Hecht

MapalesterResearchProject

Page79

distributedin obscureprojections,I havemadesupportingthe widestpossiblecollection
of projection conversionfunctions a high priority. A user not being able to input a
certaindatasetbecausethe datasetis projectedin an unsupportedprojectionviolates
both the ease-of-use
andpowerful developmentgoals.

NAME
Aitoff
Albers EoualArea Conic

Behrmann
Bonne

DIRECTION
both
both
both

both

SHAPE
sphere
ellipsoid

sohere

Cassini
Craster Parabolic
CylindricalEqual Area
Double Stereoqraphic

both
both
both
both

ellipsoid
ellipsoid
elliosoid
ellipsoid
ellipsoid

EckertI - VI

both

sphere

EouidistantConic
EouidistantCvlindrical
Flat Polar Quartic
Gall Stereoqraphic

Gauss-Kruqer
Gnomonic

both
both
both
both
both
both

elliosoid
sohere
sohere
sphere
ellipsoid

Hammer-Aitoff

both

HotineTwo Point

both
both
both
both
both
both
both
both
both
both

Hotine Azimuth

Krovak
Lambert Azimuthal EqualArea
Lambert Conformal Conic
Loximuthal

Mercator
MillerCvlindrical
Mollweide
New ZealandMap Grid
Orthoqraohic
PlateCarree
Polyconic
Quartic-Authalic
Robinson
Sinusoidal
Stereoqraohic
StereooraphicNorth Pole
StereoqraohicSouth Pole
Times

Transverse Mercator
Two-Point Equidistant

Van der GrintenI

sohere
sphere
elliosoid
elliosoid
ellipsoid
ellipsoid
ellipsoid

sohere
elliosoid
sphere

shoere

both

ellipsoid
sphere

both
both

elliosoid

both

sphere

both
both
both
both
both
both
both
both
both

ellipsoid
ellipsoid
ellipsoid

MapalesterResearchProject

sohere

ellipsoid

ellipsoid

sohere
elliosoid
sohere

sphere
Page80

Veftical near-side perspective
WinkelI
WinkelII
WinkelTrioel

both

sohere

both
both
both

sDhere
sohere
sohere

Figure 4.6a - Table of supported projections. Bold projections are finished.

Fortunately,I have setup the structureof the coordinatesystemengine in sucha
way that addingnew projectionconversionfunctionsis relatively easy. All that is
requiredis to essentiallygive the new projectiona narne,enterthe function into the code,
and optimizethe function.Projectionconversionfunctionsarenothing more than
formulas. As such,I simply programmaticallyencodetheseformulas in REALbasic or
C+r code(The final versionwill only useC** codeas all the datathat needsto be
projectedexistsat a level below that of the map layer,andthusmust be codedin C++
plug-in format. Seesection3.3 for more details). My main sourcefor the formulashas
beenthe seminalmap projection book Map Projections- A Working Manual by John
Snyderof the USGS. An exampleof a formula from the book and its REALbasiccode
equivalentcanbe found in figure 4.6b.

TransverseMercator Forward Projection ConversionFormula for Spheroids:
SynderFormula
x-k,NfA+(l-T+ c)A3t6+(5-18r +Tz +72c +56e'2)Astlzo)
y = k"{M - M"+ Nt^nOIAz
12+(5 -T +9c + 4cz)

MapalesterResearchProject

Page8l

e ' 2= e 2 ( l - e z )

N=al

r- e2sinzq)

T -tartz Q
C = e'2cos'4
A = ()r- d)cosf
o2
?o4
M= a f ( t - i - A - 5e6 - ,)o-(+.#.

256

(,r5ea
'256

+
ffi+ ..)sin2f

45e6- . . .
- (.35e6
+ . . .) s l n b @
+ . . .I
)sln4@
'3012

tOU

k": the scaleon the cenaalmeridian. This is a constantand is input into the formula. For the UTM
projection,this equal0.9996,so this is the value alwaysin Mapalester.
e: the eccenfiicityof the ellipsoid. This is defuredby the datumof the GeoCSclassof the sameProjCS
class.
a: the semi-majoraxis of the ellipsoid.This is definedby the datumof the GeoCSclassof the same
ProjCSclass.
Mo: "M calculatedfor $o,the latitudecrossingthe centralmeridianI, at the origin of the x,y
coordinates."(Snyder 1987) The cenfial meridianis alsoan input into the projectionformula. For UTM
uses,this is the centerof the given UTM zone.

TransverseMercator Forward Projection ConversionFormula for Spheroids:
REALbasic Code Derived from Synder Formula
// pre-calculate all the stuffyou can
* myUnit.conversionFactor
dim falseEas double: params.valud"False_Easting")
* myUnit.conversionFactor
:
params.value("False_Northing")
falseN
dim
asdouble
* myGeoCs.myUnit.conversionFactor
dim lam0 as double: params.value("Central_Meridian")
:
dim k0 asdouble params.value("Scale_Factor")
dim phi0 as double: params.value("Latitude_OlOrigin")* myGeoCs.myUnit.conversionFactor
+ 3*4/32 +
dim Mo asdouble: 6* ((l-e2/4 - 3*e4164- 5*e6/256)*phi0-(3*e2l8
45*e6/1024)*sin(2*phi0)+(15*e4/256+ 45*e6/1024)*sin(4tphi0)- (35*e613072)*sin(6*phi0))
dim terml as double: (l-e2/4 - 3*e/.164- 5*e6D56)
dim term2 as double: 13*e2l8+ 3*e4/32+ 45re6/1024)
dim term3 as double: (15*e4256 + 45*e6/1024)
dim term4 as double: (35*e6/30j2\
dimN, T, C, bigA, Mp asdouble
dim cosY, tanY as double
dim boundas integer: uBound(m)
dim tempBoundas integer
dim ij as integer

Hecht

MapalesterResearchProject

Page82

for i: I to bound
tempBound= uBound(m(i).x)
forj:ltotempBound
m(i).projxO : m(i).projX(i) * myGeoCs.myUnit.conversionFactor
m(i).projYO : m(i).projYO * myGeoCs.myUnit.conversionFactor
cosY : cos(m(i).projYfi))
tanY : tan(m(i).projY(i))
// hondle special cases
if m(i).projX(i) - lam0 >= nDiv2 then
m(i).projXO : nDiv2 - SMALLEST-NUMBER + lamo
elseif m(i).projxO - lam0 <: -nDiv2 then
m(i).projX(f):'nDiv2 + SMALLEST-NUMBER + lam0
end if
if m(i).projY(i) < rDiv2 andm(i).projYO > -nDiv2 then
N : a/sqrt(l-e2r(sin(m(i).projYc)))"2)
T: tanY^2
C = eprimesq*cosY^2
bigA = (m(i).projx[) - lam0)*cosY
Mp = a * (term1*m(i).projYfi )-term2* sin(2* m(i).projYf )_
+ term3*sin(4*m(i).projY(i))- term4*sin(6*m(i).projYO))
m(i).projx0 = k0 r N t ( bigA + (l - T + C)*(bigA^3y6+ (5 - I 8'r T + T^2 + 72*c +
20)
58*eprimesq)*(bigA^5)/l
m(i).projYo:k0*(Mp-Mo+1q*s6fr(big{"2)/2+(5-T+9*c+4*c"2)*(big|^4)124+(6158*T + T^2 +600*C - 330*eprimesq)*(bigA^6)/720))
+ falseE
m(i).projxO : m(i).projx(i) *myUnit.conversionFactor
m(i).projYO : m(i).projYO*myUnit.conversionFactor+ falseN
else
Mp = a * ((l-e2/4 - 3* e4164- 5* e61256)+m(i).projY(D_
(3* e2/ 8 + 3* e4I32 + 45* e6/| 024)*sin(2* m(i).projY(i)_
- (35*e6/3072)*sin(6*m(i).projY())
+ 05re41256+ 45*e611024)*sin(4*m(i).projY(i))
m(i).projX$:0
m(i).projYO: k0*(Mp - Mo)
+ falseE
m(i).projxO : m(i).projX(i)*myUnit.conversionFactor
+ falseN
m(i).projY(i) : m(i).projY(i)*myUnit.conversionFactor
end if
next
next

Figure 4.6b- The TransverseMercator Forward Equation for Spheroids,and the corresponding
REALbasic code in Mapalester. Note that the formula doesnot take into considerstion false easting
and northings,but the codedoes,for the purposesof support for the UTM coordinatesystems.

Note that the layout of the formula in REALbasic differs somewhatfrom that
presentedby Snyder. Becausethesefunctions,in the caseof a largepolygon file, for
speedof operationis an essential
instance,are run on millions of points in sequence,
Page83
MapalesterResearchProject
Hecht

in keepingwith the "speedis harder
considerationwhile programming.Consequently,
than function" experienceof this softwareengineeringproject getting the projection
function working correctlyusuallyis lessdifficult than gettingthe projectionfunction
working at its maximum possibleefficiency. One approachthat I often usedto speedup
the function was to pre-calculateall of the constantsfor the projection of any given map
layer prior to projectingall the vectorobjectsin that map layer. The main goal is to take
asmuch out of the iterativeloop aspossible. In non-jargonterms,the goal is to only
calculateoncethe portionsof the formulathat needto be calculatedonly once. The
projectionfunctions,aspresentedby Synder,frequentlycalculatetheseportionsof the
formula with eachpoint conversion.
One especiallydifficult aspectof projectionfunctionprogrammingis the handling
of the specialcasecoordinateinput. Many of the projectionconversionfunctionsmake
heavy useof trigonometric functions that have specialor undefinedvalueswith certain
inputs. For example,the tan functionusedin figure 4.6b meansthat Mapalestermust
handlethe caseswhen the input angularvaluesareeithernl2 or -n/2. Itl do not, the
entire function will fail. In this case,I have chosento make any input that is nl2 or -+/2
the closestnumberpossibleto that valueby addingor subtractingthe smallestnumber
recognizableby a standard32-bitpersonalcomputer(0.000000000000001).

4.7 A Small Subset of Other Planned Features
The featuresand functionality identified in the previousparts of sectionfour of
are only a subsetof the featuresand functionality that have beencurrently developedand
are an even smaller subsetof the featuresthat will appearin the final version of
Mapalester. Moreover, the featuresand functionality identified aboveare in large part
aimed at the "powerful" developmentgoal identified in the introduction. In this final
part, I will describea seriesof featuresand functionalitythat will appearin the final
versionof Mapalester,but for which I havedonelittle implementationwork thus far. I
will alsopay carefulattentionto identiffing the reasonsbehindincluding thesefeatures
the context of the target marketsand developmentgoals identified in the introduction.

MapalesterResearchProject

Page84

4.7.1 Incorporation of the National Map Application Programming Interface

(APr)
One of the largestchallengesto developinga free GIS softwareprogram is to find
datato distribute with the program. Even with the limited amount of free data available,
thereareall sortsof datadistributionissues.In orderto fully meetmy developmentgoals
of producing a free (goal four) and powerful (goal one) GIS software application, it is
essentialthat I providea substantialamountof free datawith the GIS. The easiestway to
provide that datais to implementthe National Map API. I discoveredthe National Map
API during a presentationby the United StatesGeologicSurvey(USGS)on its National
Map web depositoryof spatialdata lmplementationof the NationalMap API will allow
Mapalesterusersaccessto all datainsidethe NationalMap from within Mapalester's
interface;to the user,the datamay as well resideon the user's hard drive. The datain the
National Map rangesfrom geologicalto hydrological to demographicto transportationto
administrative.

4.7.2 Providing Easy Access to Census Data
For the samereasonthat I havechosento implementthe NationalMap API,I
havealsomademakingU.S. censusdataeasilyavailablea high priority feature. It has
beenmy experienceas a GIS teachingassistant,and my perceptionfrom the GIS
applicationsliterature,that someof the desirabledatafor non-profit andK-12 education
GIS applicationsare U.S. censusdata. My goal for Mapalesteris to makeaccessing
censusdataas easyils possible. The ideais that usersshouldneverhaveto visit the U.S.
censuswebsiteitself; they shouldbe ableto get all the censusdatathey needfrom within
Mapalester's interface.

4.7.3 Data File-Sharing Using the Gnutella Network
In order to make evenmore free dataavailableto Mapalesterusers,I hope to
implement a version of the Gnutella network within Mapalester. Through the network,
Mapalesteruserswould be able to sharethe datasetsthat they createwith other users
aroundthe world. For instance,I would be ableto sharethe point shapefilesof Christian
Hecht

MapalesterResearchProject

Page85

contemporarymusic eoncertlocationsthat I createdfrom primary sourcesfor a recent
researchproject on the geographyof Christiancontemporarymusic,as well as the point
shapefilesof Bruce SpringsteenconcertlocationsI createdfor fun. Similarly, studentsin
a middle schoolscienceclasscould shareGPSpointsthat they collectedalongwith
associatedattribute data.

4.7 .4 Internationalization
As I have prograrnmedMapalester,I have beencareful to lay down the
frameworkto makeit aseasyaspossibleto produceversionsof Mapalesterin languages
otherthanEnglish. I havedonethis by makingheavyuseof constantsinsteadof directly
programmingEnglish languagephrasesinto the sourc€code. (A constantis essentiallya
variable that can changeits value basedon the languageof the operatingsystemon which
Mapalesteris rururing.)This will allow me to sendsomeonea spreadsheetof all the
words and phrasesthat I needtranslated,havethem translatethat spreadsheet,and
directly input the translatedphrasesinto Mapalester.In otherwords,onceI finish the
Englishversionof Mapalester,all I will needis a tanslator for any given languageto
make a version of Mapalesterfor that language. Hillegass(2002) suggeststhat software
with an internationalaudiencebe translatedinto at leastEnglish,French,Spanish,
German,Dutch,Italian, and Japanese.I alsohopeto produceversionsin Mandarin,
Cantonese,
Taiwanese,Russian,and Serbian.
development
Supportfor multiple languagescertainlybolstersthe ease-of-use
goal and all of its benefitsto Mapalester'stargetmarkets. In additioruthe distributionof
Mapalesterin multiple languageswill not only benefitMapalester'stargetmarkets,but it
will alsogrow themarkets. Whereasthe Englishversionof Mapalestercan only appeal
to the three target marketsin English-speakingcountries,supportfor other languageswill
make Mapalesteraccessibleto the target marketsin other counffies.

MapalesterResearchProject

Page86

Figure 4.7.4s- A screenshotof the REALb&sic constantsinterface showsbow simPleit is to add new
languages
to Mrpsle$ter. Ifthe operotingsystemonwhich Mapalesteris loadedisitrSpanishmode'
Mapelesterwill dirplay "Edici6n" insteadof "Edition" in the Librsry lnfo Brows€r window.

5.1Gonclusion
After nine monthsof attemptinga projectso challengingin both scaleand
amountofpride.
difficulty, I feel that I canconcludethis paperwith a reasonable
Granted,I did not meetthe project'soriginalgoalof releasinga productby this time'
However,I believeI havemademore thansatisfactoryprogresstowardsdoing so given
alongthe way. I feel
I haveencountered
the greatnumberofunexpectedchallenges
confidentthat theprojectis in a statewhereit canbe finishedin a moderatelysmall
amountof time. In addition,presentingthe softwareanddiscussingit with membersof
aboutthe unmetneedsofthe
the targetmarkethaveled me to believethat my hypotheses
Hecht

Project
MapalesterResearch

Page87

targetmarketsare true. I alreadyhavea small number of people eagerly awaiting the
finishedproduct.
On an individual level, the diversearrayof knowledgeand skills I gainedduring
this projectwill proveusefulas I continuemy careerin GlScience. I know understand
the conceptsbehindcoordinatesystemswell beyondthe functionalknowledgeI had
before. I canwrite codein C++. 1 understanddatabasesystemsand SQL. I know the
shapefileformat andthe reasonsbehindESRI definingthis way. My knowledgeof DFLs
and BNFs, learnedin the most theoreticalof computerscienceclasses,cameinto
practicaluse. I am now familiar with the tials andtravailsof computersoftware
engineering,notjust computerscience.The list goeson. This projecthasbeena grand
adventureinto both of my majors and hasbeena fitting and synthesizingfinale to my
bifocal collegecareer.
I furd myself at this juncture very excited aboutthe possibility of other students
headingdown the samepath. I believe that my progressin an attempt to recreatea very
expensivepackageof commercialsoftwareis evidencethat, with a coupleof
modifications,a similar effort in the futurecould be successfulin the time allottedfor this
project. This is a significantstatementas I am essentiallyarguingthat studentswith a
computersciencebackgroundhavethe empowerrnentpotential of producing free and
powerful software for groupswith needsleft unmet by the commercial market. In the
subsequentfew paragraphs,I will identiff and explicatethe aforementionedchangesthat
I think will makesimilar projectsmore "profitable" in the future. Theseparagraphscan
also be readas funding recommendationsfor Keck grantsand other surnmerfunding
My strongestrecommendationfor engagingin a project like my own is to make
surethat there is more than one studentworking on the project. If the project is of the
samescaleasMapalester,two studentsshouldbe sufficient,providedthey are willing to
put in the time and effort necessary.With two studentson the job, a softwareproject like
Mapalesterwould probably make it more than twice as far, as collaborative computer
scienceprojects tend to get past frustrating and work-stopping momentsbetter than solo
projects.
The secondrecommendationis to make surethat there is at least a semi-expertin
the theoriesand techniquesnecessaryfor makingthe software,not just usingthe
Hecht

MapalesterResearchProject

Page88

software. In my case,I was expectingto makeit pastthe programmingof the basicsof
GIS much fasterthan I di4 and then rely on Dr. Laura Smith for her knowledge of spatial
statisticsto implementhigher-levelGIS functions. Ideally, it would havebeenhelpful to
alsohavea professorproficient in the computerscienceelementsof basicGlScienceto
get me through the fiouble spots.
Finally, studentswho wish to engagein similar projectsshould,if possible,enroll
in at leastan intro softwareengineeringcourseat oneof the ACTC schools. I had
somethingsimilar to this courseduring my time at UC SanDiego, andI found elements
of it to be very helpful. I am surefurther educationon the engineeringaspectsof
computersciencewould haveprovidedevenmoreinsight into how to approachthe
problemof a massiveprogrammingproject.

5.2 Acknowledgernents
I would like to thankthe following peoplefor their help on my project Dr. Laura
Smith,for her advisingon both a professionalandpersonalevel; JovanaTrkulja" Paul
Singh, and Cole Akeson, for keepingme sanethroughoutmy exciting, productive, and at
times frustrating summeron the Keck Grant; the Keck-Bigelow Foundation,for funding
much of my research;andProfessorCarol Gersmehl,for providing me the GIS skills and
passionnecessaryto engagea project like Mapalester.

6.1 Bibliography
Bachmann,Erik. XbaseFile FormatDescription.2000Available from
(last accessedll27 2W5).
http://www.pgts.com.au/download/public/xbase.hrn
Bachorski,Andy, Andy Fuchs,Bill Mounce,Brian Blood, andet. at.2003. VALENTINA
DatabaseKernel. ParadigmaSoftware,.
VALENTINAfoTREALbasicReference.ParadigmaSoftware, .
VALENTINASOL.ParadigmaSoftware,.
VALENTINAfoTREALbasicTutoriaL ParadigmaSoftware, .
Hecht

MapalesterResearchProject

Page89

Baker,ThomasR., and SarahW. Bednarz.2004.Irssons Learnedfrom Reviewing
Researchin GIS Education.Journal of Geography102:231.
Beckmann,Norbert,Hans-PeterKriegel, Ralf Schneider,and BerhardSeeger.1990.The
R*-Tree: An Efficient and RobustAccessMethodfor Pointsandrectangles.SIGMOD
Conferencel:322.
Brandt,Dave. 2004.REALbasicLanguageReference.Austin, TX: REAL Software,In.c.
Brandt,David. 2004.REALbasicUser'sGuide.Austin, TX: REAL Software,Inc.
CMAP. CMAP CaseStudy:Robin Hood Foundation.Available from
(last accessed
3l3l 2005).
http://www.cmap.nypirg.org/case-studies/CS2/default.asp
Dalrymple,Jim. 2005.Apple desktopmarketshareon the rise; will the Mac mini, iPod
help?MacCentral.
Departmentof Defense.1984.World GeodeticSystem1984: Its Definition and
Number,NIMA TR8350.2.
Relationshipswith Local GeodeticSysfens.Report
Elwood, Saratr.2002.GIS usein communityplanning:a multidimensionalanalysisof
empowerment.
ESRI. 20C0.HowTo: Createprojectionmetadata(.prj) files for shapefiles.Redlands,
CA: ESRI, ReportNumber,1,{056.
1998.ESRI ShapefileTechnicalDescription:An ESRI White Paper.
- - *ArcGIS 8: SupportedCoordiwte Systenns
and GeographicTransformations.
Redlands,
CA: ESRI,.
Estier,Theodore.About BNF Notation.In Universityof Geneva[databaseonline].
Availablefrom http://cui.unige.ctr/db(last accessedll3l 2005).
research/Enseignement/analyseinfo/AboutBNF.html
Gewin, Virginia. 2004.MappingOpportunities.Nature427:376.
Guttman,Antonin. 1984.R-Trees:A DynamicIndex Structurefor SpatialSearching.
SIGMOD Conferencel:47 .
Hecht,Brent. 2ffi4. ClassifyingGISPolylineData UsingNeural Networks.
- - -2004. Mapalester,Empowerment,and Ra.dicalDemocratic Citizenship.
Hecht,Brent, andBen Johson.2003.Final Projectfor CS325- Compilers:A Compiler
for Cabal.
Hecht

MapalesterResearchProject

Page90

Hershberger,John,andJackSnoeyink.1992.An O(n*log(n)) Implementationof the
Algorithm for Line Simplification.Proceedingsof the SthInternational
Douglas-Peucker
Symposiumon SpatialData Handling l:134.
Hillegass,Aaron. 2N2. CocoaProgrammingforMac OSX. Boston,MA: Addison
Wesley.
Keohane,GeorgiaL., and CMAP. CMAP CaseStudy:Civic Builders.Available from
(last accessed
3/31 2005).
http://www.cmap.nypirg.org/case_studies/CSl/default.asp
Kerski, Joseph,1.2004. Analyzingthe EarthWith GeographicInformationSystems.
National SpeleologicalSocieryNews.
Leeser,Miriam. Variantson the K-MeansAlgorithm. 1999Available from
(last accessed
http://www.ece.neu.edu/groups/rpUprojects/kmeans/variants.html
1/10/20052005).
McGrew,J. C., andCharlesB. Monroe.2000.An Introductionto StatisticalProblem
Solvingin Geograpfty.United Statesof America:McGraw-Hill.
McMaster,Robert8., andK. S. Shea.1992.Generalizptionin Digital Cartography.
Washington,D.C.: Associationof AmericanGeographers.
Mikalajunas,Peter.1998.DBF File Structure.
Neuburg,Matt. 2@1. REALhasic:TheDefinitiveGuide.Sebastopol,CA: O'Reilly.
O'Rourke,Joseph.1998.ComputationalGeometryinC. Cambridge,UK: Cambridge
University Press.
REAL Software.REALbasicvs. Java.In REAL Software,Inc.[databaseonline].
(last accessen
3/31
Available from http://www.realsoftware.com/realbasic/compare/javal

200s).
Russell,Stuart,andPeterNorvig. 200.3.Artificial Intelligence:A ModernApproach.
Upper SaddleRiver, NJ: hentice Hall.
Snyder,JohnP. 1987.Map Projections- AWorking Manual. Washington,D.C.: United
StatesGovernmentPrintingOffice.
Office. 1998.WisconsinMappingBulletin.ReportNumber,24.
StateCartographer's
Sunday,Dan. Polyline Simplification.2@2 Availablefrom
(last
http://geometryalgorithms.com/Archive/algorithm_0205/algorithm_D2O5.htm
6/01 2004).
accessed
Hecht

MapalesterResearchProject

Page9l

Availablefrom http://www.rtreeportal.org/
Theodoridis,Yannis.R-tree-Portal.112612005
(last accessed
9ll5 2N4).
U.S. CensusBureauGeographyDivision, CartographicOperationsBranch.Scale,
Generalization,
andLimitations of the CartographicBoundaryFiles. In U.S. Census
2004Available from http://www.census.gov/geo/www/cob/scale.html
online].
[database
(last accesse
d 3| 25120052005).
United StatesGeologicalSurvey.2003.ImplementationPlanfor TheNational Map.
Washington,D.C.: United StatesDepartemtnof the Interior, ReportNumber, 1.0.
Wilder, Anna,JonathanD. Brinkerhoff, andTeresaM. Higgins.2OO4.Geographic
Science:ContextualizedProfessional
InformationTechnologies+ Project-Based
DevelopmentApproach.Journal of GeographylO2.,255.
Wise, Stephen.2002. GIS Basics.London,England:Taylor & Francis.

MapalesterResearchProject

Page92
