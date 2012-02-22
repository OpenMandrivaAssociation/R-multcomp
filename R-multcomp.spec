%bcond_with bootstrap
%global packname  multcomp
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.2_9
Release:          2
Summary:          Simultaneous Inference in General Parametric Models
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-9.tar.gz
Requires:         R-stats R-graphics R-mvtnorm R-survival R-lme4 R-nlme
Requires:         R-robustbase R-coin R-MASS R-car R-foreign R-xtable
Requires:         R-sandwich R-lmtest R-coxme texlive-inconsolata
%if %{without bootstrap}
Requires:         R-mboost
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-stats
BuildRequires:    R-graphics R-mvtnorm R-survival R-lme4 R-nlme R-robustbase
BuildRequires:    R-coin R-MASS R-car R-foreign R-xtable R-sandwich R-lmtest
BuildRequires:    R-coxme texlive-inconsolata
%if %{without bootstrap}
BuildRequires:    R-mboost
%endif
%rename R-cran-multcomp

%description
Simultaneous tests and confidence intervals for general linear hypotheses
in parametric models, including linear, generalized linear, linear mixed
effects, and survival models. The package includes demos reproducing
analyzes presented in the book "Multiple Comparisons Using R" (Bretz,
Hothorn, Westfall, 2010, CRC Press).

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CHANGES
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/MCMT
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/applications
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/deprecated
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/multcomp*.R
