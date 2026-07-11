%global tl_name pst-poker
%global tl_revision 75726

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.04a
Release:	%{tl_revision}.1
Summary:	Drawing poker cards
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-poker
License:	lgpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-poker.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-poker.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This PSTricks related package can create poker cards in various manners.

