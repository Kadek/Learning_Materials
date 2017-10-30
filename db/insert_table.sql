use firma_db
go

/* czyœcimy bazê danych */
DELETE FROM etaty
DELETE FROM firmy
DELETE FROM osoby
DELETE FROM miasta
DELETE FROM woj
go

/* dodajemy województwa */
insert into woj values ('Maz', 'Mazowieckie')
insert into woj values ('Pom', 'Pomorskie')
insert into woj values ('Zap', 'Zachodniopomorskie')
insert into woj values ('Wam', 'Warmiñsko-Mazurskie')
insert into woj values ('Pod', 'Podlaskie')
insert into woj values ('Kup', 'Kujawsko-Pomorskie')
insert into woj values ('Wie', 'Wielkopolskie')
insert into woj values ('Lub', 'Lubuskie')


/* dodajemy miasta */
insert into miasta (kod_woj, nazwa) values ('Maz', 'Warszawa')
declare @id_wwa int
SET @id_wwa = SCOPE_IDENTITY()

insert into miasta (kod_woj, nazwa) values ('Pom', 'Gdañsk')
declare @id_gda int
set @id_gda = SCOPE_IDENTITY()

insert into miasta (kod_woj, nazwa) values ('Zap', 'Szczecin')
declare @id_szc int
set @id_szc = SCOPE_IDENTITY()

insert into miasta (kod_woj, nazwa) values ('Wam', 'Olsztyn')
declare @id_oln int
set @id_oln = SCOPE_IDENTITY()

insert into miasta (kod_woj, nazwa) values ('Wam', 'Elbl¹g')
declare @id_elb int
set @id_elb = SCOPE_IDENTITY()

insert into miasta (kod_woj, nazwa) values ('Wam', 'Olsztynek')
declare @id_ols int
set @id_ols = SCOPE_IDENTITY()

insert into miasta (kod_woj, nazwa) values ('Wam', 'Wêgorzewo')
declare @id_weg int
set @id_weg = SCOPE_IDENTITY()

insert into miasta (kod_woj, nazwa) values ('Wam', 'Kêtrzyn')
declare @id_ket int
set @id_ket = SCOPE_IDENTITY()

insert into miasta (kod_woj, nazwa) values ('Wam', 'Barczewo')
declare @id_bar int
set @id_bar = SCOPE_IDENTITY()

insert into miasta (kod_woj, nazwa) values ('Wam', 'Mr¹gowo')
declare @id_mra int
set @id_mra = SCOPE_IDENTITY()

insert into miasta (kod_woj, nazwa) values ('Pod', 'Bia³ystok')
declare @id_bia int
set @id_bia = SCOPE_IDENTITY()

insert into miasta (kod_woj, nazwa) values ('Pod', '£om¿a')
declare @id_lom int
set @id_lom = SCOPE_IDENTITY()

insert into miasta (kod_woj, nazwa) values ('Pod', 'Suwa³ki')
declare @id_suw int
set @id_suw = SCOPE_IDENTITY()

insert into miasta (kod_woj, nazwa) values ('Pod', 'Augustów')
declare @id_aug int
set @id_aug = SCOPE_IDENTITY()

insert into miasta (kod_woj, nazwa) values ('Pod', 'Zambrów')
declare @id_zam int
set @id_zam = SCOPE_IDENTITY()

insert into miasta (kod_woj, nazwa) values ('Kup', 'Bydgoszcz')
declare @id_byd int
set @id_byd = SCOPE_IDENTITY()

insert into miasta (kod_woj, nazwa) values ('Kup', 'Toruñ')
declare @id_tor int
set @id_tor = SCOPE_IDENTITY()

insert into miasta (kod_woj, nazwa) values ('Kup', 'Inowroc³aw')
declare @id_ino int
set @id_ino = SCOPE_IDENTITY()

insert into miasta (kod_woj, nazwa) values ('Kup', 'Grudzi¹dz')
declare @id_gru int
set @id_gru = SCOPE_IDENTITY()

insert into miasta (kod_woj, nazwa) values ('Kup', 'W³oc³awek')
declare @id_wlo int
set @id_wlo = SCOPE_IDENTITY()


/* dodajemy osoby */
insert into osoby (imiê, nazwisko, id_miasta) values ('Adam', 'Kasperowicz', @id_oln)
declare @id_ak int
SET @id_ak = SCOPE_IDENTITY()

