## What is this?

This is a package to get a nice favicon from a website

## Installation

pip install faviconer

## Usage

### Get favicon.ico

from faviconer import *

get_favicon("http://google.com/")

'http://google.com/favicon.ico'

### Get favicon.ico by url

from faviconer import *

get_favicon_by_url("http://google.com/")

'http://google.com/favicon.ico'

### Get favicon.ico by html

from faviconer import *

get_favicon_by_html('<html><head><link rel="shortcut icon" href="https://cdn.sstatic.net/Sites/stackoverflow/img/favicon.ico"></head><body></body</html>')

'https://cdn.sstatic.net/Sites/stackoverflow/img/favicon.ico'