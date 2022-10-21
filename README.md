# Identifying-criminals-using-AI

## Introduction

Every day thousands of crimes were happening around the world. Most of these were committed by people who have criminal history. Every crime involves some suspicious activity which goes unreported due to insecurities of the crime witness. In this project we are going to create an application where a normal citizen can report a suspicious activity without loosing their anonymity

A suspicious activity will be reported by a citizen along with the location, description and a photo of the criminal. All the criminal details are available in the police database along with the photos. Now the photo uploaded by the citizen will be matched with the photos in the database through the face matching algorithm that we are going to implement which will be described in the proposed methodology section.

## Proposed methodology

1. Multiple photos of a criminal are present in the database. Data augmentation is done to produce diversities of the criminal photo.
2. Data augmentation includes horizontal flip, changing contrast of images and added noise to the images.
3. For each image 5 more augmented images will be produced.
4. For each criminal an ID and multiple face encodings are created [face encodings of actual and augmented images].
5. A face encoding is basically a way to represent the face using a set of 128 computer-generated measurements. Two different pictures of the same person would have similar encoding and two different people would have totally different encoding.
6. As face encoding has 128 attributes using PCA number of attributes will be reduced
7. A classification model (Hoeffding Trees) will be retrieved from the database and partially fitted with the current criminal’s data and again will be stored in the database.[This will be done on trigger basis]
8. When a suspicious activity is reported the suspect photo will be encoded, and the classification model in the database classifies who the criminal might be.
9. We will set a threshold value and when the prediction probability of the model is less than threshold then we conclude that the criminal data is not available in the database.

## Dataset
The framework will be tested using ORL database. Olivetti Research Laboratory (ORL) face dataset was used in the context of a face recognition project carried out in collaboration with the Speech, Vision and Robotics Group of the Cambridge University Engineering Department.
The dataset consists of ten different images of each of 40 distinct subjects. For some subjects, the images were taken at different times, varying the lighting, facial expressions (open / closed eyes, smiling / not smiling) and facial details (glasses / no glasses).
