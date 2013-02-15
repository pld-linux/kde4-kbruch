%define		_state		stable
%define		orgname		kbruch

Summary:	K Desktop Environment - Task generator for calculations with fractions
Summary(pl.UTF-8):	K Desktop Environment - Generator zadań z obliczeniami na ułamkach
Name:		kde4-kbruch
Version:	4.10.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	00786c2c31ab2a8c1453bc389a46513f
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel
Obsoletes:	kde4-kdeedu-kbruch < 4.6.99
Obsoletes:	kbruch < 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KBruch is a small program to generate tasks with fractions. The user
has to solve the given task by entering the right value for numerator
and denominator. The program checks the input and gives feedback. The
task generation can be adjusted by using different parameters. The
user can decide if he wants to solve tasks with addition/subtraction
and/or multiplication/division.

%description -l pl.UTF-8
Generator zadań z obliczeniami na ułamkach. KBruch to mały program do
generowania zadań z ułamkami. Użytkownik ma rozwiązać zadanie poprzez
wpisanie poprawnej wartości dla licznika i mianownika. Następnie
program sprawdza poprawność danych. Generowanie zadań można
dostosowywać przy pomocy różnych parametrów. Użytkownik może
decydować, czy chce rozwiązywać zadania z dodawaniem/odejmowaniem
i/lub mnożeniem/dzieleniem.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbruch
%{_datadir}/apps/kbruch
%{_datadir}/config.kcfg/kbruch.kcfg
%{_desktopdir}/kde4/kbruch.desktop
%{_iconsdir}/hicolor/scalable/apps/kbruch.svgz
%{_iconsdir}/hicolor/*x*/apps/kbruch.png
%{_mandir}/man1/kbruch.1*
