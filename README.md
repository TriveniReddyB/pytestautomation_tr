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

