this python test setup use for both API and WEB UI Test Automation Framework.

v	Verbose
s	display print stmt options in ide tool
k	execute only specific test
m	execute tagging(smoke/sanity) tests / execute group of test cases


Execute tests with diff options:
---------------------------------
pytest -s -v -k <specific_method_name> <folder_name> --html <folder_path>/<report_filename.html>


>> run full suite w/o markers:
pytest -v -s -m Regression .\Usecases\ --html .\Reports\regressiontests.html
pytest -v .\Usecases\ --html .\Reports\testresults.html


Git setup:
----------
pip init -b main
git add .


install/uninstall libraries and load to requirement file.
-----------------------------------------------------
pip install robotframework
pip freeze -- local > requirements.txt



create a local repository from main/master branch bydefault.
push to git remote repository

Create repo/folder(mytestproject) in local system
1. mytestproject# git init -b main
2. mytestproject# git add .
3. mytestproject# git commit -m <msg>
4. create repository in github login
5. map local repo to git remote repo: <this path copy from github>.
mytestproject #git remote add origin https://github.com/TriveniReddyB/pytestautomation_tr.git

6. push changes from local repo branch to remote repo branch.
mytestproject# git push --set-upstream origin main

7.check tracked/untracked files
mytestproject# git status
mytestproject# git add .
mytestproject# git commit -m <new chnages>
mytestproject# git push
