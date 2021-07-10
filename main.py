import face_recognition
import PIL
import sys
import os
# python3 main.py -a images/123.jpg Obama
# python3 main.py -c images/456.jpg

FACES_DIR = 'faces'

def extract_face(path):
    load = face_recognition.load_image_file(path)
    locations = face_recognition.face_locations(load)
    i = 0
    for location in locations:
        top, right, bottom, left = location
        face_img = load[top:bottom, left:right]
        pil_img = PIL.Image.fromarray(face_img)
        pil_img.save(f"faces/face{i}_{sys.argv[3]}.jpg")
        i += 1
        


def compare(path):
    try:
        image1 = face_recognition.load_image_file(path)
        image1_encodings = face_recognition.face_encodings(image1)[0]
    except IndexError:
        print("Face not found")
        exit()
    members = []
    for filename in os.listdir(FACES_DIR):
        f = os.path.join(FACES_DIR, filename)
        if os.path.isfile(f):
            
            image2 = face_recognition.load_image_file(f)
            image2_encodings = face_recognition.face_encodings(image2)[0]

            result = face_recognition.compare_faces([image1_encodings], image2_encodings)
            if result[0]:
                members.append(1)
    if 1 in members:
        print("Welcome!")
    else:
        print("Get out of here!")
            
def main():
    if sys.argv[1] == "-i":
        print("Hello! Welcome to comparing faces system!\n")
        print('-a\t- Appending image to directory of confirmed faces.')
        print('-c\t- Check if given image is confirmed.\n')
        print('Examples:\n')
        print('\tpython3 main.py -a images/123.jpg Obama')
        print('\tpython3 main.py -c images/456.jpg')
    if sys.argv[1] == '-a':
        extract_face(sys.argv[2])
    if sys.argv[1] == '-c':
        compare(sys.argv[2])
if __name__ == "__main__":
    main()