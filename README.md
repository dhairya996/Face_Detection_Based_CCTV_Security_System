# Face Detection based CCTV Security System

## Scenario
Current surveillance systems lack
efficient methods for detecting and
managing unauthorized personnel
within areas, leading to potential
security breaches.

Deploying a biometric system like ID
card or iris scanner can be costly and
might not be highly user friendly. So
our motive was to come up with an
idea which allows us to verify people
without much of user involvement.

## Objectives
To develop a streamlined video processing
pipeline integrating frame extraction, face
detection, alignment, extraction, and finally,

performing facial recognition against a pre-
existing database to identify known individuals.

Develop a user-friendly web interface for
administrators to receive alerts on detection of
unfamiliar individuals. Admins can review alerts,
add persons to the database for future
recognition, or dismiss alerts.

## Used Methodology
Input Footage: The process begins with video footage as
input. A directory containing videos to be processed can be
passed to our model.

Extract Frames at a Particular Rate: The video is broken
down into individual frames using OpenCV . The "particular
rate" refers to the number of frames extracted per second,
considering the system's processing speed and system
accuracy.We are extracting a frame at 3 seconds.

Detect Faces: Face detection model scans each frame to
identify human faces. If a face is found, it pinpoints key
facial features or landmarks (e.g., eyes, nose, mouth,
etc.).We are employing RetinaFace Resnet50 model for face
detection and extraction.

Face Restoration: Face images captured in real-world
scenarios often suffer from various issues such as low
resolution, noise, blur, or lighting variations. These
imperfections can negatively impact the accuracy of face
recognition algorithms.
We are employing CodeFormer for restoring the extracted
faces.

CodeFormer: A novel method for blind face restoration that
leverages a learned codebook space and a Transformer-
based code prediction network to enhance the quality of
degraded face images. It aims to reduce uncertainty in
restoration mapping and has shown superior performance
compared to existing methods in blind face restoration
tasks, as well as in tasks such as face color enhancement,
face inpainting, old photo enhancement.

After restoring the extracted faces, the next step involves
passing them through the Facenet Model.
Facenet is a specialized model designed for facial feature
extraction, capable of encoding facial characteristics into a
high-dimensional feature space.
By employing Facenet, the restored faces are transformed
into compact and representative feature vectors, enabling
efficient comparison, recognition, and analysis of facial
attributes.

Match Feature Vector with Pre-existing Vectors in Database
of Recognized Persons: The extracted feature vector is
compared against a database of known persons. Each
person in this database also has a corresponding feature
vector. The system aims to find a close match.
We are using MongoDB Atlas Vector Search Database

The key algorithm behind MongoDB Atlas Vector Search is
approximate k-nearest neighbors (k-NN). Let's break down
what this means:
Approximate k-nearest neighbors (approximate k-NN): This
is a technique used to find the k data points in a dataset
that are closest to a given query point. The "nearest
neighbors" are the data points whose vectors are most
similar to the query vector.

