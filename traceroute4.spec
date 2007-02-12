Summary:	A new version of 'traceroute'
Summary(pl.UTF-8):	Nowa wersja 'traceroute'
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

%description -l pl.UTF-8
Nowa wersja 'traceroute' - narzędzia pokazującego trasę w sieci do
określonego celu. Wśród nowych możliwości są:
- opcjonalne podawanie TTL,
- opcjonalne używanie swobodnego routingu źródłowego w celu pokazania
  trasy między dowolnymi celami,
- rozszerzona przenośność w celu działania na wielu platformach,
- ulepszona obsługa timeoutów podczas chwytania pakietów ICMP,
- opcja sprawdzania wszystkich adresów danego celu,
- opcja wyłączenia fragmentacji i wykrywania MTU,
- rozpoznawanie różnych nowych rodzajów pakietów ICMP,
- podawanie czasu podróży pakietu w ułamkach milisekund,
- opcja wyświetlania numeru systemu dla każdego kroku,
- opcja wyświetlania nazwy sieci dla każdego kroku,
- opcje domyślne konfigurowalne poprzez zmienne środowiskowe,
- opcjonalne ustawianie początkowego TTL dla pominięcia pierwszych
  kroków,
- opcjonalne statystyki min./śr./maks. rtt dla każdego kroku,
- dołączanie odchylenia standardowego do statystyk,
- zapamiętywanie wyników zapytań DNS w celu zminimalizowania liczby
  zapytań.

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
