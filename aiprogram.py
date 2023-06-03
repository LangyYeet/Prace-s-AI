import cv2
import numpy as np

def get_color_name(R, G, B):
    colors = {'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255),
              'yellow': (255, 255, 0), 'orange': (255, 165, 0),
              'purple': (128, 0, 128), 'pink': (255, 192, 203),
              'brown': (165, 42, 42), 'gray': (128, 128, 128)}
    
    min_dist = float('inf')
    color_name = None
    
    for color, value in colors.items():
        dist = np.sqrt((R - value[0]) ** 2 + (G - value[1]) ** 2 + (B - value[2]) ** 2)
        if dist < min_dist:
            min_dist = dist
            color_name = color
    
    return color_name

def main():
    image = cv2.imread('obrazek.jpg')
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    height, width, _ = image.shape
    
    cv2.imshow('Image', image)
    
    for i in range(height):
        for j in range(width):
            R, G, B = image[i, j]
            color_name = get_color_name(R, G, B)
            print(f'Pixel na souřadnicích ({i}, {j}) je {color_name}.')
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()