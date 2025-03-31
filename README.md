<h1 style="color: #ff9900; font-weight: bold;">HoneyPot_Lite</h1>

### Install

**1) Clone repository.**
`git clone https://github.com/NithinVikas-AV/HoneyPot_Lite.git`

**2) Keygen.**

An RSA key must be generated for the SSH server host key. The SSH host key provides proper identification for the SSH server. Ensure the key is titled `server.key` and resides in the same relative directory to the main program.

`ssh-keygen -t rsa -b 2048 -f server.key`

**3) Run.**

Make sure you run this in a virtual environment and have all the dependencies downloaded in virtual environment.( If not all packages and command given in requirements.txt do check it)

`python3 run_honeypot.py -a 127.0.0.1 -p 2223 -u admin -pw admin --http`

This is to intialise a web honeypot which will give you the link int the terminal.

or 
`python3 run_honeypot.py -a 127.0.0.1 -p 2223 -u admin -pw admin --ssh`

This is to initialise a ssh honeypot which u need to enter bash command shell and type this to command:

`ssh admin@127.0.0.1 -p 2223`

This is to access the server from command shell.

### 🛠️ Environment

 <p> Windows 11 (Use Windows 10 in Virtual Box for Security)</p>
<img src="https://upload.wikimedia.org/wikipedia/commons/8/87/Windows_logo_-_2021.svg" width="30" alt="Windows 11">
 <p>VS code</p>
<img src="https://upload.wikimedia.org/wikipedia/commons/9/9a/Visual_Studio_Code_1.35_icon.svg" width="30" alt="VS Code">  
 <p>PYTHON 3 </p>
<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="30" alt="Python">  
<p>Ubunut 22.04 LTS</p>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/UbuntuCoF.svg/1200px-UbuntuCoF.svg.png" width="30" alt="Ubuntu Logo">

