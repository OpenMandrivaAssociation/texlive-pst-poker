Name:		texlive-pst-poker
Version:	65818
Release:	1
Summary:	Drawing poker cards
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pst-poker
License:	lgpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-poker.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-poker.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This PSTricks related package can create poker cards in various
manners.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pst-poker
%doc %{_texmfdistdir}/doc/latex/pst-poker

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
