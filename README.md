# Face recognition system
## This program can take an image and check if it's in "faces" directory then you're welcome. Else - get out of here!
### Installing packages(Linux)
sudo apt-get install python3
pip install face_recognition
### How to use program?
First of all you can type 'python3 main.py -i' for info.
<br>
'python3 main.py -a images/example.jpg example' saves an image of example to an faces dir with name 'example'
<br>
'python3 main.py -c images/example2.jpg' check is there a face in the example2 in the catalog of 'faces' and if it is - you are welcome! Otherwise - get out of here!
<br>
If the program can't recognise the face - you'll get the text 'face not found'

