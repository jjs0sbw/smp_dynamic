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
from datetime import date, datetime, time
import numpy as np
import copy
import random
np.random.seed(8912)
random.seed(8912)

class Art(object):
    """The ART class encapsulates the variable and methods required
    to produce a valid ART class.  The initial arrays may not create a
    valid combination.  Therefor the ART class has methods to validate
    the ART class and create a valid ART"""
    def __init__(self,ms,vs,os):
        """Defines a new ART Object """
        #place input arrays in to numpy format
        self.lms = np.array(list(copy.deepcopy(ms)))
        self.lvs = np.array(list(copy.deepcopy(vs)))
        self.los = np.array(list(copy.deepcopy(os)))
        #provide a set of numpy array variables to hold validated arrays
        self.vlms = np.array([])
        self.vlvs = np.array([])
        self.vlos = np.array([])
        #array length
        self.len_lms = len(self.lms)
        #valid row and column numbers
        self.art_vrc_1 = 0
        self.art_vrc_2 = 0
        #test flag values
        self.OK_lms = False
        self.OK_lms_dia = False
        self.OK_lms_point = False
        #total value of the ART
        self.art_valid_total = 0
        self.valid_art = False


    ######### valid row and column numbers
    def generate_row_column_number(self):
        """Randomy generates a valid row and cluumn number.
        Very small probability that a valid set will not be found.
        (Need to work an exception case)"""
        run_limit_flag1 = 0
        self.art_vrc_1 = copy.copy(random.randint(0,self.len_lms - 1))
        self.art_vrc_2 = copy.copy(random.randint(0,self.len_lms - 1))
        while self.art_vrc_2 == self.art_vrc_1 and run_limit_flag1 < 200:
              self.art_vrc_2 = copy.copy(random.randint(0,self.len_lms - 1))
              run_limit_flag1 = run_limit_flag1 + 1
    # check for zeros on diagional and intersections
    def validate_lms(self):
        """Check that all values on the lms matrix diagional are
        equal to zero. Check that the selectd row and column intersection
        points are equal to zero.  Set lms status flag."""
        #################################################
        #first check for all zeros on the matrix diagional
        ###################################################
        check_total = 0
        dia = range(0,self.len_lms - 1)
        for value in dia:
            check_total = check_total + self.lms[value][value]
        if check_total == 0:
            self.OK_lms_dia = True
        else:
            self.OK_lms_dia = False
            print("Current ART lms is invalid with non-zero on the diagional")

        #############################
        ## Check that all ms numbers are either 0 (zero) or 1 (one)
        ## Check that row and column number are in the right range
        ## [To Do]
        ##############################

        #Check that the intersection points are zero
        ############################################
        point_check_total = 0
        point_check_total = point_check_total + \
            self.lms[self.art_vrc_1][self.art_vrc_1]
        point_check_total = point_check_total + \
            self.lms[self.art_vrc_1][self.art_vrc_2]
        point_check_total = point_check_total + \
            self.lms[self.art_vrc_2][self.art_vrc_1]
        point_check_total = point_check_total + \
            self.lms[self.art_vrc_2][self.art_vrc_2]

        #check to make sure that vrc_1 and vrc_2 are different values
        #############################################################
        if self.art_vrc_1 == self.art_vrc_2:
            point_check_total = point_check_total + 1

        #set lms status flags
        ######################
        if point_check_total == 0:
            self.OK_lms_point = True
        else:
            self.OK_lms_point = False

        if self.OK_lms_dia and self.OK_lms_point:
            self.OK_lms = True
        else:
            self.OK_lms = False

    def create_vlms(self):
        """Create a validated lms martix. (Need to add exception handler) """
        if self.OK_lms == True:
            self.vlms = copy.deepcopy(self.lms)
        else:
            print("lms not valid")

    def create_vlvs(self):
        """For this type of ART evolutionary computation aproach the value
        matrix is static and does not change.  So, if the lms is valid, then
        just copy the input lvs into the vlvs."""
        if self.OK_lms == True:
            self.vlvs = copy.deepcopy(self.lvs)
        else:
            print("lms not valid")

    def create_vlos(self):
        """If the lms is valid then, a valid output space is calculated.
        (May need to think about an exception handler.)"""
        if self.OK_lms == True:
            self.vlos = copy.deepcopy(self.vlms * self.vlvs)
        else:
            print("lms not valid")

    def calculate_art_valid_total(self):
        """If the lms is valid and a new vlos has been created then
        the total for the vlos matrix is calculated. (May need to think
        about an exception handler here)"""
        if self.OK_lms == True:
            self.art_valid_total = copy.copy(np.sum(self.vlos))

    def create_good_art(self):
        """Method to create a good (valid) ART. """
        run_limit_flag2 = 0
        while self.OK_lms == False and run_limit_flag2 < 1000:
            run_limit_flag2 = run_limit_flag2 + 1
            self.generate_row_column_number()
            self.validate_lms()
        if self.OK_lms == False:
            print("Unable to validate the input art lms")
            print("Please enter a new art lms")
            self.valid_art = False
        elif self.OK_lms == True:
            self.valid_art = True
            self.create_vlms()
            self.create_vlvs()
            self.create_vlos()
            self.calculate_art_valid_total()


