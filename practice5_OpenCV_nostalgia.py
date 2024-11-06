import cv2 as cv
import numpy as np
import gradio as gr


def nostalgia(image):
    image=np.array(image)
    #cvtColor fonksiyonu, görüntünün renk alanını dönüştürmeye yarar
    gray_image=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    return gray_image

#Gradio arayüzünü oluşturma
with gr.Blocks() as demo:
    gr.Markdown("# Convert image to black and white")
    gr.Markdown("Upload a picture for nostalgia")

    image_input=gr.Image(type="pil", label="Upload Image")
    image_output=gr.Image(type="numpy",label="Result image")

    btn = gr.Button("Convert to Black and White")
    btn.click(fn=nostalgia, inputs=image_input, outputs=image_output)

   

#Gradio arayüzünü başlat
if __name__ == "__main__":
    demo.launch()