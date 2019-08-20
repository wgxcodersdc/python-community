
Tutorial python files for WWC DC Python presentation on Scrapy.

The slide deck that goes with these files is at: https://docs.google.com/presentation/d/1MiD_cJbEWjd0kOrxjEK7ptnYZGits-kT7H-g602FOPI/edit?usp=sharing

# Before You Start

1. Clone the womenwhocode repo. You only need the 'scrapy_tutorial' directory for this lab.
2. Install python if you don't have it. Python 3 is preferred.
3. Make a python virtual environment and install Scrapy.

    * Python with pip. Create the virtual env in your scrapy tutorial directory.
    ```
    cd /path/to/repo/scrapy
    python3 -m venv scrapy_venv
    source scrapy_venv/bin/activate
    pip install -r requirements.txt
    ```

    * Python with conda. Conda will put the virtual env in your conda envs directory.
    ```
    conda create -n scrapy_venv python=3.6
    conda install -n scrapy_env -c conda-forge scrapy
    conda install -n scrapy_env beautifulsoup4
    conda install -n scrapy_env python-dateutil
    source activate scrapy_env
    ```
	
	* Note: Scrapy takes a while to install because it has many dependencies. See https://docs.scrapy.org/en/latest/intro/install.html if you run into issues.
4. The spiders in this repo in wwc directory have numbers that indicate the rough order for working through them.

# Making a Scrapy Project

1. We will run scrapy from the terminal (mac) or cmd prompt (windows). We will not 
be using Jupyter Notebook in this lab.
	* open a terminal or cmd prompt
	```
    cd /path/to/the/repo/scrapy_tutorial
    scrapy startproject wwc_tutorial
    ```
    * this creates a wwc_tutorial directory that is your project skeleton:
        * config directory
        * wwc_tutorial subdirectory with:
            * items.py -- define structure for scraped data
            * middlewares.py -- processing for the requests and responses
            * pipelines.py -- allow us to apply methods to each item scraped
            * settings.py -- scrapy settings
            * spiders -- these do our scraping!

# Making a Blank Scrapy Spider
1. Let's make the shell of our first spider
    ```
    cd wwc_tutorial
    scrapy genspider meetup_wwc www.meetup.com/Women-Who-Code-DC/
    ```
2. Now we have a meetup_wwc.py file in spiders directory

# Running a Single Scrapy Spider
  ```
  # have to go to the inner directory
  cd wwc_tutorial 
   scrapy crawl <my_spider> -o <my_spider>.json
  ```
