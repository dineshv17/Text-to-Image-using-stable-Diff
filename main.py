import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk

import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

# create a app
app = tk.Tk()
app.title("Text to Image using Stable Diffusion")
app.geometry("532x622")
ctk.set_appearance_mode("dark")
prompt = ctk.CTkEntry(master = app, height=40, width=512, font=("Arial", 20),text_color="black", fg_color="white")
prompt.place(x=10, y=10)

lmain = ctk.CTkLabel(master=app,width=512, height=512)
lmain.place(x=10, y=110) 

button = ctk.CTkButton(master=app,width=120, height=40, font=("Arial", 12),text_color="black", fg_color="white")           
button.place(x=206, y=60)
button.configure(text = "Generate")
app.mainloop()
auth_token = "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"

modelid = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(modelid, version = "fp16",torch_dtype=torch.float16,use_auth_token=auth_token)
device = "cuda"
pipe.to(device)

def generate():
    with autocast(device):
        img = pipe(prompt.get(),guidance_scale=8.5)["image"][0]
    image = ImageTk.PhotoImage(img)
    image.save("output.png")
    lmain.configure(image=image)