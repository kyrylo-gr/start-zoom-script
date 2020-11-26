# Start zoom script
This is a script that runs a zoom lecture depending on your schedule

If you are as tired as I am of opening a excel with all links to your lectures before each zoom lecture. This script will save you a few clicks.

# How this work?
1) Python file `zoom_start.py` looks in `data.py` if you have lecture running
2) `data.py` is example of data file with `lectures` as a array of your lectures in format
`[weekdate, start hour, end hour, link]`
3) `Lecture now.bat` simple bat file (obviously for Windows) with command `python zoom_start.py`

# What you can do?
* Your can create a link of `Lecture now.bat` in `%AppData%\Roaming\Microsoft\Windows\Start Menu\Programs\[subfolder if you want]`, in this way you can tap `win`, type `[name of your link file]` and open script
* You can set a shortcut for this script in Properties menu. And so open script by `ctrl+alt+l` (for example)