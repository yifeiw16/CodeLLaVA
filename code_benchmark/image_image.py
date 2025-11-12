import random
import json
import argparse
import numpy as np
import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr
import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2gray
import numpy as np
import cv2


def get_clip_score(image1, image2, model, processor):
    img1 = Image.open(image1).convert('RGB')
    img2 = Image.open(image2).convert('RGB')
    inputs1=processor(images=img1, return_tensors='pt', padding=True)
    inputs2=processor(images=img2, return_tensors='pt', padding=True)
    embed = []
    for inputs in [inputs1, inputs2]:
        with torch.no_grad():
            vision_outputs = model.vision_model(**inputs)
            image_embeds = vision_outputs[1]
            image_embeds = model.visual_projection(image_embeds)
            image_embeds = image_embeds / image_embeds.norm(dim=-1, keepdim=True)
            embed.append(image_embeds)

    similarity = (100.0 * embed[0] @ embed[1].T).sum(dim=-1)

    return round(similarity.item(),4)

def calculate_ssim(imageA_path, imageB_path):
    imageA = io.imread(imageA_path)
    imageB = io.imread(imageB_path)
    imageA = rgb2gray(imageA)

    imageB = rgb2gray(imageB)

    ssim_index = ssim(imageA, imageB, data_range=imageA.max() - imageA.min())

    return ssim_index

def calculate_psnr(img1_path, img2_path):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    if img1.shape != img2.shape:
        raise ValueError("The shape of two images should be the same")

    psnr = cv2.PSNR(img1, img2)
    return psnr

def main(args):
    
    image1 = f"/data/wl/dataset/mm-code/code_vqa_image/sphx_glr_bar_colors_001.jpg"
    image2 = f"/data/wl/dataset/mm-code/code_vqa_image/sphx_glr_barchart_001.jpg"
    if args.method == "clip":
        model = CLIPModel.from_pretrained("/data/wl/ckpt/clip-vit-large-patch14-336")
        processor = CLIPProcessor.from_pretrained("/data/wl/ckpt/clip-vit-large-patch14-336")
        print(f"CLIP: {get_clip_score(image1,image2,model,processor)}")
    elif args.method == "ssim":
        ssim_value = calculate_ssim(image1, image2)
        print(f"SSIM: {ssim_value}")
    elif args.method == "psnr":
        psnr_value = calculate_psnr(image1, image2)
        print(f"PSNR: {psnr_value}")


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--method", default="clip", type=str) # 
    args = parser.parse_args()
    main(args)