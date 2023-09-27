# Meme Generator

A multimedia application to dynamically generate memes, including an image with an overlaid quote.

## Setting up

* Make sure you have [Python](https://www.python.org/downloads/) (3.x) and [pdftotext](https://www.xpdfreader.com/pdftotext-man.html) installed on your system.

* Clone the repository then run the following commands from the root directory:

  ```sh
    python3 -m venv ./venv
    source venv/bin/activate
    pip install -r requirements.txt
  ```

* You have all the required dependencies for the project now. You can use the meme generator by either following ways.

### Command-line Tool

* Run below command to generate random memes

  ```sh
    python3 meme.py
  ```
  
* Additionally, you can specify the command arguments (*--path/-p*, *--body/-b*, *--author/-a*) for more customized memes

  ```sh
    python3 meme.py -p ./_data/photos/dog/xander_1.jpg -b 'Just do it!' -a Xander
  ```

### Flask Server

* Start the `Flask` server by running:

  ```sh
    flask --app app run --host localhost --port 8000
  ```

* The `Flask` server should be up and running on port 8000 now. Open [localhost:8000](http://localhost:8000).

* NOTICE: The default ports are 5000 (or port 3000) are used by other services on MacOS

## Built With

* [Python3](https://www.python.org/) - We all know what it is :)

* [Flask](https://flask.palletsprojects.com/) - Flask is a micro web framework written in Python

## Authors

* Github: [phuc1nguyen](https://github.com/phuc1nguyen)

## Acknowledgements

* [Udacity](https://www.udacity.com/)