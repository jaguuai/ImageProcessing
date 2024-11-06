import cv2 as cv
import numpy as np
import gradio as gr

# Filter Functions
def apply_filter(image, filter_type):
    if filter_type == "Gray":
        return cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    elif filter_type == "Sepia":
        sepia_filter = np.array([[0.272, 0.534, 0.131],
                                 [0.349, 0.686, 0.168],
                                 [0.393, 0.769, 0.189]])
        sepia_image = cv.transform(image, sepia_filter)
        return np.clip(sepia_image, 0, 255)
    elif filter_type == "Invert":
        return cv.bitwise_not(image)
    elif filter_type == "Blur":
        return cv.GaussianBlur(image, (15, 15), 0)
    elif filter_type == "Sharpen":
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        return cv.filter2D(image, -1, kernel)
    elif filter_type == "Edge Detection":
        return cv.Canny(image, 100, 200)
    else:
        return image

# Rotation Function
def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv.warpAffine(image, matrix, (w, h))
    return rotated_image

# Brightness and Contrast Adjustment
def adjust_brightness_contrast(image, brightness=0, contrast=0):
    beta = brightness - 128
    alpha = contrast / 128 + 1
    adjusted = cv.convertScaleAbs(image, alpha=alpha, beta=beta)
    return adjusted

# Resize Function
def resize_image(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    resized = cv.resize(image, (width, height), interpolation=cv.INTER_AREA)
    return resized

# Crop Function
def crop_image(image, x, y, width, height):
    return image[y:y+height, x:x+width]

# Gradio function
def process_image(image, filter_type, rotation_angle, brightness, contrast, scale_percent, crop_x, crop_y, crop_width, crop_height):
    image = np.array(image)  # Convert Gradio image to OpenCV format
    filtered_image = apply_filter(image, filter_type)
    rotated_image = rotate_image(filtered_image, rotation_angle)
    adjusted_image = adjust_brightness_contrast(rotated_image, brightness, contrast)
    resized_image = resize_image(adjusted_image, scale_percent)
    cropped_image = crop_image(resized_image, crop_x, crop_y, crop_width, crop_height)
    return cropped_image

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# Advanced Photo Editing Tool")

    with gr.Row():
        image_input = gr.Image(type="pil", label="Upload an Image")

    with gr.Row():
        filter_type = gr.Radio(["Gray", "Sepia", "Invert", "Original", "Blur", "Sharpen", "Edge Detection"], label="Filter Type")
        rotation_angle = gr.Slider(0, 360, step=1, label="Rotation Angle")
        brightness = gr.Slider(0, 255, step=1, label="Brightness")
        contrast = gr.Slider(0, 255, step=1, label="Contrast")
        scale_percent = gr.Slider(10, 200, step=10, label="Scale (%)")
    
    with gr.Row():
        crop_x = gr.Slider(0, 500, step=1, label="Crop X")
        crop_y = gr.Slider(0, 500, step=1, label="Crop Y")
        crop_width = gr.Slider(10, 500, step=1, label="Crop Width")
        crop_height = gr.Slider(10, 500, step=1, label="Crop Height")
    
    image_output = gr.Image(label="Resulting Image")
    gr.Button("Process").click(process_image, inputs=[image_input, filter_type, rotation_angle, brightness, contrast, scale_percent, crop_x, crop_y, crop_width, crop_height], outputs=image_output)

# Launch the demo
if __name__ == "__main__":
    demo.launch()
