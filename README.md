# iBot-Automation
iBot Automation is a simple cross-platform RPA tool designed to Automate any Business process.
It works in MacOSX, Windows and linux

### Requirements
* Python 3.6 and up.


## iBot Automation Modules
=================================
01. Browser - Automate Browser Activities.
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
Browser automation example
1. Check your Chrome version by typing Chrome://version in your chrome browser
2. Download chromeDriver from [Chrome driver](https://chromedriver.chromium.org/downloads).

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
from iBot.dataBase_activities import Sqlite
pathToDatabase = "c:/sqliteExample.sqlite"
Sqlite= Sqlite(pathToDatabase) 
Data = {"Dg":"Saimon", "Gt":"Manuel"}
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
Get value from cell  example

```python

from iBot.excel_activities import Excel

path = "Path/to/workbook.xlsx"
workbook = Excel(path)
sheets = workbook.GetSheets()
sheet = sheets[0]
cell = "A1"

value = workbook.readCell(cell, sheet)

```

### Files Activities 
Work with files 

```python

from iBot.files_activities import File

path = "Path/to/file"
file = File(path)
#rename file
new_file_name = "file2"
file.rename(new_file_name)
#move file
folder = 'path/to/folder'
file.move(folder)

```


### Folder Activities 
Work with folders 

```python

from iBot.files_activities import Folder
folder = 'path/to/folder'
Carpeta = Folder(folder)
if Carpeta.exists:
    Carpeta.rename("Folder")
    #get list of files
    FileList = Carpeta.fileList
    #get list of subfolders
    FolderList = Carpeta.subFoldersList
    
```

### Image Activities 
Work with Images 

```python
from iBot.files_activities import Image
path = 'path/to/folder'
image = Image(path)
# rotate image horizontally
image.mirrorH()
# rotate image vertically
image.mirrorV()
#crop image
image.crop()
#resize image
image.resize((150,250))
```

### PDF Activities 
Work with PDFs 

```python

from iBot.files_activities import PDF
path = 'path/to/PDF'
pdf = PDF(path)
#get number of pages
print(pdf.pages)
#get pdf info
print(pdf.info)
#Read PDF page 1
text= ''
for i in range(pdf.pages):
    text += pdf.readPage(i) 
print(text)

```


### OCR Activities 
Convert images to text
1. Download latest version of Tesseract from here: [tesseract-ocr](https://github.com/tesseract-ocr/tessdoc/blob/master/Home.md).
2. Download training data from [tesseract trainning data](https://github.com/tesseract-ocr/tessdata).
3. place training data in the following folder ./tesseract/share/tessdata 

```python

from iBot.ocr_activities import OCR
path = 'path/to/tesseract-executable' 
ocr = OCR(path)
#convert image to text 
path = 'path/to/picture'
text = ocr.readPicture(path, lang='eng')
print(text)
#convert pdf to text using OCR
filePath = 'path/to/pdf'
#resize images fo a better recognition
scale= 3
text = ocr.readPdf(filePath, scale= scale, lang='spa')
print(text)

```
### Word Activities 
Work with Word Documents
```python
from iBot.word_activities import Word

#Instance Word Object
document = Word("path_to_word_document")
#add heading to word document
document.addHeading("Lorem Ipsum is simply dummy text of the printing and typesetting industry.", 0)
#add paragraph to word document
paragraph = ''' 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
'''
document.addParagraph(paragraph)
#add picture to word document
document.addPicture('path_to_picture', 300, 300)
table = [('one', 'two', 'three'), (112, 122, 123)]
document.addTable(table)
#read word document
document.read()
#convert word to pdf
document.convertToPdf()
```

### Screen Activities
Find screen elements on the screen, mouse and keyboard activities 
```python
from iBot.screen_activities import Screen
#instance Screen object
screen = Screen()
#find element
element = screen.FindElement('path/to/element.png')
#move mouse to position
screen.moveMouseTo(element)
#click on position
screen.click()
#keyboard activities
text= "Hello world"
screen.write(text)
```

### Robot Activities 
Work with Robot, Queues, Items and Logs in the most simple way

```python
from iBot.robot_activities import Robot
#Instance the Robot Object
RobotName = Robot("name_of_your_robot")

#Create a Queue for your Robot
if not RobotName.findQueuesByName("Name_of_the_queue"):
    Queue1 = RobotName.createQueue("Name_of_the_queue")
else:
    Queue1 = RobotName.findQueuesByName("Name_of_the_queue")[0]

#Add items to your queue
for i in range(0,100):
    Queue1.createItem(i)

#Get items of your queue
while True:
    item = Queue1.getNextItem()
    if not item:
        break
    else:
        item.setItemAsOk()  
    print(item.value,item.status)
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


