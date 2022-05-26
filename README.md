# Disecto-Assignment

Create invoices using django

## Prerequisite
Installing wkhtmltopdf
* Visit the [wkhtmltopdf home page](https://wkhtmltopdf.org/).

I used wkhtmltopdf which is open source command line tool to render HTML template into pdf.

### Debian/Ubuntu
```
sudo apt-get install wkhtmltopdf
```
## Usage
```
python manage.py migrate
```
```
python manage.py runserver
```
> Go to http://127.0.0.1:8000/

### Hosted on pythonanywhere

http://rupesh28.pythonanywhere.com/

### My Approach for this assignment

I got data of invoice's attribute using form utility API. and I also made API for counting total cost of products. this API send data of realtime total Bill amount.
when user click on create invoice, whole data store into database using API. User can view and also download invoice. I implemented download pdf feature using pdfkit
library.  Unfortunately wkhtmltopdf did not work on PythonAnywhere. it depends on WebKit, which isn't compatible with our virtualization system of pythonanywhere. but 
amazon web services support wkhtmltopdf webkit. download invoice feature is perfectly work on localhost.
