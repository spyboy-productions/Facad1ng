<h4 align="center"> If you find this GitHub repo useful, please consider giving it a star! ⭐️ </h4> 
<img width="100%" align="centre" src="https://github.com/spyboy-productions/Facad1ng/blob/main/image/afa.png" />
<p align="center">
    <a href="https://pepy.tech/projects/facad1ng"><img src="https://static.pepy.tech/badge/facad1ng" alt="PyPI Downloads"></a>
    </a>
</p>

Facad1ng is an open-source URL masking tool designed to help you Hide Phishing URLs and make them look legit using social engineering techniques.

> [!IMPORTANT]
> This tool is a Proof of Concept and is for Educational Purposes Only.

> [!CAUTION] 
> **Please use this responsibly and ethically.**
> <h4> DISCLAIMER </h4> 
> It is possible to use Facad1ng for nefarious purposes. It merely illustrates what adept attackers are capable of. Defenders have a responsibility to consider such attacks and protect their users from them. Using Facad1ng should only be done with the written permission of the targeted parties for legitimate penetration testing assignments.

### Run Online Free On Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/spyboy-productions/Facad1ng/blob/main/Facad1ng.ipynb)

### Example:
```
Your phishing link: https://example.com/whatever

Give any custom URL: gmail.com

Phishing keyword: anything-u-want

Output: https://gamil.com-anything-u-want@tinyurl.com/yourlink

# Get 4 masked URLs like this from different URL-shortener 

```

---

### ⭔ Key Features:

- **URL Masking**: Facad1ng allows users to mask URLs with a custom domain and optional phishing keywords, making it difficult to identify the actual link.

- **Multiple URL Shorteners**: The tool supports multiple URL shorteners, providing flexibility in choosing the one that best suits your needs. Currently, it supports popular services like TinyURL, osdb, dagd, and clckru.

- **Input Validation**: Facad1ng includes robust input validation to ensure that URLs, custom domains, and phishing keywords meet the required criteria, preventing errors and enhancing security.

- **User-Friendly Interface**: Its simple and intuitive interface makes it accessible to both novice and experienced users, eliminating the need for complex command-line inputs.

- **Open Source**: Being an open-source project, Facad1ng is transparent and community-driven. Users can contribute to its development and suggest improvements.

---

<h4 align="center">
  OS compatibility :
  <br><br>
  <img src="https://img.shields.io/badge/Windows-05122A?style=for-the-badge&logo=windows">
  <img src="https://img.shields.io/badge/Linux-05122A?style=for-the-badge&logo=linux">
  <img src="https://img.shields.io/badge/Android-05122A?style=for-the-badge&logo=android">
  <img src="https://img.shields.io/badge/macOS-05122A?style=for-the-badge&logo=macos">
</h4>

<h4 align="center"> 
Requirements:
<br><br>
<img src="https://img.shields.io/badge/Python-05122A?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Git-05122A?style=for-the-badge&logo=git">
</h4>

### ⭔ Git Installation
---

```
git clone https://github.com/spyboy-productions/Facad1ng.git
```
```
cd Facad1ng
```
```
pip3 install -r requirements.txt
```
```
python3 facad1ng.py
```

### ⭔ PYPI Installation : https://pypi.org/project/Facad1ng/
---
```
pip install Facad1ng
```

#### How To Run On CLI:
```
Facad1ng <your-phishing-link> <any-custom-domain> <any-phishing-keyword>
```
```
Example: Facad1ng https://ngrok.com gmail.com accout-login
```
### Python code:
```py
import subprocess

# Define the command to run your Facad1ng script with arguments
command = ["python3", "-m", "Facad1ng.main", "https://ngrok.com", "facebook.com", "login"]

# Run the command
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait for the process to complete and get the output
stdout, stderr = process.communicate()

# Print the output and error (if any)
print("Output:")
print(stdout.decode())
print("Error:")
print(stderr.decode())

# Check the return code to see if the process was successful
if process.returncode == 0:
    print("Facad1ng completed successfully.")
else:
    print("Facad1ng encountered an error.")
```

---

## Contribution:

Contributions and feature requests are welcome! If you encounter any issues or have ideas for improvement, feel free to open an issue or submit a pull request.

#### 😴🥱😪💤 ToDo:

- Fix trycloudflare error which is blocked by TinyURL 

TinyURL not shorting trycloudflare
Solution: don’t use pyshortner. shorten links manually one by one if TinyURL blocks try using different shortener

#### 💬 If having an issue [Chat here](https://discord.gg/ZChEmMwE8d)
[![Discord Server](https://discord.com/api/guilds/726495265330298973/embed.png)](https://discord.gg/ZChEmMwE8d)

### ⭔ Snapshots:
---

<img width="100%" align="centre" src="https://github.com/spyboy-productions/Facad1ng/blob/main/image/Screenshot_2023-09-09_at_1.59.55_AM.png" />

<h4 align="center"> If you find this GitHub repo useful, please consider giving it a star! ⭐️ </h4> 
