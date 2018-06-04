if __name__ == "__main__":

    import numpy
    import compressor
    import image_tools

    matrix = image_tools.load_image("test.txt")

    compressor.get_m43(5,matrix)