class ValidArt(object):
    """The ValidArt class is used to encapsulate and process a valid Art
    object along with its attributes."""
    def __init__(self, vlms, vlvs, vlos, vrc_1, vrc_2):
        self.valid_art_lms = np.array(list(copy.deepcopy(vlms)))
        self.valid_art_lvs = np.array(list(copy.deepcopy(vlvs)))
        self.valid_art_los = np.array(list(copy.deepcopy(vlos)))
        self.valid_art_vrc_1 = copy.copy(vrc_1)
        self.valid_art_vrc_2 = copy.copy(vrc_2)
        self.valid_art_total = copy.copy(np.sum(self.valid_art_los))

class NewArt(object):
    """Create a new Art based on a valid art that is passed in
    as an argument.  The valid Art is randomaly modified to produce
    a new valid Art."""
    def __init__(self, ValidArt):
        self.ValidArt_in = copy.deepcopy(ValidArt)
        self.new_art_out = None
        self.new_art_valid_in_total = copy.copy(np.sum(ValidArt.valid_art_los))
        self.new_art_valid_out_total = None
        self.new_art_valid_in_lms = copy.deepcopy(ValidArt.valid_art_lms)
        self.new_art_valid_in_tran_lms = copy.deepcopy\
        (np.transpose(self.new_art_valid_in_lms))
        #valid_out_lms is the same as valid_in_lms to start the process
        self.new_art_valid_out_lms = copy.deepcopy(ValidArt.valid_art_lms)
        self.new_art_valid_out_tran_lms = None
        self.new_art_lms_length = len(self.new_art_valid_in_lms)
        #self.rowvector = np.array(range(1, self.new_art6_lms_length + 1))
        #self.columnvector = np.array(range(1, self.new_art6_lms_length + 1))
        self.tmprow1 = np.array(range(1,self.new_art_lms_length + 1))
        self.tmprow2 = np.array(range(1,self.new_art_lms_length + 1))
        self.tmpcolumn1 = np.array(range(1,self.new_art_lms_length + 1))
        self.tmpcolumn2 = np.array(range(1,self.new_art_lms_length + 1))
        self.new_art_valid_in_num_1 = copy.copy(ValidArt.valid_art_vrc_1)
        self.new_art_valid_in_num_2 = copy.copy(ValidArt.valid_art_vrc_2)
        self.new_art_valid_in_lvs = copy.deepcopy(ValidArt.valid_art_lvs)
        self.new_art_valid_out_lvs = copy.deepcopy(ValidArt.valid_art_lvs)
        self.new_art_valid_in_los = copy.deepcopy(ValidArt.valid_art_los)
        self.new_art_valid_out_los = None
        self.new_valid_art_out = False #added flag for valid out ART creation

    def create_art_out(self):
        self.tmprow1 = copy.deepcopy(np.array(self.new_art_valid_in_lms\
            [self.new_art_valid_in_num_1][:]))
        self.tmprow2 = copy.deepcopy(np.array(self.new_art_valid_in_lms\
            [self.new_art_valid_in_num_2][:]))
        self.tmpcolumn1 = copy.deepcopy(np.array(self.new_art_valid_in_tran_lms\
            [self.new_art_valid_in_num_1][:]))
        self.tmpcolumn2 = copy.deepcopy(np.array(self.new_art_valid_in_tran_lms\
            [self.new_art_valid_in_num_2][:]))
        self.new_art_valid_out_lms[self.new_art_valid_in_num_1] = \
            copy.deepcopy(self.tmprow2[:])
        self.new_art_valid_out_lms[self.new_art_valid_in_num_2] = \
            copy.deepcopy(self.tmprow1[:])
        self.new_art_valid_out_tran_lms = np.array(np.transpose(copy.deepcopy\
            (self.new_art_valid_out_lms[:])))
        self.new_art_valid_out_tran_lms[self.new_art_valid_in_num_1] = \
            copy.deepcopy(self.tmpcolumn2)
        self.new_art_valid_out_tran_lms[self.new_art_valid_in_num_2] = \
            copy.deepcopy(self.tmpcolumn1)
        self.new_art_valid_out_lms = np.array(np.transpose(copy.deepcopy\
            (self.new_art_valid_out_tran_lms[:])))
        self.new_art_valid_out_los = copy.deepcopy(self.new_art_valid_out_lms *\
            self.new_art_valid_out_lvs)
        self.new_art_out = Art(copy.deepcopy(self.new_art_valid_out_lms), \
            copy.deepcopy(self.new_art_valid_out_lvs), copy.deepcopy\
            (self.new_art_valid_out_los))
        self.new_art_out.create_good_art() #added this in version 16
        if self.new_art_out.valid_art == True:
            self.new_art_valid_out_total = copy.copy(np.sum\
                (self.new_art_out.los))
            self.new_valid_art_out = True
        else:
            print("New ART not valid...")
            self.new_art_out = None
            self.new_valid_art_out = False

