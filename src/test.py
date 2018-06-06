import compressor
import image_tools

image = image_tools.load_image("test.txt")

compressor.csr(5, image)
