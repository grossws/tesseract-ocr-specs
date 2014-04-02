%define upstreamname tesseract
Name:		%{upstreamname}-langpack
Version:	3.02
Release:	1%{?dist}
Summary:	Langpacks for tesseract

Group:		Applications/File
License:	ASL 2.0
URL:		http://code.google.com/p/tesseract-ocr/
Source1:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.rus.tar.gz
Source2:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.grc.tar.gz
Source3:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.epo_alt.tar.gz
Source4:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.ukr.tar.gz
Source5:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.tur.tar.gz
Source6:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.tha.tar.gz
Source7:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.tgl.tar.gz
Source8:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.tel.tar.gz
Source9:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.tam.tar.gz
Source10:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.swe.tar.gz
Source11:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.swa.tar.gz
Source12:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.srp.tar.gz
Source13:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.sqi.tar.gz
Source14:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.spa_old.tar.gz
Source15:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.spa.tar.gz
Source16:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.slv.tar.gz
Source17:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.slk.tar.gz
Source18:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.ron.tar.gz
Source19:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.por.tar.gz
Source20:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.pol.tar.gz
Source21:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.nor.tar.gz
Source22:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.nld.tar.gz
Source23:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.msa.tar.gz
Source24:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.mlt.tar.gz
Source25:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.mkd.tar.gz
Source26:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.mal.tar.gz
Source27:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.lit.tar.gz
Source28:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.lav.tar.gz
Source29:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.kor.tar.gz
Source30:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.kan.tar.gz
Source31:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.ita_old.tar.gz
Source32:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.ita.tar.gz
Source33:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.isl.tar.gz
Source34:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.ind.tar.gz
Source35:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.chr.tar.gz
Source36:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.hun.tar.gz
Source37:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.hrv.tar.gz
Source38:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.hin.tar.gz
Source39:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.heb.tar.gz
Source40:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.glg.tar.gz
Source41:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.frm.tar.gz
Source42:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.frk.tar.gz
Source43:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.fra.tar.gz
Source44:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.fin.tar.gz
Source45:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.eus.tar.gz
Source46:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.est.tar.gz
Source47:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.equ.tar.gz
Source48:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.epo.tar.gz
Source49:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.enm.tar.gz
Source50:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.ell.tar.gz
Source51:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.deu.tar.gz
Source52:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.dan.tar.gz
Source53:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.ces.tar.gz
Source54:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.cat.tar.gz
Source55:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.bul.tar.gz
Source56:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.ben.tar.gz
Source57:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.bel.tar.gz
Source58:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.aze.tar.gz
Source59:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.ara.tar.gz
Source60:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.afr.tar.gz
Source61:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.jpn.tar.gz
Source62:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.chi_sim.tar.gz
Source63:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.chi_tra.tar.gz
Source64:	https://tesseract-ocr.googlecode.com/files/%{upstreamname}-ocr-%{version}.vie.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
Group:		Applications/File
Requires:	%{upstreamname} >= 3.02