class Art3M(object):
    """Art object used to manage the three basic Art matrices."""

    def __init__(self, lms_in, lvs_in, los_in):
        self.lms = copy.deepcopy(lms_in)
        self.lvs = copy.deepcopy(lvs_in)
        self.los = copy.deepcopy(los_in)

    def set_lms(self,a_lms):
        self.lms = copy.deepcopy(a_lms)

    def set_lvs(self, a_lvs):
        self.lvs = copy.deepcopy(a_lvs)

    def set_los(self, a_los):
        self.los = copy.deepcopy(a_los)

    def get_lms(self):
        return self.lms

    def get_lvs(self):
        return self.lvs

    def get_los(self):
        return self.los

class InitialPop(object):
    """Create an initial population of randomly generated solutions.
    """
    def __init__(self,initial_lms, initial_lvs, initial_los):
        self.initial_lms_in = copy.deepcopy(initial_lms)
        self.initial_lvs_in = copy.deepcopy(initial_lvs)
        self.initial_los_in = copy.deepcopy(initial_los)
        self.initial_pop = []
        self.initial_pop_dictionary = {}
        self.initial_pop_out = []
        self.pop_total = []
        self.new_pop_total = []
        self.in_upper_limit = copy.copy(len(self.initial_lms_in))
        self.pop_initial_art = None
        self.pop_valid_art = None
        self.pop_new_art = None
        self.initial_pop_out_min = None
        self.pop_limit = None
        self.pop_done = False

    def make_initial_pop(self):
        for x in range(1,self.in_upper_limit * 20):
            self.pop_initial_art = copy.deepcopy(Art(self.initial_lms_in, \
                self.initial_lvs_in, self.initial_los_in))
            self.pop_initial_art.create_good_art()
            if self.pop_initial_art.valid_art == False:
                print("Skip this invalid ART.. go to the next..")
            elif self.pop_initial_art.valid_art == True:
                self.pop_valid_art = copy.deepcopy(ValidArt(\
                    self.pop_initial_art.vlms,self.pop_initial_art.vlvs,\
                    self.pop_initial_art.vlos, self.pop_initial_art.art_vrc_1,\
                    self.pop_initial_art.art_vrc_2))
                self.pop_new_art = copy.deepcopy(NewArt(self.pop_valid_art))
                self.pop_new_art.create_art_out()
                self.pop_total.append(copy.copy(\
                    self.pop_new_art.new_art_valid_out_total))
                self.pop_new_art.new_art_out.create_good_art()
                self.pop_limit = copy.copy(\
                    self.pop_new_art.new_art_out.len_lms * 10)
                self.initial_pop.append(copy.deepcopy(\
                    self.pop_new_art.new_art_out))

        self.sorted_pop_total = np.sort(self.pop_total)
        self.initial_pop_out_min = copy.copy(self.sorted_pop_total[0])
        int_pop_limit_third = int(self.pop_limit/3)
        #added for new approach
        #make a new approach to population development
        for x in range(self.in_upper_limit * 10): # remove divide by 2
            self.new_pop_total.append(copy.deepcopy(self.sorted_pop_total[0]))
            self.new_pop_total.append(copy.deepcopy(\
                self.sorted_pop_total[int_pop_limit_third]))
                # self.sorted_pop_total[self.pop_limit/3]))

        for x in range(0,len(self.new_pop_total)-1): #new_pop_total len = 24
            n = self.new_pop_total[x]
            for y in range(0,len(self.initial_pop)-1):#initila_pop_1 len = 23
                if n == self.initial_pop[y].art_valid_total:
                    self.initial_pop_out.append(copy.deepcopy(\
                        self.initial_pop[y]))
                    self.initial_pop_out.append(copy.deepcopy(\
                        self.initial_pop[y]))
                    self.initial_pop[y].valid_total = 0

        if len(self.initial_pop_out) > self.pop_limit * 10:
            self.initial_pop_out = copy.deepcopy(\
                self.initial_pop_out[:self.pop_limit * 10])
        else:
            self.initial_pop_out = copy.deepcopy(self.initial_pop_out) * 2

    def make_pop_dictionary(self):
        #make dictionary with new art3m class
        if self.initial_pop == []:
            self.make_initial_pop6()
        #c_dict_list = []
        c_value_list = []
        c_key_list = []
        for x in range(len(self.initial_pop)):
            #c_li = []
            #part_a = 1
            part_b = copy.deepcopy(self.initial_pop[x].vlms)
            part_c = copy.deepcopy(self.initial_pop[x].vlvs)
            part_d = copy.deepcopy(self.initial_pop[x].vlos)
            #p1 = copy.deepcopy([part_a, part_b, part_c, part_d])
            current_value = copy.deepcopy(Art3M(part_b, part_c,part_d))
            current_key = self.initial_pop[x].art_valid_total
            c_value_list.append(current_value)
            c_key_list.append(current_key)

        self.initial_pop_dictionary = dict(zip(copy.deepcopy(c_key_list), \
            copy.deepcopy(c_value_list)))
        #need to work adding a list to each of the value bins
        i_keys = self.initial_pop_dictionary.keys()
        for x in i_keys:
            t_list = []
            t_list.append(copy.deepcopy(self.initial_pop_dictionary[x]))
            self.initial_pop_dictionary[x] = t_list

