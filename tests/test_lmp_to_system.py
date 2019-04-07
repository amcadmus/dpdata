import os
import numpy as np
import unittest
from context import system
from poscars.poscar_ref_oh import TestPOSCARoh        

class TestLmp(unittest.TestCase, TestPOSCARoh):
    
    def setUp(self): 
        self.system = system.System()
        self.system.from_lammps_lmp(os.path.join('poscars', 'conf.lmp'), 
                                    type_map = ['O', 'H'])
        
if __name__ == '__main__':
    unittest.main()
    