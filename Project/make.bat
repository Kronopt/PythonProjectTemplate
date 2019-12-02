@echo off

if "%1" == "" goto help
goto %~1

:help
echo.
echo clean            <description of 'clean'>
echo lint             <description of 'lint'>
echo test             <description of 'test'>
echo coverage         <description of 'coverage'>
echo docs             <description of 'docs'>
echo sdist            <description of 'sdist'>
echo sdist-test       <description of 'sdist-test'>
echo release          <description of 'release'>
goto:eof

:clean
rmdir /s /q build
rmdir /s /q dist
del /s *.pyc
goto:eof

:lint
:: lint code
goto:eof

:test
python -m unittest <tests folder>
goto:eof

:coverage
:: coverage code
goto:eof

:docs
:: build/release docs
goto:eof

:sdist
python setup.py sdist bdist_wheel
goto:eof

:sdist-test
twine check dist/*
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
goto:eof

:release
call:sdist
twine upload dist/*
goto:eof
