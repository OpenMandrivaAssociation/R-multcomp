%define modulename multcomp
%define realver 1.0-8
%define r_library %{_libdir}/R/library

Summary:	Simultaneous Inference in General Parametric Models for R
Name:		R-cran-%{modulename}
Version:	%(echo %{realver} | tr '-' '.')
Release:	%mkrel 1
License:	GPLv2
Group:		Sciences/Mathematics
Url:		http://cran.r-project.org/web/packages/%{modulename}/index.html
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{realver}.tar.gz
BuildRequires:	R-base
BuildRequires:	R-cran-mvtnorm
Requires:	R-base
Requires:	R-cran-mvtnorm
Suggests:	R-cran-car
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The package contains simultaneous tests and confidence intervals for 
general linear hypotheses in parametric models, including linear, 
generalized linear, linear mixed effects, and survival models.

%prep
%setup -q -c

%build

R CMD build --no-vignettes %{modulename}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{r_library}

# install
R CMD INSTALL %{modulename} --library=%{buildroot}/%{r_library}

# provided by R-base
rm -rf %{buildroot}/%{r_library}/R.css

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{r_library}/%{modulename}
