cd %~dp0
echo off
setlocal EnableExtensions EnableDelayedExpansion
path="C:\python27";"C:\python27\Scripts";%path%
echo %path%

if %1%==test (
    python setup.py test
)

if "%1%"=="upload_test" (
    rmdir dist /s /q
    python setup.py sdist
    echo "YOU ARE UPLOADING TO TEST PYPI REPO"
    echo "Checklist"
    echo "1. Have you done the readme?"
    pause
    twine upload --repository testpypi dist/*
)

if "%1%"=="upload_main" (
    rmdir dist /s /q
    python setup.py sdist
    echo "YOU ARE UPLOADING TO MAIN PYPI REPO"
    echo "Checklist"
    echo "1. Have you done the readme?"
    pause
    twine upload --repository pypi dist/*
)

