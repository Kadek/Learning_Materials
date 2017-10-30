CREATE DATABASE firma_db
go

use firma_db
go

CREATE TABLE [dbo].woj(
	kod_woj	char(3)	not null
	constraint pk_woj primary key
,	nazwa	varchar(30)
)

CREATE TABLE [dbo].miasta(
	id_miasta	int	not null	identity
	constraint pk_miasta primary key
,	kod_woj	char(3) not null
	constraint	fk_miasta__woj foreign key
	references woj(kod_woj)
,	nazwa	varchar(30)	not null
)

CREATE TABLE [dbo].osoby(
	id_osoby	int	not null	identity
	constraint pk_osoby primary key
,	id_miasta	int not null
	constraint fk_osoby__miasta foreign key
	references miasta(id_miasta)
,	imiê		varchar(30)	not null
,	nazwisko	varchar(30)	not null
,	imiê_i_nazwisko as convert(char(24), left(imiê,1) + '. ' + nazwisko)
)

CREATE TABLE [dbo].firmy(
	nazwa_skr	char(3)	not null
	constraint pk_firmy primary key
,	id_miasta	int not null
	constraint fk_firmy__miasta foreign key
	references miasta(id_miasta)
,	nazwa		varchar(30) not null
,	kod_pocztowy	char(6) not null
,	ulica		varchar(60) not null
)


CREATE TABLE [dbo].etaty(
	id_etatu integer not null identity
	constraint pk_etaty primary key
,	id_osoby integer not null
	constraint fk_etaty__osoby foreign key
	references osoby(id_osoby)
,	id_firmy char(3) not null
	constraint fk_etaty__firmy foreign key
	references firmy(nazwa_skr)
,	stanowisko	varchar(60)	not null
,	pensja 		money 		not null
,	od 		datetime 	not null
,	do 		datetime 	null
)