class WorkingPop(object):
    """Create a new working population. """
    def __init__(self,initial_pop_dict,):
        self.initial_pop_dict_in = copy.deepcopy(initial_pop_dict)
        self.total_pop_dict_out = {}
        self.new_wp_pop = {}


    def make_total_pop(self):
        #build input components to make new population
        # initial_wp_pop_keys = copy.deepcopy(self.initial_pop_dict_in.keys())
        initial_wp_pop_keys = copy.deepcopy(list(self.initial_pop_dict_in.keys()))
        length_wp_pop_keys = len(initial_wp_pop_keys)
        r_sel = copy.copy(random.randint(0,length_wp_pop_keys -1))
        sel = initial_wp_pop_keys[r_sel]
        t_lms = self.initial_pop_dict_in[sel][0].get_lms()
        t_lvs = self.initial_pop_dict_in[sel][0].get_lvs()
        t_los = self.initial_pop_dict_in[sel][0].get_los()
        #make new population dictionary
        i_pop = InitialPop(t_lms, t_lvs, t_los)
        i_pop.make_initial_pop()
        i_pop.make_pop_dictionary()
        #OK, now we have three populations in, out and new
        self.new_wp_pop = copy.deepcopy(i_pop.initial_pop_dictionary)
        self.total_pop_dict_out.update(self.initial_pop_dict_in)

        # n_pop_key = copy.deepcopy(self.new_wp_pop.keys())
        n_pop_key = copy.deepcopy(list(self.new_wp_pop.keys()))
        # total_key = copy.deepcopy(self.total_pop_dict_out.keys())
        total_key = copy.deepcopy(list(self.total_pop_dict_out.keys()))
        for i in range(len(n_pop_key)):
            eq_1 = np.equal(total_key, n_pop_key[i])
            sum_eq_1 = np.sum(eq_1)
            if sum_eq_1 == 0:
                tmp_list = []
                new_item = self.new_wp_pop[n_pop_key[i]][0]
                tmp_list.append(copy.deepcopy(new_item))
                self.total_pop_dict_out[n_pop_key[i]] = copy.deepcopy(tmp_list)
            else:
                #key in current key list
                t_pop_value_len = len(self.total_pop_dict_out[n_pop_key[i]])
                length = len(self.total_pop_dict_out[n_pop_key[i]]\
                    [t_pop_value_len -1].get_lms())
                n_pop_value_len = len(self.new_wp_pop[n_pop_key[i]])
                part_1 = self.new_wp_pop[n_pop_key[i]]\
                    [n_pop_value_len -1].get_lms()
                part_2 = self.total_pop_dict_out[n_pop_key[i]]\
                    [n_pop_value_len -1].get_lms()
                eq_2 = np.equal(part_1, part_2)
                sum_eq_2 = np.sum(eq_2)
                flag_one = length * length
                if sum_eq_2 < flag_one:
                    #The new pop key exists already and ...
                    #The value arrays are different.....
                    old_total_value = copy.deepcopy(\
                        self.total_pop_dict_out[n_pop_key[i]])
                    new_pop_value = copy.deepcopy(self.new_wp_pop[n_pop_key[i]])
                    new_combined_value = []
                    new_combined_value.append(old_total_value[0])
                    new_combined_value.append(new_pop_value[0])
                    self.total_pop_dict_out[n_pop_key[i]] = new_combined_value

                else:
                    #The new pop key exists and the value arrays are the same..
                    #Do nothing..
                    pass

