from collections import Counter

from pathlib import Path
import argparse

import face_recognition

from detector.train import train_and_encode_known_faces
from detector.validate import validate
from detector.recognize import recognize_faces

DEFAULT_ENCODINGS_PATH = Path("output/encodings.pkl")
# Showing boundary color and text color for the identified person
BOUNDING_BOX_COLOR = "red"
TEXT_COLOR = "white"

# Create directories if they don't already exist
Path("training").mkdir(exist_ok=True)
Path("output").mkdir(exist_ok=True)
Path("validation").mkdir(exist_ok=True)

# different arguments available for the command line utility
argparser = argparse.ArgumentParser(description="Recognition face from image")
argparser.add_argument("--train", action="store_true", help="If training data provided, enhance the model with new training data")
argparser.add_argument(
    "--validate", action="store_true", help="Validate against the unseen data"
)
argparser.add_argument(
    "--test", action="store_true", help="Given a new image classify the image by testing"
)
argparser.add_argument(
    "-m",
    action="store",
    default="hog",
    choices=["hog", "cnn"],
    help="Which model to use for training: hog (CPU), cnn (GPU)",
)
argparser.add_argument(
    "-f", action="store", help="Image file Path to new face"
)
args = argparser.parse_args()


if __name__ == "__main__":
    if args.train:
        train_and_encode_known_faces(model=args.m)
    if args.validate:
        validate(model=args.m)
    if args.test:
        recognize_faces(image_location=args.f, model=args.m)
