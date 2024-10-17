Name:		texlive-umbclegislation
Version:	41348
Release:	2
Summary:	A LaTeX class for building legislation files for UMBC Student Government Association Bills
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/umbclegislation
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umbclegislation.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umbclegislation.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX class for building legislation files for UMBC Student
Government Association Bills. Requires pdflatex and the
mdframed enumitem, lineno, and xifthen packages.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/umbclegislation
%doc %{_texmfdistdir}/doc/latex/umbclegislation

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
