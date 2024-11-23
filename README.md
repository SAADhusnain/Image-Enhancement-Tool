# Image Enhancement Tool
============================================================================================

**A Python-based Image Enhancement Utility**

Utilize the power of OpenCV and Pillow to enhance your images with ease. This tool provides a simple, efficient way to sharpen, denoise, and adjust the brightness and contrast of your images.

### Key Features

* **Image Sharpening**: Enhance image details using a custom kernel
* **Noise Reduction**: Apply fast NL means denoising to reduce unwanted noise
* **Brightness & Contrast Adjustment**: Fine-tune your image's brightness and contrast levels
* **Additional Denoising Filters**: Compare results using Gaussian Blur, Median Blur, and Bilateral Filter

### Requirements

* **Python 3.8+**: Ensure you have the latest Python version installed
* **OpenCV (`opencv-python`)**: For computer vision and image processing
* **Pillow (`Pillow`)**: For additional image processing capabilities
* **NumPy (`numpy`)**: For efficient numerical computations

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SAADhusnain/ImageEnhancementTool.git

2. **Navigate to the Project Directory**: 
   ```bash
   cd ImageEnhancementTool

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

### **Usage**

**Run the Enhancement Script**:
```bash
python enhance_image.py yourimage.jpg image_enhanced
```
yourimage.jpg:  **Input image file**

image_enhanced:  **Output file prefix (multiple outputs will be generated with suffixes)**


## API Documentation
### Functions
 1. load_image_cv(path): Load an image using OpenCV
 2. load_image_pil(path): Load an image using Pillow
 3. save_image_cv(image, path): Save an image using OpenCV
 4. save_image_pil(image, path): Save an image using Pillow
 5. sharpen_image(image): Apply sharpening filter to the image
 6. reduce_noise(image): Reduce noise in the image using fast NL means denoising
 7. adjust_brightness_contrast(image, brightness, contrast): Adjust image brightness and contrast
 8. apply_denoising_filters(image): Apply additional denoising filters (Gaussian Blur, Median Blur, Bilateral Filter)









