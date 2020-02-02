# -*- coding: utf-8 -*-

# Copyright 2008 - 2020 Joseph J. Simpson GPL-3.0-or-later
#   This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#

import artdata
import standard_matrix as sm
import numpy as np
np.set_printoptions(threshold=np.inf)

# Standard Example 9 x 9 - 20 percent 
ms1 = artdata.SME_CD_9_20P_NER_DO_V001
vs1 = artdata.SME_CD_9_20P_NER_DO_VS_V001
os1 = artdata.SME_CD_9_20P_NER_DO_OS_V001

# Standard Example 9 x 9 - 25 percent 
ms2 = artdata.SME_CD_9_25P_NER_DO_V001
vs2 = artdata.SME_CD_9_25P_NER_DO_VS_V001
os2 = artdata.SME_CD_9_25P_NER_DO_OS_V001

# Standard Example 9 x 9 - 30 percent 
ms3 = artdata.SME_CD_9_30P_NER_DO_V001
vs3 = artdata.SME_CD_9_30P_NER_DO_VS_V001
os3 = artdata.SME_CD_9_30P_NER_DO_OS_V001

# Standard Example 9 x 9 - 35 percent 
ms4 = artdata.SME_CD_9_35P_NER_DO_V001
vs4 = artdata.SME_CD_9_35P_NER_DO_VS_V001
os4 = artdata.SME_CD_9_35P_NER_DO_OS_V001

# Standard Example 9 x 9 - 40 percent 
ms5 = artdata.SME_CD_9_40P_NER_DO_V001
vs5 = artdata.SME_CD_9_40P_NER_DO_VS_V001
os5 = artdata.SME_CD_9_40P_NER_DO_OS_V001

# Standard Example 9 x 9 - 45 percent 
ms6 = artdata.SME_CD_9_45P_NER_DO_V001
vs6 = artdata.SME_CD_9_45P_NER_DO_VS_V001
os6 = artdata.SME_CD_9_45P_NER_DO_OS_V001

# Standard Example 9 x 9 - 50 percent 
ms7 = artdata.SME_CD_9_50P_NER_DO_V001
vs7 = artdata.SME_CD_9_50P_NER_DO_VS_V001
os7 = artdata.SME_CD_9_50P_NER_DO_OS_V001


def test_valid_standard_matrix_20p():
    assert sm.valid_standard_matrix_20p(ms1, vs1, os1) == True
    

def test_valid_marking_space_20p():
    array_1 = np.array(sm.valid_marking_space_20p(ms1, vs1, os1))
    array_2 = np.array(
    [[0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,1],\
     [1,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0],[0,1,0,1,0,0,0,0,0],\
     [0,0,0,0,0,0,0,1,0],[0,0,1,1,0,0,1,0,0],[0,1,1,0,0,0,0,0,0]] )
    
    assert np.array_equal(array_1, array_2)
    
def test_valid_value_space_20p():
    array_3 = np.array(sm.valid_value_space_20p(ms1, vs1, os1))
    array_4 = np.array(
    [[0,1,2,3,4,5,6,7,8],[1,0,1,2,3,4,5,6,7],[2,1,0,1,2,3,4,5,6],\
     [3,2,1,0,1,2,3,4,5],[4,3,2,1,0,1,2,3,4],[5,4,3,2,1,0,1,2,3],\
     [6,5,4,3,2,1,0,1,2],[7,6,5,4,3,2,1,0,1],[8,7,6,5,4,3,2,1,0]])
    
    assert np.array_equal(array_3, array_4)
        
    
    
def test_valid_outcome_space_20p():
    array_5 = np.array(sm.valid_outcome_space_20p(ms1, vs1, os1))
    array_6 = np.array(
    [[0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0]])
    
    assert np.array_equal(array_5, array_6)
            
def test_valid_art_total_20p(): 
    out_1 = sm.valid_art_total_20p(ms1, vs1, os1)   

    assert out_1 == 58    
    
def test_valid_standard_matrix_25p():
    assert sm.valid_standard_matrix_25p(ms2, vs2, os2) == True
     
def test_valid_marking_space_25p():
    array_7 = np.array(sm.valid_marking_space_25p(ms2, vs2, os2))
    array_8 = np.array(
    [[0,1,0,0,0,0,0,1,0],[0,0,1,1,0,0,0,1,0],[1,0,0,1,0,0,0,0,0],\
     [0,0,0,0,0,1,0,0,0],[1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,1,1],\
     [0,1,0,0,0,0,0,1,0],[1,1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0]] )
    
    assert np.array_equal(array_7, array_8)    
    