class WorkingTotalPop(object):

    def __init__(self,total_pop_dict,):
        self.total_pop_dict_wtp_in = copy.deepcopy(total_pop_dict)
        self.total_pop_dict_wtp_out = {}
        self.current_min_key_wtp = np.min(np.array(total_pop_dict.keys()))
        self.min_key_list_wtp = []
        self.length_wtp = copy.deepcopy(len(self.total_pop_dict_wtp_in[\
            list(self.total_pop_dict_wtp_in.keys())[0]]))
            # self.total_pop_dict_wtp_in.keys()[0]]))

    def make_working_total_pop(self):
        self.total_pop_dict_wtp_out.update(self.total_pop_dict_wtp_in)
        # wtp_out_keys = copy.deepcopy(self.total_pop_dict_wtp_out.keys())
        wtp_out_keys = copy.deepcopy(list(self.total_pop_dict_wtp_out.keys()))
        length_wtp_out_keys = copy.copy(len(wtp_out_keys))
        wtp_key_min = copy.copy(np.min(np.array(wtp_out_keys)))
        wtp_key_max = copy.copy(np.max(np.array(wtp_out_keys)))
        wtp_key_average = copy.copy((wtp_key_min + wtp_key_max)/2)

        for i in range(length_wtp_out_keys):
            wtp_sel = wtp_out_keys[copy.copy(random.randint(0, \
                length_wtp_out_keys -1))]
            ##############################################
            ###  AVERAGE to MAX  ONE
            ##############################################
            if wtp_sel > wtp_key_average: #switch between average and max
                #wtp key is too big... break go to next key
                break
            else:
                wtp_value_len = len(self.total_pop_dict_wtp_in[wtp_sel])
                #value list associated with the key
                sel_art = copy.deepcopy(self.total_pop_dict_wtp_out[wtp_sel])
                #loop through the value list associated with the selected key
                #for each item in the value list....
                for x in range(0,wtp_value_len): #remove the -1
                    sel_art_lms = copy.deepcopy(sel_art[x].get_lms())
                    sel_art_lvs = copy.deepcopy(sel_art[x].get_lvs())
                    sel_art_los = copy.deepcopy(sel_art[x].get_los())
                    #make a new art
                    wtp_art = copy.deepcopy(Art(sel_art_lms, sel_art_lvs, \
                        sel_art_los))
                    #create a good valid art
                    wtp_art.create_good_art()
                    #check to see if new art is valid
                    if wtp_art.valid_art == False:
                        #print "Invalid art ..."
                        break
                    #art is valid so continue with the process
                    else:
                        wtp_valid_art = copy.deepcopy(ValidArt(wtp_art.vlms, \
                            wtp_art.vlvs, wtp_art.vlos, wtp_art.art_vrc_1, \
                            wtp_art.art_vrc_2))
                        wtp_new_art = copy.deepcopy(NewArt(wtp_valid_art))
                        wtp_new_art.create_art_out()
                        #need to add valid art check...
                        if wtp_new_art.new_valid_art_out == False:
                            break
                        #new art valid so continue with the process
                        else:
                            wtp_new_art_lms = copy.deepcopy(\
                                wtp_new_art.new_art_out.lms)
                            wtp_new_art_lvs = copy.deepcopy(\
                                wtp_new_art.new_art_out.lvs)
                            wtp_new_art_los = copy.deepcopy(\
                                wtp_new_art.new_art_out.los)
                            wtp_new_art_key = copy.copy(np.sum(\
                                np.array(wtp_new_art_los)))
                            #######################################
                            ##### AVEARGE to MAX TWO
                            ########################################
                            if wtp_new_art_key > wtp_key_average:
                                #switch between max and average
                                #print "[Continue wtp - s4] -- wtp new art key
                                #greater than average... do nothing"
                                break
                            else:
                                #check if wtp_new_art_key is in the key list
                                eq_wtp_1 = np.equal(wtp_out_keys, \
                                    wtp_new_art_key)
                                sum_eq_wtp_1 = np.sum(eq_wtp_1)
                                if sum_eq_wtp_1 == 0:
                                    #wtp_new_art_value not in current list
                                    #so add to list
                                    wtp_new_art_value = copy.deepcopy(Art3M(\
                                        wtp_new_art_lms, wtp_new_art_lvs, \
                                        wtp_new_art_los))
                                    self.total_pop_dict_wtp_out[\
                                        wtp_new_art_key] = copy.deepcopy(\
                                        [wtp_new_art_value])
                                    t_new_keys = \
                                        self.total_pop_dict_wtp_out.keys()

                                else:
                                    #wtp_new_art_value is in the current list
                                    #need to check for existing array values
                                    #create loop to go through the value list
                                    #first select the proper key-value pair
                                    wtp_new_art_key_value = copy.deepcopy(\
                                        self.total_pop_dict_wtp_out[\
                                        wtp_new_art_key])
                                    #find the length of the new value list
                                    length_wtp_new_value_list = copy.copy(\
                                        len(wtp_new_art_key_value))
                                    different_flag = 0
                                    #check and bound the value list processing
                                    max_bound = copy.copy(self.length_wtp * \
                                        self.length_wtp)
                                    if length_wtp_new_value_list > max_bound:
                                        max_range = max_bound
                                        random_flag = True
                                    else:
                                        max_range = length_wtp_new_value_list
                                        random_flag = False
                                    for x in range(max_range): #remove the -1
                                        if random_flag == True:
                                            xx = copy.copy(random.randint(0, \
                                            length_wtp_new_value_list -1))
                                        elif random_flag == False:
                                            xx = x
                                        #check each array to see if the array 
                                        #pattern is already in the list
                                        wtp_new_list_lms = \
                                            wtp_new_art_key_value[xx].get_lms()
                                        wtp_new_list_los = \
                                            wtp_new_art_key_value[xx].get_los()
                                        eq_2 = np.equal(wtp_new_list_lms, \
                                            wtp_new_art_lms)
                                        sum_wtp_eq_2 = np.sum(eq_2)
                                        length = len(wtp_new_art_lms)
                                        flag_one_wtp = length * length
                                        if sum_wtp_eq_2 < flag_one_wtp:
                                            different_flag = different_flag + 1
                                        else:
                                            different_flag = 0
                                    if different_flag > 0:
                                        #add new element to value list
                                        wtp_new_art_value_1 = copy.deepcopy(\
                                            Art3M(wtp_new_art_lms, \
                                            wtp_new_art_lvs, wtp_new_art_los))
                                        wtp_new_art_key_value.append(\
                                            copy.deepcopy(wtp_new_art_value_1))
                                        self.total_pop_dict_wtp_out[\
                                            wtp_new_art_key] = copy.deepcopy(\
                                            wtp_new_art_key_value)
                                        new_keys = copy.deepcopy(\
                                            list(self.total_pop_dict_wtp_out.keys()))
                                            # self.total_pop_dict_wtp_out.keys())
                                    else:
                                        #Array already in list...
                                        break


