import face_recognition
import pickle

image = face_recognition.load_image_file(
    "face_recognition_module/owner/hitesh.jpg"
)

encodings = face_recognition.face_encodings(image)

if len(encodings) == 0:
    print("No Face Found")
    exit()

with open(
    "face_recognition_module/encodings/owner.pkl",
    "wb"
) as file:

    pickle.dump(
        encodings[0],
        file
    )

print("Owner Registered Successfully")