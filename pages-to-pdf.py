from PIL import Image
import os

# Folder containing the edited PNG images
input_folder = "./pages"  # Change this to your folder path if needed

# Output PDF file name
output_pdf_path = "./Prohlaseni_poplatnika_2025_bezbarve.pdf"

# Get a list of PNG files in numerical order (e.g., page_1.png, page_2.png, ...)
image_files = sorted(
    [f for f in os.listdir(input_folder) if f.endswith(".png")],
    key=lambda x: int(x.split("_")[1].split(".")[0])
)

# Load images and convert to PDF
if image_files:
    images = [Image.open(os.path.join(input_folder, img)).convert("RGB") for img in image_files]
    images[0].save(output_pdf_path, save_all=True, append_images=images[1:])
    print(f"PDF saved as {output_pdf_path}")
else:
    print("No PNG files found in the folder.")
