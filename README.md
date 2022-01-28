# Alarm
<br>
This program takes in timestamps as input and plays a random youtube video (url of which is given in urls.txt) at that timestamp
<br /><br />

#### STEPS TO GET STARTED
<br/>
* Clone this github repo to a folder<br />
* Open command prompt from that folder and run - pip install -r requirements.txt<br />
* Once the required files are installed by pip, execute the main.py file - python3 main.py<br />
<br /><br />

**main.py** file is the file that contains the python code. <br />
* It has a function called play() which uses the python selenium library to open google chrome and direct it to the provided URL. The URL in this case is selected by file reading "urls.txt" and picking one random URL from it.<br />

