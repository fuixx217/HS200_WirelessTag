# HS200_WirelessTag
Repo to house code for controlling TP Link HS200 by responding to emailed alarms from WirelessTag Temperature sensors.

## Scenario
I installed wirelesstag sensors to monitor temperature in various parts of my house to see where I had hot and cold spots.  I also installed a wood stove insert into my fireplace box, and wanted to trigger ThruWall fans to turn on when the temperature sensor in that room reached a certain temperature (74 in my case), and then turn off when the temperature dropped back to normal (The wirelesstag device have a monitor feature where you can set the normal range).  The wirelesstag devices can also send emails or tweets.

## Layout
1. Got a raspberry pi 3 with wifi, and installed Respbian OS.
2. Found these other repos and forked them to use on my own:
   a. https://github.com/abhishekchhibber/Gmail-Api-through-Python (to monitor and interact with a gmail mailbox where I am sending wirelesstag alarms)
      i. There are steps necessary to get API access working; notably, a client secret json file from your gmail account.
   b. https://github.com/GadgetReactor/pyHS100 (to interact with my TP-Link HS200 wifi switch; hard-coded IP for that device on my router)
   c. https://github.com/click-contrib/click-datetime (needed for the gmail repo referenced above to work)
3. Modified the "gmail read py" file to look for subjects of unread messages, and then called a separate python files to turn the switch on or off.

## Installation
1. Install Raspbian on Raspberry Pi 3.  Copy "NOOBS" to the Micro SD card if you are starting from a blank SD card.  (There are kits available that include NOOBS lite already on the micro SD).
2. Configure Python 3 to be used (pre-requisite for gmail)
   From CLI, type "python --version" to determine which version is currently in use as per PATH environment variable.
   If necessary, find the 3.5+ python file in /usr/bin/ and replace python with that file.
      Example: mv python python2.7.13
               mb python3.5 python
               python --version
                  * this changed my version output to 3.5.3 (you could have higher installed)
3. Install remaining gmail pre-requisites:
   a. pip install --upgrade google-api-python-client
	b. pip install BeautifulSoup4
	c. pip install python-dateutil
   * Note about these, they will go to the old version of python directory if you forget/omit step 2 above, so you may need to repeat this if you try to run these before confirmation of python 3 being used
4. Clone click-datetime repo and install
   a. git clone https://github.com/click-contrib/click-datetime.git
   b. sudo python setup.py install
   c. After install, it is safe to delete the clone of the repo.
5. Clone pyHS100 repo and install
   a. git clone https://github.com/GadgetReactor/pyHS100.git


