import torch
from torchvision import transforms
from pytorch_fid import fid_score
from PIL import Image

# Define a function to load and preprocess images
def load_image(image_path):
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(256),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])
    image = transform(Image.open(image_path).convert('RGB')).unsqueeze(0)
    return image

# Load the images
image1 = f"/data/wl/dataset/mm-code/code_vqa_image/sphx_glr_bar_colors_001.jpg"
image2 = f"/data/wl/dataset/mm-code/code_vqa_image/sphx_glr_barchart_001.jpg"
#image1 = load_image('image1.jpg')  # Replace 'image1.jpg' with the path to your first image
#image2 = load_image('image2.jpg')  # Replace 'image2.jpg' with the path to your second image

# Calculate FID
fid_value = fid_score.calculate_fid_given_paths([image1, image2], batch_size=50, device='cuda',dims=2048)

print("FID:", fid_value)
