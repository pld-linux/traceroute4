Summary:	A new version of 'traceroute'
Summary(pl):	Nowa wersja 'traceroute'
Name:		traceroute4
Version:	991603
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	ftp://ftp.nikhef.nl/pub/network/traceroute_%{version}.tar.Z
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A new version of 'traceroute', a utility to show the network
route to a certain destination. Among the new features are:
 o  Optional ttl reporting.
 o  Optional use of the loose source routing facility,
    to show the route between arbitrary destinations.
 o  Enhanced portability, to run on a variety of platforms.
 o  Improved timeout handling during icmp packet catching.
 o  Option to probe all addresses of multi-homed destinations.
 o  Option to disable fragmentation and perform MTU discovery.
 o  Recognize various new icmp packet types.
 o  Round-trip time reporting in fractional milliseconds.
 o  Option to display the Autonomous System number for each hop.
 o  Option to display the network name for each hop.
 o  Configurable default options via environment variables.
 o  Optional setting of initial ttl to skip first hops.
 o  Optional min/avg/max rtt statistics summary for each hop.
 o  Include standard deviation in rtt statistics summary.
 o  Cache nameserver lookups to minimize DNS queries.

%description -l pl
Nowa wersja 'traceroute'.

%prep
%setup -q -c %{name}

%build
%{__make} CFLAGS="%{rpmcflags} -D_BSD_SOURCE" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install traceroute $RPM_BUILD_ROOT%{_bindir}/traceroute4

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(4754,root,icmp) %{_bindir}/traceroute4