insert into osoby (imiê, nazwisko, id_miasta) values ('Adam', 'Adamowicz', @id_wwa)
declare @id_aa int
SET @id_aa = SCOPE_IDENTITY()

insert into osoby (imiê, nazwisko, id_miasta) values ('Adam', 'Barbarossa', @id_gda)
declare @id_ab int
SET @id_ab = SCOPE_IDENTITY()

insert into osoby (imiê, nazwisko, id_miasta) values ('Adam', 'Ca³y', @id_szc)
declare @id_ac int
SET @id_ac = SCOPE_IDENTITY()

insert into osoby (imiê, nazwisko, id_miasta) values ('Adam', 'Drozd', @id_elb)
declare @id_ad int
SET @id_ad = SCOPE_IDENTITY()

insert into osoby (imiê, nazwisko, id_miasta) values ('Bonifacy', 'Edward', @id_ols)
declare @id_be int
SET @id_be = SCOPE_IDENTITY()

insert into osoby (imiê, nazwisko, id_miasta) values ('Bonifacy', 'Fjordowy', @id_weg)
declare @id_bf int
SET @id_bf = SCOPE_IDENTITY()

insert into osoby (imiê, nazwisko, id_miasta) values ('Zenon', 'Martyniuk', @id_wlo)
declare @id_zm int
SET @id_zm = SCOPE_IDENTITY()

insert into osoby (imiê, nazwisko, id_miasta) values ('Jimi', 'Hendrix', @id_aug)
declare @id_jh int
SET @id_jh = SCOPE_IDENTITY()

insert into osoby (imiê, nazwisko, id_miasta) values ('Zawisza', 'Czarny', @id_wwa)
declare @id_zc int
SET @id_zc = SCOPE_IDENTITY()

insert into osoby (imiê, nazwisko, id_miasta) values ('Franz', 'Szkop', @id_gda)
declare @id_fz int
SET @id_fz = SCOPE_IDENTITY()

insert into osoby (imiê, nazwisko, id_miasta) values ('Mateusz', 'Ojciec', @id_ols)
declare @id_mo int
SET @id_mo = SCOPE_IDENTITY()

insert into osoby (imiê, nazwisko, id_miasta) values ('Barack', 'Trump', @id_tor)
declare @id_bt int
SET @id_bt = SCOPE_IDENTITY()

insert into osoby (imiê, nazwisko, id_miasta) values ('Osama', 'Husajn', @id_oln)
declare @id_oh int
SET @id_oh = SCOPE_IDENTITY()

insert into osoby (imiê, nazwisko, id_miasta) values ('Xi', 'Jinping', @id_ket)
declare @id_xj int
SET @id_xj = SCOPE_IDENTITY()

insert into osoby (imiê, nazwisko, id_miasta) values ('Super', 'Pan', @id_tor)
declare @id_sp int
SET @id_sp = SCOPE_IDENTITY()

insert into osoby (imiê, nazwisko, id_miasta) values ('Adam', 'Kasprowicz', @id_oln)

insert into osoby (imiê, nazwisko, id_miasta) values ('Byl', 'Juz', @id_ket)
declare @id_bj int
SET @id_bj = SCOPE_IDENTITY()

insert into osoby (imiê, nazwisko, id_miasta) values ('£ysy', 'Aktor', @id_gru)
declare @id_la int
SET @id_la = SCOPE_IDENTITY()

insert into osoby (imiê, nazwisko, id_miasta) values ('Cypis', 'Artysta', @id_oln)
declare @id_ca int
SET @id_ca = SCOPE_IDENTITY()

insert into osoby (imiê, nazwisko, id_miasta) values ('Figo', 'Fagot', @id_oln)
declare @id_ff int
SET @id_ff = SCOPE_IDENTITY()

insert into osoby (imiê, nazwisko, id_miasta) values ('Mozart', 'Chopin', @id_gru)
declare @id_mc int
SET @id_mc = SCOPE_IDENTITY()

insert into osoby (imiê, nazwisko, id_miasta) values ('Bob', 'Budowniczy', @id_oln)
declare @id_bb int
SET @id_bb = SCOPE_IDENTITY()

insert into osoby (imiê, nazwisko, id_miasta) values ('Jakiœ', 'Koleœ', @id_lom)
declare @id_jk int
SET @id_jk = SCOPE_IDENTITY()

insert into osoby (imiê, nazwisko, id_miasta) values ('Jako', 'Tako', @id_lom)


