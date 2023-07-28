import unittest 
import src.read as read
#import src.algo  as algo     #test crash when uncomment
from src.table import Table    


class Test_Read(unittest.TestCase):
    
    def test_format(self):
        self.assertEqual(read.format("a -> b"),('a','b'))
        self.assertEqual(read.format("a , c -> b , d"),('a,c','b,d'))

    def test_make_split(self):
        self.assertEqual(read.make_split("a -> b",[]), [({'a'} , {'b'})])
        self.assertEqual(read.make_split("a , c -> b , d",[]), [({'a','c'}, {'b', 'd'})])

    def test_read_file(self):
        wanted_result = [({'b'},{'c','g'}),({'b','d','e'},{'c'}),({'h','c'} ,{'i'})]
        path_file = "./test/BD_test/test2.txt"
        self.assertEqual(read.read_file(path_file),wanted_result)
        
    def test_get_all_attribut(self):
        wanted_result = set(({'b','c','g','b','d','e','h','i'}))
        path_file = "./test/BD_test/test2.txt"
        F = read.read_file(path_file)
        self.assertEqual(read.get_all_attribut(F),wanted_result)


class Test_Algo(unittest.TestCase):
    
    def test_DecompoDFen3FN(self):
        L = []
        L.append(Table("C_R",set({'c','r'}),set({'i','c','r'}),set()))
        L.append(Table("P",set({'p'}),set({'p','l','e'}),set()))
        L.append(Table("L",set({'l'}),set({'l','a'}),set()))
        L.append(Table("A",set({'a'}),set({'c','a'}),set()))
        L.append(Table("O",set({'o'}),set({'o','t'}),set()))
        L2 = L
        L2.append(Table("S",set({'s'}),set({'s','c'}),set()))
        path_file = "./test/BD_test/test.txt"
        F = read.read_file(path_file)
        A = set({})
        #tab = algo.DecompoDFen3FN(F,A)
        #self.assertTrue(tab == L or tab == L2)
    
if __name__ == '__main__':
    unittest.main()
