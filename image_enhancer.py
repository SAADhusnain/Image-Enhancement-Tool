import cv2
from PIL import Image, ImageEnhance
import numpy as np

# Load the image using OpenCV
def load_image_cv(path):
    return cv2.imread(path)

# Load the image using Pillow
def load_image_pil(path):
    return Image.open(path)

# Save the image using OpenCV
def save_image_cv(image, path):
    cv2.imwrite(path, image)

# Save the image using Pillow
def save_image_pil(image, path):
    image.save(path)

# Sharpen the image
def sharpen_image(image):
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    return cv2.filter2D(image, -1, kernel)

# Reduce noise in the image
def reduce_noise(image):
    return cv2.fastNlMeansDenoisingColored(image, None, 6, 6, 7, 21)

# Adjust brightness and contrast
def adjust_brightness_contrast(image, brightness=0, contrast=0):
    brightness = int(brightness)
    contrast = int(contrast)
    
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow)/255
        gamma_b = shadow
            
        buf = cv2.addWeighted(image, alpha_b, image, 0, gamma_b)
        cv2.putText(buf, f"Brightness:{brightness}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        image = buf.copy()
        
    if contrast != 0:
        if contrast > 0:
            alpha_c = 131+(contrast*127)
            gamma_c = 127-(contrast*127)
        else:
            alpha_c = 127+(contrast*127)
            gamma_c = 127-(contrast*127)
        alpha_c /= 127 
        gamma_c /= 127
        
        buf = cv2.addWeighted(image, alpha_c, image, 0, gamma_c)
        cv2.putText(buf, f"Contrast:{contrast}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        image = buf.copy()
        
    return image

# Apply additional denoising filters (for comparison)
def apply_denoising_filters(image):
    # Gaussian Blur
    gaussian = cv2.GaussianBlur(image, (5, 5), 0)
    
    # Median Blur
    median = cv2.medianBlur(image, 5)
    
    # Bilateral Filter
    bilateral = cv2.bilateralFilter(image, 5, 50, 50)
    
    return gaussian, median, bilateral

# Main function to enhance the image
def enhance_image(image_path, output_path):
    image = load_image_cv(image_path)
    
    # Sharpen the image
    sharpened = sharpen_image(image)
    save_image_cv(sharpened, f"{output_path}_sharpened.jpg")
    
    # Reduce noise
    denoised = reduce_noise(image)
    save_image_cv(denoised, f"{output_path}_denoised.jpg")
    
    # Adjust brightness and contrast
    adjusted = adjust_brightness_contrast(image, brightness=50, contrast=50)
    save_image_cv(adjusted, f"{output_path}_brightness_contrast.jpg")
    
    # Apply additional denoising filters
    gaussian, median, bilateral = apply_denoising_filters(image)
    save_image_cv(gaussian, f"{output_path}_gaussian_blur.jpg")
    save_image_cv(median, f"{output_path}_median_blur.jpg")
    save_image_cv(bilateral, f"{output_path}_bilateral_filter.jpg")

# Usage
image_path = "yourimage.jpg"
output_path = "image_enhanced"
enhance_image(image_path, output_path)
