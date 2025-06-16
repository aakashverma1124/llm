## Setup Python virtual enviroment

`cd python`

`python3 -m venv venv`

`source venv/bin/activate` for Mac/Linux `.\venv\Scripts\activate` for Windows

`pip install -r requirements.txt`

Keep adding dependencies that you need in the `requirement.txt` files and whenever you need them just run `pip install -r requirements.txt`

## Build in this order if you're following and building on your machine.

- intro-project
- web-summarization

## Run projects

`python3 <project_name>/main.py`

## `web-summarization` project

Add the following packages in `requirement.txt` file.
`requests>=2.0.0`
`beautifulsoup4>=4.0.0`
and then run `pip install -r requirements.txt`

`requests`: for making http requests
`beautifulsoup4`: for scraping the content of the website.

requests>=2.0.0
beautifulsoup4>=4.0.0
