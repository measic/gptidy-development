import unittest
from unittest import *

class TestTouchcodeStrApi(TestCase):
    def test_happy_path(self):
        coord_string = "[(0,0),(0,3),(3,0),(2,3),(1,3)]"
        touchcode = check_touchcode_str(coord_string, False)
        self.assertEqual(touchcode, 3)
        
    def test_fail_path(self):
        coord_string = "[+++GARBAGE+++]"
        touchcode = check_touchcode_str(coord_string, False)
        self.assertEqual(touchcode, -1)

class TestTouchcodeApi(TestCase):
    def test_arg_is_empty_list(self):
        arg = []
        touchcode = check_touchcode(arg)
        self.assertEqual(touchcode, -1)
        
    def test_arg_is_empty_tuple(self):
        arg = ()
        touchcode = check_touchcode(arg)
        self.assertEqual(touchcode, -1)
        
    def test_arg_is_empty_dict(self):
        arg = {}
        touchcode = check_touchcode(arg)
        self.assertEqual(touchcode, -1)
        
    def test_arg_is_true(self):
        arg = True
        touchcode = check_touchcode(arg)
        self.assertEqual(touchcode, -1)
        
    def test_arg_is_false(self):
        arg = False
        touchcode = check_touchcode(arg)
        self.assertEqual(touchcode, -1)
        
    def test_arg_is_numeric(self):
        arg = 0
        touchcode = check_touchcode(arg)
        self.assertEqual(touchcode, -1)
        
    def test_arg_is_none(self):
        arg = None
        touchcode = check_touchcode(arg)
        self.assertEqual(touchcode, -1)
        
    def test_arg_is_empty_string(self):
        arg = ""
        touchcode = check_touchcode(arg)
        self.assertEqual(touchcode, -1)
        
    def test_arg_is_non_empty_string(self):
        arg = "this string is not empty"
        touchcode = check_touchcode(arg)
        self.assertEqual(touchcode, -1)
        
    def test_simple_case(self):
        arg = [(0, 0),(0, 3),(3, 0),(2, 3)]
        touchcode = check_touchcode(arg, x_mirror=False)
        self.assertEqual(touchcode, 0x2)
        
    def test_happy_path(self):
        for sample in samples[0x80]:
            touchcode = check_touchcode(sample)
            self.assertEqual(touchcode, 0x80)
        
        for sample in samples[0x10]:
            touchcode = check_touchcode(sample)
            self.assertEqual(touchcode, 0x10)
            
    def test_fail_path(self):
        for sample in samples[-1]:
            touchcode = check_touchcode(sample)
            self.assertEqual(touchcode, -1)
                        

class TestStringToCoords(TestCase):
    def test_none(self):
        arg = None
        coords = string_to_coords(arg)
        self.assertEqual(coords, [])
        
    def test_empty(self):
        arg = ""
        coords = string_to_coords(arg)
        self.assertEqual(coords, [])
        
    def test_number(self):
        arg = "3"
        coords = string_to_coords(arg)
        self.assertEqual(coords, [])
        
    def test_list_of_number(self):
        arg = "[1, 2, 3]"
        coords = string_to_coords(arg)
        self.assertEqual(coords, [])
        
    def test_one_coord(self):
        arg = "[(1,1)]"
        coords = string_to_coords(arg)
        self.assertEqual(coords, [(1,1)])
        
    def test_two_coords(self):
        arg = "[(1,1),(178312312,312312312321)]"
        coords = string_to_coords(arg)
        self.assertEqual(coords, [(1,1),(178312312,312312312321)])
        
    def test_more_coords(self):
        arg = "[(1,1),(178312312,312312312321),(2,3),(4,5),(0,0),(400,500)]"
        coords = string_to_coords(arg)
        self.assertEqual(coords, [(1,1),(178312312,312312312321),(2,3),(4,5),(0,0),(400,500)])

    def test_with_whitespaces(self):
        arg = "[(1,1)   ,   (    178312312,			312312312321),   (     2,3),(4,     5),(0,  0)    ,(400,500)]"
        coords = string_to_coords(arg)
        self.assertEqual(coords, [(1,1),(178312312,312312312321),(2,3),(4,5),(0,0),(400,500)])
        
        