/* dodajemy firmy */
insert into firmy 
(	nazwa_skr
,	nazwa
,	id_miasta
,	kod_pocztowy
,	ulica
) values 
(	'HP'
, 	'Hewlett Packard'
,	@id_wwa
,	'00-000'
,	'Szturmowa 2a'
)

insert into firmy 
(	nazwa_skr
,	nazwa
,	id_miasta
,	kod_pocztowy
,	ulica
) values 
(	'PW'
,	'Politechnika Warszawska'
,	@id_wwa
,	'00-000'
,	'Pl. Politechniki 1'
)

insert into firmy 
(	nazwa_skr
,	nazwa
,	id_miasta
,	kod_pocztowy
,	ulica
) values 
(	'F£P'
,	'Fabryka £odzi Podwodnych'
,	@id_wwa
,	'00-000'
,	'Na dnie 4'
)

insert into [dbo].firmy 
(	nazwa_skr
,	nazwa
,	id_miasta
,	kod_pocztowy
,	ulica
) values 
(	'GS'
, 	'Goldman Sachs'
,	@id_gda
,	'00-000'
,	'Bankowa 4'
)

insert into [dbo].firmy 
(	nazwa_skr
,	nazwa
,	id_miasta
,	kod_pocztowy
,	ulica
) values 
(	'CS'
, 	'Credit Suisse'
,	@id_gda
,	'00-010'
,	'Szwajcarska 3'
)

insert into [dbo].firmy 
(	nazwa_skr
,	nazwa
,	id_miasta
,	kod_pocztowy
,	ulica
) values 
(	'GOG'
, 	'Google'
,	@id_gda
,	'00-100'
,	'Internetowa 5'
)

insert into [dbo].firmy 
(	nazwa_skr
,	nazwa
,	id_miasta
,	kod_pocztowy
,	ulica
) values 
(	'PT'
, 	'Piekarnia Tyrolska'
,	@id_tor
,	'01-000'
,	'Austraicka 60'
)

insert into [dbo].firmy 
(	nazwa_skr
,	nazwa
,	id_miasta
,	kod_pocztowy
,	ulica
) values 
(	'RY'
, 	'RyanAir'
,	@id_tor
,	'00-120'
,	'Irlandzka -1'
)

insert into [dbo].firmy 
(	nazwa_skr
,	nazwa
,	id_miasta
,	kod_pocztowy
,	ulica
) values 
(	'CR'
, 	'Casino Royale'
,	@id_tor
,	'02-000'
,	'Handlowa 10'
)

insert into [dbo].firmy 
(	nazwa_skr
,	nazwa
,	id_miasta
,	kod_pocztowy
,	ulica
) values 
(	'BM'
, 	'BudiMex'
,	@id_oln
,	'00-034'
,	'Budowlana 15'
)

insert into [dbo].firmy 
(	nazwa_skr
,	nazwa
,	id_miasta
,	kod_pocztowy
,	ulica
) values 
(	'ZT'
, 	'Zoltrax'
,	@id_oln
,	'00-000'
,	'Drukarkowa 35'
)

insert into [dbo].firmy 
(	nazwa_skr
,	nazwa
,	id_miasta
,	kod_pocztowy
,	ulica
) values 
(	'JM'
, 	'Jeronimo Martins'
,	@id_oln
,	'00-678'
,	'Biedronkowa 900'
)

insert into [dbo].firmy 
(	nazwa_skr
,	nazwa
,	id_miasta
,	kod_pocztowy
,	ulica
) values 
(	'VW'
, 	'Volkswagen'
,	@id_oln
,	'00-111'
,	'Niemiecka 39'
)

insert into [dbo].firmy 
(	nazwa_skr
,	nazwa
,	id_miasta
,	kod_pocztowy
,	ulica
) values 
(	'ZTM'
, 	'Zarz¹d Transportu Miejskiego'
,	@id_oln
,	'00-000'
,	'Transportowa 1'
)

insert into [dbo].firmy 
(	nazwa_skr
,	nazwa
,	id_miasta
,	kod_pocztowy
,	ulica
) values 
(	'PP'
, 	'Poczta Polska'
,	@id_oln
,	'00-000'
,	'Donosicielska 2'
)


