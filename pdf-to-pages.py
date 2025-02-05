from pdf2image import convert_from_path

# Input PDF path
pdf_path = "./Prohlaseni_poplatnika_2025.pdf"

# Convert PDF to images
images = convert_from_path(pdf_path, dpi=300)  # Adjust DPI if needed

# Save each page as PNG
for i, image in enumerate(images):
    image.save(f"page_{i+1}.png", "PNG")

print("PDF pages converted to PNG successfully!")
