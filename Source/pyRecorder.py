import pygame
import cv2
import os
import re

class Recorder:
    def __init__(self, imageName):
        self.shotsTaken = 1
        self.imageName = imageName

    def takeShot(self, screen):
        self.shotsTaken += 1
        filepath = self.imageName + str(self.shotsTaken) + ".png"
        pygame.image.save(screen, filepath)

    def getVideo(self, output_filename, fps=60):
        # Get list of all image files in current directory
        images = [img for img in os.listdir('.') if img.endswith(('.png'))]
        
        # Sort images alphabetically
        images = self.sorted_alphanumeric(images)
        
        # Check if we found any images
        if not images:
            print("No images found in current directory!")
            return
            
        # Read first image to get dimensions
        frame = cv2.imread(images[0])
        height, width, layers = frame.shape
        
        # Create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        video = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))
        
        # Write all frames to video
        for image in images:
            frame = cv2.imread(image)
            video.write(frame)
        
        # Release the video writer
        video.release()
        cv2.destroyAllWindows()

    def sorted_alphanumeric(self, data):
        convert = lambda text: int(text) if text.isdigit() else text.lower()
        alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
        return sorted(data, key=alphanum_key)