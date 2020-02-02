# -*- coding: utf-8 -*-

#   Copyright 2008 - 2020 Joseph J. Simpson GPL-3.0-or-later
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



import artclass

def valid_standard_matrix_20p(ms1, vs1, os1):
    a1 = artclass.Art(ms1, vs1, os1)
    a1.create_good_art()
    return a1.valid_art

def valid_marking_space_20p(ms1, vs1, os1):
    a2 = artclass.Art(ms1, vs1, os1)
    a2.create_good_art()
    return a2.lms
    
def valid_value_space_20p(ms1, vs1, os1):
    a2 = artclass.Art(ms1, vs1, os1)
    a2.create_good_art()
    return a2.lvs

def valid_outcome_space_20p(ms1, vs1, os1):
    a3 = artclass.Art(ms1, vs1, os1)
    a3.create_good_art()
    return a3.los

def valid_art_total_20p(ms1, vs1, os1):
    a4 = artclass.Art(ms1, vs1, os1)
    a4.create_good_art()
    a5 = artclass.ValidArt(a4.vlms, a4.vlvs, a4.vlos, a4.art_vrc_1, a4.art_vrc_2)
    
    return a5.valid_art_total

def valid_standard_matrix_25p(ms2, vs2, os2):
    a6 = artclass.Art(ms2, vs2, os2)
    a6.create_good_art()
    return a6.valid_art

def valid_marking_space_25p(ms2, vs2, os2):
    a7 = artclass.Art(ms2, vs2, os2)
    a7.create_good_art()
    return a7.lms

def valid_value_space_25p(ms2, vs2, os2):
    a8 = artclass.Art(ms2, vs2, os2)
    a8.create_good_art()
    return a8.lvs

def valid_outcome_space_25p(ms2, vs2, os2):
    a9 = artclass.Art(ms2, vs2, os2)
    a9.create_good_art()
    return a9.los

def valid_art_total_25p(ms2, vs2, os2):
    a10 = artclass.Art(ms2, vs2, os2)
    a10.create_good_art()
    a11 = artclass.ValidArt(a10.vlms, a10.vlvs, a10.vlos, a10.art_vrc_1, a10.art_vrc_2)
    
    return a11.valid_art_total

def valid_standard_matrix_30p(ms3, vs3, os3):
    a12 = artclass.Art(ms3, vs3, os3)
    a12.create_good_art()
    return a12.valid_art

def valid_marking_space_30p(ms3, vs3, os3):
    a13 = artclass.Art(ms3, vs3, os3)
    a13.create_good_art()
    return a13.lms

def valid_value_space_30p(ms3, vs3, os3):
    a14 = artclass.Art(ms3, vs3, os3)
    a14.create_good_art()
    return a14.lvs

def valid_outcome_space_30p(ms3, vs3, os3):
    a15 = artclass.Art(ms3, vs3, os3)
    a15.create_good_art()
    return a15.los

def valid_art_total_30p(ms3, vs3, os3):
    a16 = artclass.Art(ms3, vs3, os3)
    a16.create_good_art()
    a17 = artclass.ValidArt(a16.vlms, a16.vlvs, a16.vlos, a16.art_vrc_1, a16.art_vrc_2)

    return a17.valid_art_total

def valid_standard_matrix_35p(ms4, vs4, os4):
    a18 = artclass.Art(ms4, vs4, os4)
    a18.create_good_art()
    return a18.valid_art


def valid_marking_space_35p(ms4, vs4, os4):
    a19 = artclass.Art(ms4, vs4, os4)
    a19.create_good_art()
    return a19.lms

def valid_value_space_35p(ms4, vs4, os4):
    a20 = artclass.Art(ms4, vs4, os4)
    a20.create_good_art()
    return a20.lvs

def valid_art_total_35p(ms4, vs4, os4):
    a21 = artclass.Art(ms4, vs4, os4)
    a21.create_good_art()
    a22 = artclass.ValidArt(a21.vlms, a21.vlvs, a21.vlos, a21.art_vrc_1, a21.art_vrc_2)
    
    return a22.valid_art_total

def valid_standard_matrix_40p(ms5, vs5, os5):
    a23 = artclass.Art(ms5, vs5, os5)
    a23.create_good_art()
    return a23.valid_art

def valid_marking_space_40p(ms5, vs5, os5):
    a24 = artclass.Art(ms5, vs5, os5)
    a24.create_good_art()
    return a24.lms

def valid_value_space_40p(ms5, vs5, os5):
    a25 = artclass.Art(ms5, vs5, os5)
    a25.create_good_art()
    return a25.lvs

