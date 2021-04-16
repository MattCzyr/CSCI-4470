from PIL import Image
from PIL import ImageOps

for name in ['tshirt', 'shirt', 'pants']:
    image = Image.open(name + '.png')
    image = ImageOps.grayscale(image)
    image = image.resize((28, 28))
    # Scaling and inverting happens in checkpoint3.py, no need to do it now
    image.save(name + '-prepared.png')
