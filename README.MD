# UI tests for a Book Store

## Hey! There are some automated test cases for this [store](http://selenium1py.pythonanywhere.com/)

## How to install
1. Create virtual envirinment with Python v3.9. I use conda:
```sh
conda deactivate
conda create -n your_env_name python=3.9
conda activate your_env_name
```
2. Clone repo:
```sh
git clone https://github.com/uzigang16/book_store_testing.git
```
3. Install requirements:
```sh
pip install -r requirements.txt
```
4. Run tests via shell command:
```sh
pytest -v --tb=line
```
5. Enjoy watching magic:)

## Options for tests run
1. You can test specific module by running previous command with "-m" flag.
Actual modules are:
- need_review
- user
- login_guest
```sh
pytest -v --tb=line -m need_review
```
2. You can specify language in --language flag. The default is eng.
For example:
- gr
- de
- po
You cal see the full list of avaliable languages in the [store](http://selenium1py.pythonanywhere.com/) left corner
```sh
pytest -v --tb=line --language=en
```

## Project goals
### This project is written to practice with [Pytest](https://docs.pytest.org/), [Selenium](https://selenium-python.readthedocs.io/) and have some experience in UI testing. And also because I like to code:)
