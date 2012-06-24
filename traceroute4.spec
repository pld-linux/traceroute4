Summary:	A new version of 'traceroute'
Summary(pl):	Nowa wersja 'traceroute'
Name:		traceroute4
Version:	991603
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	ftp://ftp.nikhef.nl/pub/network/traceroute_%{version}.tar.Z
# Source0-md5:	0e0cf1f08525c531c7db9dc604b77b11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A new version of 'traceroute', a utility to show the network route to
a certain destination. Among the new features are:
- Optional TTL reporting.
- Optional use of the loose source routing facility, to show the route
  between arbitrary destinations.
- Enhanced portability, to run on a variety of platforms.
- Improved timeout handling during ICMP packet catching.
- Option to probe all addresses of multi-homed destinations.
- Option to disable fragmentation and perform MTU discovery.
- Recognize various new ICMP packet types.
- Round-trip time reporting in fractional milliseconds.
- Option to display the Autonomous System number for each hop.
- Option to display the network name for each hop.
- Configurable default options via environment variables.
- Optional setting of initial TTL to skip first hops.
- Optional min/avg/max rtt statistics summary for each hop.
- Include standard deviation in rtt statistics summary.
- Cache nameserver lookups to minimize DNS queries.

%description -l pl
Nowa wersja 'traceroute' - narz�dzia pokazuj�cego tras� w sieci do
okre�lonego celu. W�r�d nowych mo�liwo�ci s�:
- opcjonalne podawanie TTL,
- opcjonalne u�ywanie swobodnego routingu �r�d�owego w celu pokazania
  trasy mi�dzy dowolnymi celami,
- rozszerzona przeno�no�� w celu dzia�ania na wielu platformach,
- ulepszona obs�uga timeout�w podczas chwytania pakiet�w ICMP,
- opcja sprawdzania wszystkich adres�w danego celu,
- opcja wy��czenia fragmentacji i wykrywania MTU,
- rozpoznawanie r�nych nowych rodzaj�w pakiet�w ICMP,
- podawanie czasu podr�y pakietu w u�amkach milisekund,
- opcja wy�wietlania numeru systemu dla ka�dego kroku,
- opcja wy�wietlania nazwy sieci dla ka�dego kroku,
- opcje domy�lne konfigurowalne poprzez zmienne �rodowiskowe,
- opcjonalne ustawianie pocz�tkowego TTL dla pomini�cia pierwszych
  krok�w,
- opcjonalne statystyki min./�r./maks. rtt dla ka�dego kroku,
- do��czanie odchylenia standardowego do statystyk,
- zapami�tywanie wynik�w zapyta� DNS w celu zminimalizowania liczby
  zapyta�.

%prep
%setup -q -c %{name}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -D_BSD_SOURCE" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install traceroute $RPM_BUILD_ROOT%{_bindir}/traceroute4

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(4754,root,icmp) %{_bindir}/traceroute4