/* dodajemy etaty */
insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	@id_jh
,	'PW'
,	600
,	convert(datetime,'19940101',112)
,	convert(datetime,'19980101',112)
,	'Doktorant'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	@id_bj
,	'PW'
,	1600
,	convert(datetime,'19980102',112)
,	convert(datetime,'20000101',112)
,	'Asystent'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	stanowisko
) values 
(	@id_mc
,	'PW'
,	3200
,	convert(datetime,'20000102',112)
,	'Adjunkt'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	stanowisko
) values 
(	@id_xj
,	'PW'
,	2200
,	convert(datetime,'19990101',112)
,	'Sprz¹tacz'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	stanowisko
) values 
(	@id_be
,	'HP'
,	20000
,	convert(datetime,'20000101',112)
,	'Konsultant'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	stanowisko
) values 
(	@id_ab
,	'PW'
,	3200
,	convert(datetime,'20011110',112)
,	'Adjunkt'
)


insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	stanowisko
,	do
) values 
(	@id_ac
,	'PW'
,	4200
,	convert(datetime,'20040922',112)
,	'Magazynier'
,	convert(datetime,'20041022',112)
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	stanowisko
,	do
) values 
(	@id_ad
,	'HP'
,	50000
,	convert(datetime,'20000101',112)
,	'Dyrektor'
,	convert(datetime,'20021021',112)
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	stanowisko
,	do
) values 
(	@id_bf
,	'F£P'
,	6200
,	convert(datetime,'20040922',112)
,	'Kierownik'
,	convert(datetime,'20041022',112)
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	stanowisko
) values 
(	@id_ad
,	'F£P'
,	65200
,	convert(datetime,'20041023',112)
,	'Prezes'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	@id_ak
,	'PP'
,	1600
,	convert(datetime,'19980102',112)
,	null
,	'Asystent'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	@id_oh
,	'PP'
,	1000
,	convert(datetime,'19980102',112)
,	convert(datetime,'20000101',112)
,	'Listonosz'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	@id_ca
,	'PP'
,	3200
,	convert(datetime,'19980102',112)
,	convert(datetime,'20000101',112)
,	'Kierowca'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	@id_jk
,	'GS'
,	16000
,	convert(datetime,'20000101',112)
,	null
,	'Sekretarka'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	@id_jk
,	'CS'
,	160
,	convert(datetime,'19980102',112)
,	convert(datetime,'20000101',112)
,	'T³umacz'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	@id_ff
,	'VW'
,	9000
,	convert(datetime,'19980102',112)
,	convert(datetime,'20000101',112)
,	'In¿ynier'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	@id_ff
,	'PT'
,	1500
,	convert(datetime,'20000101',112)
,	convert(datetime,'20010101',112)
,	'Piekarz'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	@id_fz
,	'RY'
,	5000
,	convert(datetime,'20000101',112)
,	null
,	'Pilot'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	@id_mo
,	'RY'
,	5000
,	convert(datetime,'19980102',112)
,	null
,	'Pilot'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	@id_fz
,	'RY'
,	5000
,	convert(datetime,'19980102',112)
,	convert(datetime,'20000101',112)
,	'Pilot'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	@id_be
,	'GOG'
,	10
,	convert(datetime,'19980102',112)
,	convert(datetime,'20000101',112)
,	'Programista'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	@id_zm
,	'GOG'
,	160000
,	convert(datetime,'19980102',112)
,	convert(datetime,'20000101',112)
,	'Diversity Manager'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	@id_zm
,	'GOG'
,	1000
,	convert(datetime,'20000101',112)
,	null
,	'Data Scraper'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	@id_ff
,	'BM'
,	4000
,	convert(datetime,'19980102',112)
,	convert(datetime,'20000101',112)
,	'Brygadzista'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	@id_bf
,	'BM'
,	10000
,	convert(datetime,'19980102',112)
,	convert(datetime,'20000101',112)
,	'Prezes'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	@id_xj
,	'BM'
,	2100
,	convert(datetime,'19980102',112)
,	convert(datetime,'20000101',112)
,	'Robotnik'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	@id_sp
,	'BM'
,	2100
,	convert(datetime,'19980102',112)
,	null
,	'Robotnik'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	@id_bb
,	'HP'
,	1600
,	convert(datetime,'19980102',112)
,	convert(datetime,'20000101',112)
,	'Monter Drukarek'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	@id_bb
,	'HP'
,	2600
,	convert(datetime,'20000101',112)
,	convert(datetime,'20010101',112)
,	'Projektant Drukarek'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	@id_bb
,	'HP'
,	3600
,	convert(datetime,'20010101',112)
,	convert(datetime,'20020101',112)
,	'Designer Drukarek'
)

insert into etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	@id_bb
,	'HP'
,	4600
,	convert(datetime,'20020101',112)
,	null
,	'Sprz¹tacz'
)
