# Copyright 2008 - 2019 Joseph J. Simpson GPL-3.0-or-later
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
import artclass


if __name__ == "__main__":
    print("Structural Modeling Project TR-27 ART Dim Cluster v0.1.0")
    ms1 = artdata.str9dh2d
    vs1 = artdata.val9dh2d
    os1 = artdata.out9dh2d
    a1 = artclass.Art(ms1, vs1, os1)
    a1.create_good_art()
    print("\nArt new validated output space is.\n")
    print(a1.vlos)

    av1 = artclass.ValidArt(a1.vlms,a1.vlvs,a1.vlos,a1.art_vrc_1,a1.art_vrc_2)

    print("\nValid Art has been created.\n")

    na1 = artclass.NewArt(av1)
    na1.create_art_out()

    print("\nNew Art has been created from the valid input Art.\n")

    am3_lms = na1.new_art_valid_out_lms
    am3_lvs = na1.new_art_valid_out_lvs
    am3_los = na1.new_art_valid_out_los

    am3 = artclass.Art3M(am3_lms, am3_lvs, am3_los)

    print("\nNew Art3M ha been created ....\n")

    print("\nArt3m marking space is.......\n")
    print(am3.get_lms())

    print('\nArt3m value space is........\n')
    print(am3.get_lvs())

    print("\nArt3m outcome space is.........\n")
    print(am3.get_los())

    ip1 = artclass.InitialPop(am3.get_lms(), am3.get_lvs(), am3.get_los())
    ip1.make_initial_pop()
    ip1.make_pop_dictionary()
    ip1_dic = ip1.initial_pop_dictionary

    print("\nThe Initial population has been created.\n")
    
    print("The initial population dictionary contains %d keys..." % len(ip1_dic))
    keys_1 = ip1_dic.keys()
    print("keys_1 content is: ")
    print(keys_1)
    
    wp1 = artclass.WorkingPop(ip1_dic)
    wp1.make_total_pop()
    wp1_tpd = wp1.total_pop_dict_out
    keys_2 = wp1_tpd.keys()
    
    wtp1 = artclass.WorkingTotalPop(wp1_tpd)
    wtp1.make_working_total_pop()
    wtp1_tpd = wtp1.total_pop_dict_wtp_out

    keys_3 = wtp1_tpd.keys()
    print(keys_3)
    
   
    print("Running the process now..... Please wait...")
    ra1 = artclass.RunArt("ra1", 1000, 28, artdata.str9dh2d, artdata.val9dh2d)
    ra1.print_initialization_data()
    ra1.build_population()
    ra1.print_final_data()
    print("Process complete..")