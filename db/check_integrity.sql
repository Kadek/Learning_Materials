use firma_db
go

/* sprawdzamy integralnoœc poprzez usuwanie */
DELETE FROM woj WHERE woj.kod_woj = 'Wam'

DELETE FROM miasta WHERE miasta.nazwa = 'Warszawa'

DELETE FROM firmy WHERE firmy.nazwa = 'Poczta Polska'

DELETE FROM osoby WHERE osoby.nazwisko = 'Kasperowicz'
go

/* sprawdzamy integralnoœc poprzez dodawanie */
INSERT INTO etaty 
(	id_osoby
,	id_firmy
,	pensja
,	od
,	do
,	stanowisko
) values 
(	99999
,	'XXX'
,	1600
,	convert(datetime,'19980102',112)
,	convert(datetime,'20000101',112)
,	'Asystent'
)

INSERT INTO firmy 
(	nazwa_skr
,	nazwa
,	id_miasta
,	kod_pocztowy
,	ulica
) values 
(	'XXX'
,	'Politechnika Warszawska'
,	99999
,	'00-000'
,	'Pl. Politechniki 1'
)

insert into osoby (imiê, nazwisko, id_miasta) values ('Adam', 'Adamowicz', 99999)
declare @id_aa int
SET @id_aa = SCOPE_IDENTITY()

insert into miasta (kod_woj, nazwa) values ('XXX', 'W³oc³awek')
declare @id_wlo int
set @id_wlo = SCOPE_IDENTITY()