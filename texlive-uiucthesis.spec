# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/uiucthesis
# catalog-date 2007-01-20 15:20:16 +0100
# catalog-license lppl
# catalog-version 2.25
Name:		texlive-uiucthesis
Version:	2.25
Release:	5
Summary:	UIUC thesis class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uiucthesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uiucthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uiucthesis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uiucthesis.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class produces a document that conforms to the format
described in the University's Handbook for Graduate Students
Preparing to Deposit.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/uiucthesis/uiucthesis.cls
%{_texmfdistdir}/tex/latex/uiucthesis/uiucthesis.sty
%doc %{_texmfdistdir}/doc/latex/uiucthesis/README
%doc %{_texmfdistdir}/doc/latex/uiucthesis/thesis-ex.pdf
%doc %{_texmfdistdir}/doc/latex/uiucthesis/thesis-ex.tex
%doc %{_texmfdistdir}/doc/latex/uiucthesis/uiucthesis.pdf
#- source
%doc %{_texmfdistdir}/source/latex/uiucthesis/uiucthesis.dtx
%doc %{_texmfdistdir}/source/latex/uiucthesis/uiucthesis.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.25-2
+ Revision: 757245
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.25-1
+ Revision: 719835
- texlive-uiucthesis
- texlive-uiucthesis
- texlive-uiucthesis

