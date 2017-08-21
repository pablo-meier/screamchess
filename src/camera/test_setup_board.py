import unittest
import time
import src.camera.setup_board as sb


class TestCenterInference(unittest.TestCase):

    def setUp(self):  # TODO: put in init
        self.num_squares = 8
        self.img_height = 480  # FOr some reason had to be 320 to work for
                               # test dedupe and get centers...bug...

    @unittest.skip
    def test_dedupe2(self):
        input = [(16, 202), (20, 78), (21, 321), (22, 135), (22, 383),
                 (24, 18), (32, 437), (68, 138), (70, 256), (71, 199),
                 (75, 78), (75, 319), (76, 12), (82, 384), (89, 437),
                 (128, 133), (130, 71), (130, 194), (132, 9), (134, 258),
                 (138, 321), (139, 387), (145, 442), (189, 191), (194, 128),
                 (196, 259), (197, 320), (198, 68), (200, 8), (203, 386),
                 (210, 444), (262, 62), (262, 129), (262, 258), (264, 190),
                 (265, 6), (269, 320), (269, 385), (273, 445), (326, 126),
                 (327, 442), (330, 66), (330, 255), (331, 7), (331, 320),
                 (338, 389), (340, 184), (387, 440), (391, 125), (391, 255),
                 (394, 385), (395, 8), (397, 65), (397, 190), (399, 317),
                 (452, 437), (454, 7), (455, 379), (458, 65), (458, 188),
                 (460, 252), (469, 128)]
        output = [None, None, None]
        self.assertEqual(sb.dedupe_centers(input, self.img_height,
                                           self.num_squares), output)

    @unittest.skip
    def test_dedupe1(self):
        """We have an 8x8 grid, on a 480x530-ish size board,
        In this test case, we are missing 3 squares.
        So we want to end up with 61 squares, about 60-65 pixels apart

        14 20 30 70 80 120 130 137 144 186 192 201 208 260 ... 467

        440

        :return:
        """
        input = [(14, 201), (18, 379), (19, 319), (20, 75), (20, 136),
                 (22, 17),
                 (22, 381), (30, 435), (67, 137), (68, 255), (70, 197),
                 (73, 76),
                 (73, 317), (74, 11), (80, 383), (87, 435), (126, 131),
                 (128, 69),
                 (128, 192), (130, 7), (133, 257), (136, 319), (137, 386),
                 (144, 440),
                 (186, 191), (192, 126), (194, 257), (196, 66), (196, 319),
                 (198, 4),
                 (201, 384), (208, 442), (260, 127), (260, 257), (261, 60),
                 (262, 188),
                 (263, 2), (267, 383), (268, 317), (271, 443), (324, 124),
                 (328, 64),
                 (328, 440), (329, 3), (329, 317), (330, 253), (336, 387),
                 (339, 183),
                 (385, 439), (389, 123), (391, 383), (393, 5), (395, 63),
                 (396, 188),
                 (396, 384), (397, 315), (448, 437), (452, 5), (453, 377),
                 (456, 186),
                 (457, 64), (459, 251), (467, 126)]
        output = {25: [17, 75, 136, 201, 319, 380, 435],
                  81: [11, 76, 137, 197, 255, 317, 383, 435],
                  139: [7, 69, 131, 192, 257, 319, 386, 440],
                  203: [4, 66, 126, 191, 257, 319, 384, 442],
                  268: [2, 60, 127, 188, 257, 317, 383, 443],
                  335: [3, 64, 124, 183, 253, 317, 387, 440],
                  395: [5, 63, 123, 188, 315, 383, 439],
                  462: [5, 64, 126, 186, 251, 377, 437]}
        self.assertEqual(sb.dedupe_centers(input, self.img_height,
                                           self.num_squares), output)

    @unittest.skip
    def test_infer_missing(self):
        input = {25: [17, 75, 136, 201, 319, 380, 435],
                 81: [11, 76, 137, 197, 255, 317, 383, 435],
                 139: [7, 69, 131, 192, 257, 319, 386, 440],
                 203: [4, 66, 126, 191, 257, 319, 384, 442],
                 268: [2, 60, 127, 188, 257, 317, 383, 443],
                 335: [3, 64, 124, 183, 253, 317, 387, 440],
                 395: [5, 63, 123, 188, 315, 383, 439],
                 462: [5, 64, 126, 186, 251, 377, 437]}
        output = {139: [7, 69, 131, 192, 257, 319, 386, 440],
                  203: [4, 66, 126, 191, 257, 319, 384, 442],
                  268: [2, 60, 127, 188, 257, 317, 383, 443],
                  462: [5, 64, 111, 126, 186, 251, 377, 437],
                  335: [3, 64, 124, 183, 253, 317, 387, 440],
                  81: [11, 76, 137, 197, 255, 317, 383, 435],
                  25: [3, 17, 75, 136, 201, 319, 380, 435],
                  395: [5, 50, 63, 123, 188, 315, 383, 439]}
        self.assertEqual(sb.insert_centers(input, self.img_height,
                                           self.num_squares), output)

    def test_setup_board(self):
        output = {139: [7, 69, 131, 192, 257, 319, 386, 440],
                  203: [4, 66, 126, 191, 257, 319, 384, 442],
                  268: [2, 60, 127, 188, 257, 317, 383, 443],
                  462: [5, 64, 111, 126, 186, 251, 377, 437],
                  335: [3, 64, 124, 183, 253, 317, 387, 440],
                  81: [11, 76, 137, 197, 255, 317, 383, 435],
                  25: [3, 17, 75, 136, 201, 319, 380, 435],
                  395: [5, 50, 63, 123, 188, 315, 383, 439]}
        start = time.time()
        centers = sb.get_square_centers_from_board(
            'src/camera/captured_images/blue_squares.png',
            8, show_images=True)
        end = time.time()
        print('Got centers in ', end - start, ' seconds')
        self.assertEqual(centers, output)

if __name__ == '__main__':
    unittest.main()