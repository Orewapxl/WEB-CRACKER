
## 1. Download the Project as a ZIP from GitHub

- Click the "**Code**" button in the upper-right corner.
- Select "**Download ZIP**" from the dropdown menu.
- Download the ZIP file and extract it to a folder on your computer. 



## 2. Install Required Libraries

After extracting the project, you need to install the required libraries listed in the ```requirements.txt``` file:

**1.** **Open CMD:** Press the Windows key and type "cmd" to open Command Prompt.

**2.** Navigate to the folder where the project files are located. For example, if the extracted folder is in **C:\Users\YourName\Downloads\WebCracker**, use the **cd** command:

```bash 
cd C:\Users\YourName\Downloads\WebCracker
```

**3.** Install the required libraries using the following command:

```bash
pip install -r requirements.txt
```
This will install all the necessary Python libraries, like **requests** and **beautifulsoup4**. If you don't have a **requirements.txt** file, you can manually install the required libraries using:

```bash
pip install requests
pip install beautifulsoup4
```

## 3. Run

Once the libraries are installed, you can run the script. In CMD, navigate to the project folder and execute:

```bash
python webcracker.py

```