class TestPointsToTouchcode(TestCase):
    def test_no_points(self):
        points = []
        touchcode = touchcode_from_points(points)
        self.assertEqual(touchcode, 0)
    
    def test_christmas_tree(self):
        points = [(1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (3, 1), (0, 2), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3)]
        touchcode = touchcode_from_points(points)
        self.assertEqual(touchcode, 0xFFF)
        
    def test_0x18(self):
        touchcode = touchcode_from_points([(1.1, 2.0), (1.8, 2.2)])
        self.assertEqual(touchcode, 0x18)
    
    def test_0x888(self):
        touchcode = touchcode_from_points([(1.1, 2.0), (1.1, 1.2), (2.0, 0.0)])
        self.assertEqual(touchcode, 0x888)
     
    def test_0x444(self):
        touchcode = touchcode_from_points([(0, 2), (0.1, 1.2), (1.0, 0.1)])
        self.assertEqual(touchcode, 0x444)
    
    def test_0x80_precise(self):
        points = [(1, 1)]
        touchcode = touchcode_from_points(points)
        self.assertEqual(touchcode, 0x80)
    def test_0x80_round(self):
        points = [(0.9, 1.1)]
        touchcode = touchcode_from_points(points)
        self.assertEqual(touchcode, 0x80)
    def test_0x80_round(self):
        points = [(1.2, 0.8)]
        touchcode = touchcode_from_points(points)
        self.assertEqual(touchcode, 0x80)
    def test_0x80_no_code(self):
        points = [(1.3, 0.7)]
        touchcode = touchcode_from_points(points)
        self.assertEqual(touchcode, 0)
    def test_no_fail_on_unknown_points(self):
        points = [(70, 100)]
        touchcode = touchcode_from_points(points)
        self.assertEqual(touchcode, 0)
        

class TestNormalization (TestCase):
    def test_normalize_to_simple_system(self):
        coords = (np.array([0,0]), np.array([3,0]), np.array([0,3]) )
        self.assertEqual(norm(coords, np.array([0, 0])), (0, 0))
        self.assertEqual(norm(coords, np.array([1, 0])), (1, 0))
        self.assertEqual(norm(coords, np.array([2, 0])), (2, 0))
        self.assertEqual(norm(coords, np.array([3, 0])), (3, 0))
        
        self.assertEqual(norm(coords, np.array([0, 1])), (0, 1))
        self.assertEqual(norm(coords, np.array([1, 1])), (1, 1))
        self.assertEqual(norm(coords, np.array([2, 1])), (2, 1))
        self.assertEqual(norm(coords, np.array([3, 1])), (3, 1))
        
        self.assertEqual(norm(coords, np.array([0, 2])), (0, 2))
        self.assertEqual(norm(coords, np.array([1, 2])), (1, 2))
        self.assertEqual(norm(coords, np.array([2, 2])), (2, 2))
        self.assertEqual(norm(coords, np.array([3, 2])), (3, 2))
        
        self.assertEqual(norm(coords, np.array([0, 3])), (0, 3))
        self.assertEqual(norm(coords, np.array([1, 3])), (1, 3))
        self.assertEqual(norm(coords, np.array([2, 3])), (2, 3))
        self.assertEqual(norm(coords, np.array([3, 3])), (3, 3))
               
    def test_normalize_to_rotated_system_90(self):
        coords = (np.array([3,3]), np.array([0,3]), np.array([3,0]) )
        self.assertEqual(norm(coords, np.array([0, 0])), (3, 3))
        self.assertEqual(norm(coords, np.array([1, 0])), (2, 3))
        self.assertEqual(norm(coords, np.array([2, 0])), (1, 3))
        self.assertEqual(norm(coords, np.array([3, 0])), (0, 3))
        
        self.assertEqual(norm(coords, np.array([0, 1])), (3, 2))
        self.assertEqual(norm(coords, np.array([1, 1])), (2, 2))
        self.assertEqual(norm(coords, np.array([2, 1])), (1, 2))
        self.assertEqual(norm(coords, np.array([3, 1])), (0, 2))
        
        self.assertEqual(norm(coords, np.array([0, 2])), (3, 1))
        self.assertEqual(norm(coords, np.array([1, 2])), (2, 1))
        self.assertEqual(norm(coords, np.array([2, 2])), (1, 1))
        self.assertEqual(norm(coords, np.array([3, 2])), (0, 1))
 
        self.assertEqual(norm(coords, np.array([0, 3])), (3, 0))
        self.assertEqual(norm(coords, np.array([1, 3])), (2, 0))
        self.assertEqual(norm(coords, np.array([2, 3])), (1, 0))
        self.assertEqual(norm(coords, np.array([3, 3])), (0, 0))
        
    def test_normalize_to_rotated_system_45(self):
        coords = (np.array([3,0]), np.array([3,3]), np.array([0,0]) )
        self.assertEqual(norm(coords, np.array([0, 0])), (0, 3))
        self.assertEqual(norm(coords, np.array([1, 0])), (0, 2))
        self.assertEqual(norm(coords, np.array([2, 0])), (0, 1))
        self.assertEqual(norm(coords, np.array([3, 0])), (0, 0))
        
        self.assertEqual(norm(coords, np.array([0, 1])), (1, 3))
        self.assertEqual(norm(coords, np.array([1, 1])), (1, 2))
        self.assertEqual(norm(coords, np.array([2, 1])), (1, 1))
        self.assertEqual(norm(coords, np.array([3, 1])), (1, 0))
        
        self.assertEqual(norm(coords, np.array([0, 2])), (2, 3))
        self.assertEqual(norm(coords, np.array([1, 2])), (2, 2))
        self.assertEqual(norm(coords, np.array([2, 2])), (2, 1))
        self.assertEqual(norm(coords, np.array([3, 2])), (2, 0))
        
        self.assertEqual(norm(coords, np.array([0, 3])), (3, 3))
        self.assertEqual(norm(coords, np.array([1, 3])), (3, 2))
        self.assertEqual(norm(coords, np.array([2, 3])), (3, 1))
        self.assertEqual(norm(coords, np.array([3, 3])), (3, 0))

    def test_with_samples_for_0x80(self):
        for sample in samples[0x80]:
            coords = np.array(sample)
            om = get_orientation_marks(coords)
            result = norm(om, sample[2])
            self.assertTrue(0.9 <= result[0] <= 1.1)
            self.assertTrue(0.9 <= result[1] <= 1.1)


