# A web crawler project

Written and tested against Python 3.6, using a virtualenv

To setup and activate the virtualenv:
* `virtualenv venv --python=python3.6`
* `source venv/bin/activate`
* `pip install -r requirements.txt`

To run the command: `python source/web_crawler.py http://www.yoyowallet.com`

To run the tests: `python -m unittest`

To run the tests automatically upon code change:
* `npm install -g gulp-cli`
* `npm install`
* `gulp watch`
