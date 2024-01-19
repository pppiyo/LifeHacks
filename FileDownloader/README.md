# About
A small program that helps batch download files on the internet by simply feeding the url of the parent page to the command line.

# Motivation
Finding all slides listed on a webpage waiting for me to download one by one, I figured I was too lazy for this.<br>
Hence did some googling and tweaked a few code to realize this function.

# How to run
1. Open terminal under FileDownloader.py file folder.
2. Type the following command and hit enter: "python3 FileDownloader.py".
3. Follow the directions of the program (basically just provide the url that leads to the list of files and download will start immediately).

# Note
1. This program currently only supports downloading pdf and ppt files (others may be added later).
2. For bug-free experiences, preferably your files are supposed to be in situations like this:
<img width="458" alt="webpage demo" src="https://github.com/pppiyo/LifeHacks/assets/31379013/8c42e7c3-f614-4b19-939b-f970c632c15f">

  That is to say, 1) you have a parent link which leads you to see a page like this; 2) each file has its own link provided.<br><br>
3. Outcome will be like the following. You should be able to find the files in the folder where FileDownloader.py is.<br>

   <img width="1017" alt="code effect" src="https://github.com/pppiyo/LifeHacks/assets/31379013/00905cc5-6990-4151-8446-ff3792d78252">