class TestFindVxVy(TestCase):
    def test_with_standard_coordinates(self):
        o  = np.array([0, 0])
        v1 = np.array([0, 3])
        v2 = np.array([3, 0])
        m = np.array([o,v1,v2])
        
        expected_result = np.array([[0,0],[3,0],[0,3]])
        result = find_vx_vy_new(m)
        self.assertTrue(np.array_equal(expected_result, result))
        
        
    def test_with_standard_coordinates_swapped(self):
        o  = np.array([0, 0])
        v1 = np.array([3, 0])
        v2 = np.array([0, 3])
        m = np.array([o,v1,v2])
        
        expected_result = np.array([[0,0],[3,0],[0,3]])
        result = find_vx_vy_new(m)
        self.assertTrue(np.array_equal(expected_result, result))
        
    def test_with_standard_coordinates_rot90(self):
        o  = np.array([0, 0])
        v1 = np.array([0, -3]) # vx
        v2 = np.array([3, 0])  # vy
        m = np.array([o,v1,v2])
        
        expected_result = np.array([[0,0],[0,-3],[3,0]])
        result = find_vx_vy_new(m)
        self.assertTrue(np.array_equal(expected_result, result))
        
    def test_with_standard_coordinates_rot180(self):
        o  = np.array([0, 0])
        v1 = np.array([0, -3])
        v2 = np.array([-3, 0])
        m = np.array([o,v1,v2])
        
        expected_result = np.array([[0,0],[-3,0],[0,-3]])
        result = find_vx_vy_new(m)
        self.assertTrue(np.array_equal(expected_result, result))
        
    def test_with_standard_coordinates_rot270(self):
        o  = np.array([0, 0])
        v1 = np.array([0, 3])
        v2 = np.array([-3, 0])
        m = np.array([o,v1,v2])
        
        expected_result = np.array([[0,0],[0,3],[-3,0]])
        result = find_vx_vy_new(m)
        self.assertTrue(np.array_equal(expected_result, result))
        
    def test_with_sample(self):
        o = np.array([453, 701])
        v1 = np.array([379, 577])
        v2 = np.array([577,629])
        m1 = np.array([o, v1, v2])
        m2 = np.array([o, v2, v1])
        
        result_m1 = find_vx_vy_new(m1)
        result_m2 = find_vx_vy_new(m1)

        expected_result = np.array([[453,701],[379,577], [577,629]])
        
        self.assertTrue(np.array_equal(result_m1, expected_result))
        self.assertTrue(np.array_equal(result_m2, expected_result))
        
        
