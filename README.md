Home Task: Phishing Email Detection System & Gmail Add-on
By:Bar Kobi
Date:2025-06-19

1. Introduction and Project Objective
This project develops a rule-based phishing email detection system and integrates it as a Gmail Add-on for on-demand scanning. The solution includes Python components for potential detection logic and a Gmail Add-on for the user interface.

2. System Architecture
a. Phishing Detection System (Python):
The Python files (email_utils.py, phishing_checker.py, main.py) constitute the core detection logic. main.py demonstrates its operation with example emails.

b. Gmail Add-on for Scanning (Google Apps Script):
The Apps Script code implements the Gmail Add-on, providing a user interface within Gmail. The primary detection logic is implemented directly in the Apps Script code for ease of demonstration and standalone operation.

3. How the Detection Model Works (in Gmail Add-on)
The detection model uses heuristics to assign a "Phishing Score" to an email, which determines the final classification (Safe, Suspicious, Phishing).

Phishing Score:

≥3
 points: "Phishing"

≥1
 points: "Suspicious"

0
 points: "Safe"

Implemented Heuristics:

Urgent or Suspicious Language: Checks for phrases like "urgent", "verify your account", "won", "prize". (2 points).

Links with Suspicious Keywords: Checks for words like "login", "payment", "security" in links. (2 points).

Domain Mismatch in Links: Compares sender's domain to link domains. (3 points).

Shortened URL Detection: Identifies common shortened links. (1 point).

"Machine Learning" (Mark Sender as Trusted):

This button marks a sender's domain as trusted, stored privately for the user.

Impact: Emails from a trusted sender will be classified as "Safe" if no other suspicious indicators are present. If indicators exist, they will be classified as "Suspicious" or "Phishing" with a high phishing score, but noted as coming from a trusted sender.

"Unusual Sender Address": This reason does not add points and appears only if the overall email is suspicious due to other factors.

4. Gmail Add-on Installation and Usage Instructions
Open Apps Script editor: Go to script.google.com.

Create a new project and paste the code from gmail_phishing_scanner_addon.gs.

Configure Manifest: Ensure "Show manifest in editor" is checked, paste content from appsscript.json into the editor's appsscript.json file.

Save the project.

Run Add-on (for Authorization): Select getContextualAddOn in the Run dropdown and execute. Authorize permissions (via "Advanced" > "Go to...").

Refresh Gmail: Close and reopen your Gmail tab.

Use Add-on: Open an email, find "Phishing Scanner" in the right sidebar.

5. Python Files (for Standalone Testing)
The Python files demonstrate the detection logic.

Ensure email_utils.py, phishing_checker.py, main.py are in the same directory.

Run python main.py in the terminal.

6. Limitations and Future Improvements
Live Python Backend Integration: True integration with Python cloud services.

More Advanced Link Analysis: Shortened URL expansion (requires external API), Typosquatting/Homoglyphs detection.

Attachment Analysis.

Advanced UI for Trusted Sender Management.

Loading Indicators during scanning.

7. Google Apps Script Project Link
[Paste the link you received from sharing your project here :https://script.google.com/d/1XQDyTrscsOfYUIpRK95UUM15G_PeJoRvFO6wO3_2gD1RIgUUyKme_Qdz/edit?usp=sharing]