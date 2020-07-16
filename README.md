# iBot-Automation
iBot Automation is a simple cross-platform RPA tool designed to Automate any Business process.
It works in MacOSX, Windows and linux

### Requirements
* Python 3.6 and up.


## iBot Automation Modules
=================================
01. Browser - Automate Browser Activites.
02. DataBase - Create manage and modify databases.
03. Email - Read and send Emails.
04. Excel - Create, read and modify Excel workbooks.
05. Files - Work with Files, folders, images and PDFs.
06. OCR - Convert images to text.
07. Robot -  Manage Robots, Queues and items.
08. System - Work with process and system activities.
09. Word - Create, edit and modify Word documents.
10. Screen - Find bitmap elements on screen, mouse and keyboard control (move, drag, click and type). 


### Installation

First, see if a binary wheel is available for your machine by running:

    $ pip install iBotAutomation

Another option is to build from the latest source on the GitHub repository:

    $ git clone https://github.com/ecrespo66/iBot-Automation.git
    $ cd iBot
    $ make
    $ make install


### Browser Automation

1. Check your Chrome version by typing "Chrome://version" in your chrome browser
2. Download chromeDriver from  [Chrome driver](https://chromedriver.chromium.org/downloads).

```python
from iBot.browser_activities import * 
# undetectable=True to make browser undetectable to AntiBot systems
PathDriver = "path_to_chrome_driver.exe"
Browser = ChromeBrowser(PathDriver,undetectable=True)
Browser.open()
Browser.get('https://google.com')

```

### DataBase Activities
Insert data example
```python
from iBot.dataBabase_activities import Sqlite

pathToDatabase = "c:/sqliteExample.sqlite"
Sqlite= Sqlite(pathToDatabase) 
Data = {"Dg":"Saimon","Gt":"Manuel"}
tableName = "random"
Sqlite.Insert(tableName,Data)

```

### Email Automation 
Read Emails example **enable less secure apps in your email account settings
```python
from iBot.email_activities import Mail

email = 'mail@mail.com'
password = '*******'
Mail = Mail(email, password)

mails= Mail.fetchBox()

for mail in mails:
    print(mail.subject)

```
### Excel Automation 
Get value from cell  
```python
from iBot.excel_activities import Excel

path = "Path/to/workbook.xlsx"
workbook = Excel(path)
sheets = workbook.GetSheets()
sheet = sheets[0]
cell = "A1"

value = workbook.readCell(cell, sheet)

```

## Contributing

If you are interested in this project, please consider contributing. Here are a
few ways you can help:

- [Report issues](https://github.com/ecrespo66/iBot-Automation/issues).
- Fix bugs and [submit pull requests](https://github.com/ecrespo66/iBot-Automation/pulls).
- Write, clarify, or fix documentation.
- Suggest or add new features.

## License

This project is licensed under either the [Apache-2.0](LICENSE-APACHE) or
[MIT](LICENSE-MIT) license, at your option.

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall be
dual licensed as above, without any additional terms or conditions.


