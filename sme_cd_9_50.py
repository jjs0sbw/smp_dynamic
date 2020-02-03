# Copyright 2020 Joseph J. Simpson GPL-3.0-or-later
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
## -*- coding: utf-8 -*-

import artdata
import artclass

if __name__ == "__main__":
    ms7 = artdata.SME_CD_9_50P_NER_DO_V001
    vs7 = artdata.SME_CD_9_50P_NER_DO_VS_V001
    os7 = artdata.SME_CD_9_50P_NER_DO_OS_V001

    a1 = artclass.Art(ms7, vs7, os7)
    a1.create_good_art()

    print("\nThe original marking space is: \n")
    print(a1.lms)
    
    print("\nThe original value space is: \n")
    print(a1.lvs)
    
    print("\nThe original outcome space is: \n")
    print(a1.los)

    print("\nArt new validated outcome space is.\n")
    print(a1.vlos)

    av1 = artclass.ValidArt(a1.vlms,a1.vlvs,a1.vlos,a1.art_vrc_1,a1.art_vrc_2)

    print("\nValid Art has been created.\n")
    
    total_av1 = av1.valid_art_total
    
    print("The initial matrix total is: " + str(total_av1) + "\n")
    
    print("\nRunning the sme_cd_9_50 process now..... Please wait...\n")
    sme_cd_9_50 = artclass.RunArt("sme_cd_9_50", 1000, 75, ms7, vs7)
    sme_cd_9_50.print_initialization_data()
    sme_cd_9_50.build_population()
    sme_cd_9_50.print_final_data()
    print("sme_cd_9_50 process is now complete..\n")