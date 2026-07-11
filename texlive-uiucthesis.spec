%global tl_name uiucthesis
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.25
Release:	%{tl_revision}.1
Summary:	UIUC thesis class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uiucthesis
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uiucthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uiucthesis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uiucthesis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class produces a document that conforms to the format described in
the University's Handbook for Graduate Students Preparing to Deposit.