class RunArt:
    """RunArt is designed to manage the Art program execution. """
    def __init__(self, run_tag, max_interation, target_number, lms, lvs):
        self.in_run_tag = run_tag
        self.in_max_interation = max_interation
        self.in_target_number = target_number
        self.in_lms = lms
        self.in_lvs = lvs
        self.in_los = np.array(self.in_lms) * np.array(self.in_lvs)
        self.in_value = np.sum(np.array(self.in_lms) * np.array(self.in_lvs))
        self.in_lms_sum = np.sum(self.in_lms)
        self.file_name = self.in_run_tag + ".txt"
        self.fout_a = open(self.file_name, 'a')
        self.pop_in = {} #need to pass between methods
        self.pop_out = {} #need to pass between methods
        self.min_lms = []
        self.min_lvs = self.in_lvs
        self.file_name = self.in_run_tag + ".txt"

    def print_initialization_data(self):
        fout_a = open(self.file_name, 'w')
        self.fout_a.write("\n###############################################\n")
        self.fout_a.write("##### Initial Data " + self.file_name + " #########")
        self.fout_a.write("\n###############################################\n")
        today_1 = datetime.now()
        today_f = today_1.strftime("%A,  %d.  %B %Y %I:%M%p")
        self.fout_a.write("\n###############################################\n")
        self.fout_a.write("##### DATE IS:  " + today_f + " #####\n")
        self.fout_a.write("##### TIME IS:  " + today_f  + " #####\n")
        self.fout_a.write("#################################################\n")
        s_1a = "Number of array entries is...%d\n" % self.in_lms_sum
        s_2a = "Initial value is.. %d \n" % self.in_value
        self.fout_a.write("\n#################################################")
        self.fout_a.write("\n %s \n" % s_1a)
        self.fout_a.write("\n %s \n" % s_2a)
        self.fout_a.write("#################################################\n")
        s_3a = "Initial input lms is ...\n %s" % np.array(self.in_lms)
        s_4a = "Initial input lvs is ...\n %s" % np.array(self.in_lvs)
        s_5a = "Initial input los is ...\n %s" % np.array(self.in_los)
        self.fout_a.write("\n#################################################")
        self.fout_a.write("\n %s \n" % s_3a)
        self.fout_a.write("\n###############################################\n")
        self.fout_a.write("\n %s \n" % s_4a)
        self.fout_a.write("\n###############################################\n")
        self.fout_a.write("\n %s \n" % s_5a)
        self.fout_a.write("\n###############################################\n")

    def build_population(self):
        i_pop = InitialPop(copy.deepcopy(self.in_lms),\
            copy.deepcopy(self.in_lvs),copy.deepcopy(self.in_los))

        i_pop.make_initial_pop()
        i_pop.make_pop_dictionary()
        w_pop = WorkingPop(i_pop.initial_pop_dictionary)
        w_pop.make_total_pop()

        flag_wt = 0
        pop_in = copy.deepcopy(w_pop.total_pop_dict_out)
        while flag_wt <= self.in_max_interation:
            batch_out = flag_wt % 2
            if batch_out == 0:
                string_1 = "flag_wt is ...%d\n" % flag_wt
                self.fout_a.write("\n############################\n")
                self.fout_a.write(string_1)
                self.fout_a.write("\n############################\n")
            flag_wt = flag_wt + 1
            wt_pop = WorkingTotalPop(copy.deepcopy(pop_in))
            wt_pop.make_working_total_pop()
            wt_keys = copy.deepcopy(list(wt_pop.total_pop_dict_wtp_out.keys()))
            # wt_keys = copy.deepcopy(wt_pop.total_pop_dict_wtp_out.keys())
            if batch_out ==0:
                string_2 = "Current WTP dictionary keys are..%s\n"  %wt_keys
                for i in wt_keys:
                    string_3 = "wt_key is..%d value array length is..%d\n" % \
                        (i ,len(wt_pop.total_pop_dict_wtp_out[i]))

            wt1_pop = WorkingTotalPop(copy.deepcopy(\
                wt_pop.total_pop_dict_wtp_out))
            wt1_pop.make_working_total_pop()
            wt1_keys = copy.deepcopy(list(wt1_pop.total_pop_dict_wtp_out.keys()))
            # wt1_keys = copy.deepcopy(wt1_pop.total_pop_dict_wtp_out.keys())
            if batch_out == 0:
                string_4 = "Current WTP1 dictionary keys are..%s\n" % wt1_keys
                for i in wt1_keys:
                    string_5 = "wt1_key is..%d value array length is..%d\n" % \
                        (i,  len(wt1_pop.total_pop_dict_wtp_out[i]))
            pop_in = copy.deepcopy(wt1_pop.total_pop_dict_wtp_out)
        self.pop_out = copy.deepcopy(wt1_pop.total_pop_dict_wtp_out)


    def print_final_data(self):

        target_key = self.in_target_number
        print("Target key is...", target_key)
        min_key = np.min(list(self.pop_out.keys()))
        print("Min key is .. : ", min_key)
        # wt1_keys = self.pop_out.keys()
        # min_key = np.min(np.array(wt1_keys))
        print("Minimum key is....", min_key)
        self.fout_a.write("\n################\n")
        self.fout_a.write("Target key is .. \n %s " % target_key)
        self.fout_a.write("\n################\n")
        self.fout_a.write("\n################\n")
        self.fout_a.write("Minimum key is .. \n %s " % min_key)
        self.fout_a.write("\n################\n")
        string_e1 = np.array(self.pop_out[min_key][0].get_lms())
        print("Array value min_key [0] is .. \n %s" % string_e1)
        print("\n")
        self.fout_a.write("\n################\n")
        self.fout_a.write("Array value min_key [0] is .. \n %s " % string_e1)
        self.fout_a.write("\n################\n")
        self.min_lms = np.array(self.pop_out[min_key][0].get_lms())
        self.min_lvs = np.array(self.pop_out[min_key][0].get_lvs())
        self.fout_a.write("Array lms in is \n %s \n" % np.array(\
            self.pop_out[min_key][0].get_lms()))
        self.fout_a.write("\n################\n")
        self.fout_a.write("Array lvs in is \n %s \n" % np.array(\
            self.pop_out[min_key][0].get_lvs()))
        self.fout_a.write("\n################\n")
        self.fout_a.write("Array los in is \n %s \n" % np.array(\
            self.pop_out[min_key][0].get_los()))
        self.fout_a.close()



if __name__ == "__main__":
    print("This is the artclass.......... ")