def test_valid_value_space_25p():
    array_9 = np.array(sm.valid_value_space_25p(ms2, vs2, os2))
    array_10 = np.array(
    [[0,1,2,3,4,5,6,7,8],[1,0,1,2,3,4,5,6,7],[2,1,0,1,2,3,4,5,6],\
     [3,2,1,0,1,2,3,4,5],[4,3,2,1,0,1,2,3,4],[5,4,3,2,1,0,1,2,3],\
     [6,5,4,3,2,1,0,1,2],[7,6,5,4,3,2,1,0,1],[8,7,6,5,4,3,2,1,0]])
    
    assert np.array_equal(array_9, array_10)    
    
def test_valid_outcome_space_25p():
    array_11 = np.array(sm.valid_outcome_space_25p(ms2, vs2, os2))
    array_12 = np.array(
    [[0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0]])
    
    assert np.array_equal(array_11, array_12)    
    
def test_valid_art_total_25p(): 
    out_2 = sm.valid_art_total_25p(ms2, vs2, os2)   

    assert out_2 == 66    
   
def test_valid_standard_matrix_30p():
    assert sm.valid_standard_matrix_30p(ms3, vs3, os3) == True

def test_valid_marking_space_30p():
    array_13 = np.array(sm.valid_marking_space_30p(ms3, vs3, os3))
    array_14 = np.array(
    [[0,1,1,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,1],\
     [0,0,0,0,1,1,0,1,0],[0,0,1,0,0,0,0,1,1],[0,0,0,1,1,0,0,0,0],\
     [0,1,0,0,1,1,0,0,0],[0,1,0,0,1,0,0,0,1],[0,0,0,0,1,1,0,0,0]] )
    
    assert np.array_equal(array_13, array_14)    
    
def test_valid_value_space_30p():
    array_15 = np.array(sm.valid_value_space_30p(ms3, vs3, os3))
    array_16 = np.array(
    [[0,1,2,3,4,5,6,7,8],[1,0,1,2,3,4,5,6,7],[2,1,0,1,2,3,4,5,6],\
     [3,2,1,0,1,2,3,4,5],[4,3,2,1,0,1,2,3,4],[5,4,3,2,1,0,1,2,3],\
     [6,5,4,3,2,1,0,1,2],[7,6,5,4,3,2,1,0,1],[8,7,6,5,4,3,2,1,0]])
    
    assert np.array_equal(array_15, array_16)        

def test_valid_outcome_space_30p():
    array_17 = np.array(sm.valid_outcome_space_30p(ms3, vs3, os3))
    array_18 = np.array(
    [[0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0]])
    
    assert np.array_equal(array_17, array_18)   

def test_valid_art_total_30p(): 
    out_3 = sm.valid_art_total_30p(ms3, vs3, os3)   

    assert out_3 == 65     
    
    
def test_valid_standard_matrix_35p():
    assert sm.valid_standard_matrix_35p(ms4, vs4, os4) == True    
    
    
def test_valid_marking_space_35p():
    array_19 = np.array(sm.valid_marking_space_35p(ms4, vs4, os4))
    array_20 = np.array(
    [[0,0,0,0,0,0,1,1,0],[0,0,1,1,0,0,0,0,0],[0,0,0,1,1,1,0,0,0],\
     [0,0,0,0,1,0,0,1,0],[0,0,1,0,0,1,1,1,1],[1,1,0,0,0,0,0,1,0],\
     [1,0,0,0,0,1,0,0,1],[1,0,0,0,1,0,0,0,0],[1,0,1,0,0,0,1,0,0]] )    
    
    assert np.array_equal(array_19, array_20)
    
def test_valid_value_space_35p():
    array_21 = np.array(sm.valid_value_space_35p(ms4, vs4, os4))
    array_22 = np.array(
    [[0,1,2,3,4,5,6,7,8],[1,0,1,2,3,4,5,6,7],[2,1,0,1,2,3,4,5,6],\
     [3,2,1,0,1,2,3,4,5],[4,3,2,1,0,1,2,3,4],[5,4,3,2,1,0,1,2,3],\
     [6,5,4,3,2,1,0,1,2],[7,6,5,4,3,2,1,0,1],[8,7,6,5,4,3,2,1,0]])
    
    assert np.array_equal(array_21, array_22)  

def test_valid_art_total_35p(): 
    out_4 = sm.valid_art_total_35p(ms4, vs4, os4)   

    assert out_4 == 85          
    
def test_valid_standard_matrix_40p():
    assert sm.valid_standard_matrix_40p(ms5, vs5, os5) == True    
        