%package rus
Summary:	Russian language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package grc
Summary:	Ancient Greek language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package epo_alt
Summary:	Esperanto alternative language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package ukr
Summary:	Ukrainian language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package tur
Summary:	Turkish language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package tha
Summary:	Thai language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package tgl
Summary:	Tagalog language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package tel
Summary:	Telugu language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package tam
Summary:	Tamil language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package swe
Summary:	Swedish language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package swa
Summary:	Swahili language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package srp
Summary:	Serbian (Latin) language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package sqi
Summary:	Albanian language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package spa_old
Summary:	Spanish (Old) language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package spa
Summary:	Spanish language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package slv
Summary:	Slovenian language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package slk
Summary:	Slovakian language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package ron
Summary:	Romanian language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package por
Summary:	Portuguese language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package pol
Summary:	Polish  language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package nor
Summary:	Norwegian language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package nld
Summary:	Dutch language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package msa
Summary:	Malay language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package mlt
Summary:	Maltese language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package mkd
Summary:	Macedonian language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package mal
Summary:	Malayalam language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package lit
Summary:	Lithuanian language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package lav
Summary:	Latvian language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package kor
Summary:	Korean language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package kan
Summary:	Kannada language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package ita_old
Summary:	Italian (Old) language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package ita
Summary:	Italian language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package isl
Summary:	Icelandic language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package ind
Summary:	Indonesian language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package chr
Summary:	Cherokee language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package hun
Summary:	Hungarian  language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package hrv
Summary:	Croatian language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package hin
Summary:	Hindi language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package heb
Summary:	Hebrew language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package glg
Summary:	Galician language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package frm
Summary:	Middle French (ca. 1400-1600)  language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package frk
Summary:	Frankish language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package fra
Summary:	French language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package fin
Summary:	Finnish language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package eus
Summary:	Basque language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package est
Summary:	Estonian language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package equ
Summary:	Math / equation detection data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package epo
Summary:	Esperanto language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package enm
Summary:	Middle English (1100-1500) language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package ell
Summary:	Greek language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package deu
Summary:	German language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package dan
Summary:	Danish language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package ces
Summary:	Czech language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package cat
Summary:	Catalan language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package bul
Summary:	Bulgarian language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package ben
Summary:	Bengali language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package bel
Summary:	Belarusian language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package aze
Summary:	Azerbaijani language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package ara
Summary:	Arabic language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package afr
Summary:	Afrikaans language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package jpn
Summary:	Japanese language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package chi_sim
Summary:	Chinese (Simplified) language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package chi_tra
Summary:	Chinese (Traditional) language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package vie
Summary:	Vietnamese language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package dan-frak
Summary:	Danish (Fraktur) language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package deu-frak
Summary:	German (Fraktur) language data for Tesseract
Requires:	%{upstreamname} >= 3.02

%package slk-frak
Summary:	Slovakian (Fraktur) language data for Tesseract
Requires:	%{upstreamname} >= 3.02


%description

%description rus
Russian language data for Tesseract 

%description grc
Ancient Greek language data for Tesseract 

%description epo_alt
Esperanto alternative language data for Tesseract 

%description ukr
Ukrainian language data for Tesseract 

%description tur
Turkish language data for Tesseract 

%description tha
Thai language data for Tesseract 

%description tgl
Tagalog language data for Tesseract 

%description tel
Telugu language data for Tesseract 

%description tam
Tamil language data for Tesseract 

%description swe
Swedish language data for Tesseract 

%description swa
Swahili language data for Tesseract 

%description srp
Serbian (Latin) language data for Tesseract 

%description sqi
Albanian language data for Tesseract 

%description spa_old
Spanish (Old) language data for Tesseract 

%description spa
Spanish language data for Tesseract 

%description slv
Slovenian language data for Tesseract 

%description slk
Slovakian language data for Tesseract 

%description ron
Romanian language data for Tesseract 

%description por
Portuguese language data for Tesseract 

%description pol
Polish  language data for Tesseract 

%description nor
Norwegian language data for Tesseract 

%description nld
Dutch language data for Tesseract 

%description msa
Malay language data for Tesseract 

%description mlt
Maltese language data for Tesseract 

%description mkd
Macedonian language data for Tesseract 

%description mal
Malayalam language data for Tesseract 

%description lit
Lithuanian language data for Tesseract 

%description lav
Latvian language data for Tesseract 

%description kor
Korean language data for Tesseract 

%description kan
Kannada language data for Tesseract 

%description ita_old
Italian (Old) language data for Tesseract 

%description ita
Italian language data for Tesseract 

%description isl
Icelandic language data for Tesseract 

%description ind
Indonesian language data for Tesseract 

%description chr
Cherokee language data for Tesseract 

%description hun
Hungarian  language data for Tesseract 

%description hrv
Croatian language data for Tesseract 

%description hin
Hindi language data for Tesseract 

%description heb
Hebrew language data for Tesseract 

%description glg
Galician language data for Tesseract 

%description frm
Middle French (ca. 1400-1600)  language data for Tesseract 

%description frk
Frankish language data for Tesseract 

%description fra
French language data for Tesseract 

%description fin
Finnish language data for Tesseract 

%description eus
Basque language data for Tesseract 

%description est
Estonian language data for Tesseract 

%description equ
Math / equation detection data for Tesseract 

%description epo
Esperanto language data for Tesseract 

%description enm
Middle English (1100-1500) language data for Tesseract 

%description ell
Greek language data for Tesseract 

