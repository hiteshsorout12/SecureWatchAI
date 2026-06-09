import pickle
import face_recognition

# Load owner encoding
with open(
    "face_recognition_module/encodings/owner.pkl",
    "rb"
) as file:

    owner_encoding = pickle.load(file)

image = face_recognition.load_image_file(
    "face_recognition_module/owner/hitesh.jpg"
)

encodings = face_recognition.face_encodings(image)

if len(encodings) == 0:
    print("No Face Found")
    exit()

unknown_encoding = encodings[0]

result = face_recognition.compare_faces(
    [owner_encoding],
    unknown_encoding
)

if result[0]:
    print("OWNER DETECTED")
else:
    print("INTRUDER DETECTED")