def test_valid_marking_space_40p():
    array_23 = np.array(sm.valid_marking_space_40p(ms5, vs5, os5))
    array_24 = np.array(
    [[0,1,0,1,0,1,0,1,0],[0,0,0,1,0,1,0,1,0],[1,1,0,0,0,1,0,0,0],\
     [0,1,0,0,1,0,0,0,1],[0,1,1,0,0,1,1,1,0],[0,1,1,0,0,0,0,0,1],\
     [0,0,0,0,0,1,0,1,1],[0,0,0,1,0,0,0,0,1],[0,0,1,0,1,0,0,0,0]] )    
    
    assert np.array_equal(array_23, array_24)    
    
    
def test_valid_value_space_40p():
    array_25 = np.array(sm.valid_value_space_40p(ms5, vs5, os5))
    array_26 = np.array(
    [[0,1,2,3,4,5,6,7,8],[1,0,1,2,3,4,5,6,7],[2,1,0,1,2,3,4,5,6],\
     [3,2,1,0,1,2,3,4,5],[4,3,2,1,0,1,2,3,4],[5,4,3,2,1,0,1,2,3],\
     [6,5,4,3,2,1,0,1,2],[7,6,5,4,3,2,1,0,1],[8,7,6,5,4,3,2,1,0]])
    
    assert np.array_equal(array_25, array_26)      
    

def test_valid_art_total_40p(): 
    out_5 = sm.valid_art_total_40p(ms5, vs5, os5)   

    assert out_5 == 82  

def test_valid_standard_matrix_45p():
    assert sm.valid_standard_matrix_45p(ms6, vs6, os6) == True               
    
    
def test_valid_marking_space_45p():
    array_27 = np.array(sm.valid_marking_space_45p(ms6, vs6, os6))
    array_28 = np.array(
    [[0,1,0,0,1,1,0,0,0],[0,0,0,0,1,0,0,1,0],[0,0,0,0,1,0,0,1,1],\
     [1,1,1,0,1,1,0,1,0],[0,1,0,1,0,1,0,0,0],[0,0,0,1,0,0,1,1,0],\
     [0,1,0,0,0,0,0,1,1],[0,0,1,1,1,1,0,0,1],[0,1,0,0,0,1,1,1,0]] )   
    
    assert np.array_equal(array_27, array_28)        
    
def test_valid_value_space_45p():
    array_29 = np.array(sm.valid_value_space_45p(ms6, vs6, os6))
    array_30 = np.array(
    [[0,1,2,3,4,5,6,7,8],[1,0,1,2,3,4,5,6,7],[2,1,0,1,2,3,4,5,6],\
     [3,2,1,0,1,2,3,4,5],[4,3,2,1,0,1,2,3,4],[5,4,3,2,1,0,1,2,3],\
     [6,5,4,3,2,1,0,1,2],[7,6,5,4,3,2,1,0,1],[8,7,6,5,4,3,2,1,0]])
    
    assert np.array_equal(array_29, array_30)    
        
def test_valid_art_total_45p(): 
    out_6 = sm.valid_art_total_45p(ms6, vs6, os6)   

    assert out_6 == 91   
    
def test_valid_standard_matrix_50p():
    assert sm.valid_standard_matrix_50p(ms7, vs7, os7) == True               
        
def test_valid_marking_space_50p():
    array_31 = np.array(sm.valid_marking_space_50p(ms7, vs7, os7))
    array_32 = np.array(
     [[0,0,1,1,0,0,0,0,1],[0,0,0,0,0,0,0,0,1],[0,1,0,1,0,1,1,0,1],\
      [1,1,1,0,1,0,1,1,1],[0,1,1,0,0,0,0,1,1],[1,1,0,1,0,0,0,1,0],\
      [1,0,1,0,0,0,0,1,0],[0,1,0,1,1,0,0,0,1],[1,1,0,1,1,1,0,0,0]])   
    
    assert np.array_equal(array_31, array_32)            
    
def test_valid_value_space_50p():
    array_33 = np.array(sm.valid_value_space_50p(ms7, vs7, os7))
    array_34 = np.array(
    [[0,1,2,3,4,5,6,7,8],[1,0,1,2,3,4,5,6,7],[2,1,0,1,2,3,4,5,6],\
     [3,2,1,0,1,2,3,4,5],[4,3,2,1,0,1,2,3,4],[5,4,3,2,1,0,1,2,3],\
     [6,5,4,3,2,1,0,1,2],[7,6,5,4,3,2,1,0,1],[8,7,6,5,4,3,2,1,0]])
    
    assert np.array_equal(array_33, array_34)      
    
def test_valid_art_total_50p(): 
    out_7 = sm.valid_art_total_50p(ms7, vs7, os7)   

    assert out_7 == 131      
    