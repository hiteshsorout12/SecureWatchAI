import pickle
import face_recognition


def recognize_face(image_path):

    with open(
        "face_recognition_module/encodings/owner.pkl",
        "rb"
    ) as file:

        owner_encoding = pickle.load(file)

    image = face_recognition.load_image_file(
        image_path
    )

    encodings = face_recognition.face_encodings(
        image
    )

    if len(encodings) == 0:
        return False

    result = face_recognition.compare_faces(
        [owner_encoding],
        encodings[0]
    )

    return result[0]