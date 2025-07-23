import cv2 # pip install opencv-python
import matplotlib.pyplot as plt

def convert_colored_to_gray(colored_image):
    gray_image = cv2.cvtColor(colored_image, cv2.COLOR_BGR2GRAY)
    return gray_image

def convert_gray_to_binary(gray_image, treshold_value=127):
    _, binary_image = cv2.threshold(gray_image, treshold_value, 255, cv2.THRESH_BINARY)
    return binary_image

def display_images(colored_image, gray_image, binary_image):
    plt.figure(figsize=(15, 5)) 

    plt.subplot(1, 3, 1) # (rows, columns, panel number)
    plt.imshow(cv2.cvtColor(colored_image, cv2.COLOR_BGR2RGB)) # OpenCV loads images in BGR format, but Matplotlib expects RGB.
    plt.title('Original Color Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(gray_image, cmap='gray') # Use 'gray' colormap for grayscale display
    plt.title('Grayscale Image')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(binary_image, cmap='gray') # Use 'gray' colormap for black and white display
    plt.title('Binary Image')
    plt.axis('off')

    plt.tight_layout() 
    plt.show()
     
if __name__ == "__main__":
    colored_image_path = 'input\\road.jpg'
    colored_image = cv2.imread(colored_image_path)

    gray_image = convert_colored_to_gray(colored_image)

    treshold_value = 127 #Pixels with intensity above the threshold become white (255), and pixels below or equal to the threshold become black (0).
    binary_image = convert_gray_to_binary(gray_image, treshold_value)

    display_images(colored_image, gray_image, binary_image)
      
