import unittest
from skimage.data import astronaut
from image_processor import preprocess_image

class TestImageProcessor(unittest.TestCase):

    def test_preprocess_image_shape(self):
        image = astronaut()
        processed = preprocess_image(image)
        self.assertEqual(len(processed), 64*64)

if __name__ == '__main__':
    unittest.main()