%description deu
German language data for Tesseract 

%description dan
Danish language data for Tesseract 

%description ces
Czech language data for Tesseract 

%description cat
Catalan language data for Tesseract 

%description bul
Bulgarian language data for Tesseract 

%description ben
Bengali language data for Tesseract 

%description bel
Belarusian language data for Tesseract 

%description aze
Azerbaijani language data for Tesseract 

%description ara
Arabic language data for Tesseract 

%description afr
Afrikaans language data for Tesseract 

%description jpn
Japanese language data for Tesseract 

%description chi_sim
Chinese (Simplified) language data for Tesseract 

%description chi_tra
Chinese (Traditional) language data for Tesseract 

%description vie
Vietnamese language data for Tesseract 

%description dan-frak
Danish (Fraktur) language data for Tesseract 

%description deu-frak
German (Fraktur) language data for Tesseract 

%description slk-frak
Slovakian (Fraktur) language data for Tesseract 


%prep
%setup -c -T
for i in %sources; do 
  tar xzf $i --strip 1
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{upstreamname}/tessdata/
rm tessdata/eng.*
install -p -m 644 -t $RPM_BUILD_ROOT%{_datadir}/%{upstreamname}/tessdata/ tessdata/*

%clean
rm -rf $RPM_BUILD_ROOT


%files rus
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/rus.*

%files grc
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/grc.*

%files epo_alt
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/epo_alt.*

%files ukr
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/ukr.*

%files tur
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/tur.*

%files tha
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/tha.*

%files tgl
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/tgl.*

%files tel
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/tel.*

%files tam
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/tam.*

%files swe
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/swe.*

%files swa
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/swa.*

%files srp
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/srp.*

%files sqi
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/sqi.*

%files spa_old
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/spa_old.*

%files spa
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/spa.*

%files slv
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/slv.*

%files slk
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/slk.*

%files ron
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/ron.*

%files por
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/por.*

%files pol
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/pol.*

%files nor
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/nor.*

%files nld
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/nld.*

%files msa
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/msa.*

%files mlt
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/mlt.*

%files mkd
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/mkd.*

%files mal
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/mal.*

%files lit
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/lit.*

%files lav
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/lav.*

%files kor
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/kor.*

%files kan
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/kan.*

%files ita_old
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/ita_old.*

%files ita
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/ita.*

%files isl
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/isl.*

%files ind
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/ind.*

%files chr
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/chr.*

%files hun
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/hun.*

%files hrv
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/hrv.*

%files hin
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/hin.*

%files heb
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/heb.*

%files glg
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/glg.*

%files frm
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/frm.*

%files frk
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/frk.*

%files fra
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/fra.*

%files fin
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/fin.*

%files eus
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/eus.*

%files est
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/est.*

%files equ
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/equ.*

%files epo
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/epo.*

%files enm
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/enm.*

%files ell
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/ell.*

%files deu
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/deu.*

%files dan
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/dan.*

%files ces
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/ces.*

%files cat
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/cat.*

%files bul
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/bul.*

%files ben
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/ben.*

%files bel
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/bel.*

%files aze
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/aze.*

%files ara
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/ara.*

%files afr
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/afr.*

%files jpn
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/jpn.*

%files chi_sim
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/chi_sim.*

%files chi_tra
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/chi_tra.*

%files vie
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/vie.*

%files dan-frak
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/dan-frak.*

%files deu-frak
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/deu-frak.*

%files slk-frak
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/slk-frak.*


%changelog
* Sun Sep 29 2013 Konstantin Gribov <grossws@gmail.com> - 3.02-1
- Updated to v3.02

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 01 2010 Karol Trzcionka <karlikt at gmail.com> - 3.00-1
- Update to v3.00+
- Naming based on upstream

* Thu Dec 10 2009 Karol Trzcionka <karlikt at gmail.com> - 2.00-6
- Delete %%{?dist} macro

* Thu Dec 10 2009 Karol Trzcionka <karlikt at gmail.com> - 2.00-5
- Fix typo

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 24 2007 Karol Trzcionka <karlikt at gmail.com> - 2.00-2
- Fixed executable file in nl
* Tue Aug 21 2007 Karol Trzcionka <karlikt at gmail.com> - 2.00-1
- Initial Release