class TestOrientationMarks (TestCase):
    def test_get_orientation_marks_simple (self):
        coords = np.array([ [0, 0], [3, 0], [0, 3], [1, 1] ])
        om = get_orientation_marks(coords)
        self.assertTrue(np.array_equal(om[0], coords[0]))
        self.assertTrue(np.array_equal(om[1], coords[1]))
        self.assertTrue(np.array_equal(om[2], coords[2]))
        
    def test_get_orientation_marks_simple_different_order (self):
        coords = np.array([ [1, 1], [0, 3], [3, 0], [0, 0] ])
        om = get_orientation_marks(coords)      
        self.assertTrue(np.array_equal(om[0], coords[3]))
        self.assertTrue(np.array_equal(om[1], coords[2]))
        self.assertTrue(np.array_equal(om[2], coords[1]))
        
    def test_get_orientation_marks_simple_rotate_45(self):
        coords = np.array([ [0, 0], [3, 0], [2, 1], [3, 3] ])
        om = get_orientation_marks(coords)        
        self.assertTrue(np.array_equal(om[0], coords[1]))
        self.assertTrue(np.array_equal(om[1], coords[3]))
        self.assertTrue(np.array_equal(om[2], coords[0]))
        
    def test_get_orientation_marks_simple_rotate_90(self):
        coords = np.array([ [0, 3], [3, 0], [3, 3], [2, 2], [1, 1], [0, 1] ])
        om = get_orientation_marks(coords)        
        self.assertTrue(np.array_equal(om[0], coords[2]))
        self.assertTrue(np.array_equal(om[1], coords[0]))
        self.assertTrue(np.array_equal(om[2], coords[1]))
        
    def test_get_orientation_marks_simple_rotate_135(self):
        coords = np.array([ [0, 0], [0, 3], [3, 3], [1, 2], [1, 1] ])
        om = get_orientation_marks(coords)        
        self.assertTrue(np.array_equal(om[0], coords[1]))
        self.assertTrue(np.array_equal(om[1], coords[0]))
        self.assertTrue(np.array_equal(om[2], coords[2]))
        
    def test_get_orientation_marks_from_samples(self):
        for sample in samples[0x80]:
            coords = np.array(sample)
            om = get_orientation_marks(coords)        
            self.assertTrue(np.array_equal(om[0], coords[3]))
            self.assertTrue(np.array_equal(om[1], coords[1]))
            self.assertTrue(np.array_equal(om[2], coords[0]))

    def test_get_no_orientation_marks_on_garbage(self):
        coords = samples[-1][0]
        om = get_orientation_marks(coords)
        self.assertEqual(om, None)
        
    def test_get_no_orientation_marks_for_empty_points(self):
        coords = []
        om = get_orientation_marks(coords)
        self.assertEqual(om, None)
        
    def test_get_no_orientation_marks_for_non_coordinates(self):
        coords = [1,2,3]
        om = get_orientation_marks(coords)
        self.assertEqual(om, None)
        
    def test_get_no_orientation_marks_for_one_point(self):
        coords = np.array([ [1, 1] ])
        om = get_orientation_marks(coords)
        self.assertEqual(om, None)
        
    def test_get_no_orientation_marks_for_two_points(self):
        coords = np.array([ [1, 1], [1, 2] ])
        om = get_orientation_marks(coords)
        self.assertEqual(om, None)
    
    def test_get_no_orientation_marks_for_three_wrong_points(self):
        coords = np.array([ [0, 0], [3, 0], [0, 2] ])
        om = get_orientation_marks(coords)
        self.assertEqual(om, None)
        

suite = unittest.TestLoader().loadTestsFromModule(TestOrientationMarks())
suite.addTests(unittest.TestLoader().loadTestsFromModule(TestNormalization()))
suite.addTests(unittest.TestLoader().loadTestsFromModule(TestPointsToTouchcode()))
suite.addTests(unittest.TestLoader().loadTestsFromModule(TestStringToCoords()))
suite.addTests(unittest.TestLoader().loadTestsFromModule(TestTouchcodeApi()))
suite.addTests(unittest.TestLoader().loadTestsFromModule(TestTouchcodeStrApi()))
suite.addTests(unittest.TestLoader().loadTestsFromModule(TestFindVxVy()))
unittest.TextTestRunner().run(suite)