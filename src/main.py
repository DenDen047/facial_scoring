import os
import face_recognition


DATA_DIR = '/data'


def main():
    image = face_recognition.load_image_file(os.path.join(DATA_DIR, 'obama-240p.jpg'))
    face_landmarks_list = face_recognition.face_landmarks(image)
    print(face_landmarks_list)

if __name__ == "__main__":
    main()