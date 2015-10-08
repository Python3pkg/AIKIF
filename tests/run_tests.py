#!/usr/bin/python3
# -*- coding: utf-8 -*-
# run_tests.py

import os
import glob
import time
import unittest as unittest

# run all tests in tests folder
all_tests = unittest.TestLoader().discover('.', pattern='test*.py')
unittest.TextTestRunner().run(all_tests)    

def wipe_file(fname):
    if os.path.exists(fname):
        try:
            os.remove(fname)
            print('deleted ' + fname)
        except:
            pass
        
print('Did the tests fail.... DID YOU TURN ON VIRTUALENV!   ". ~/p von"')
print('WIPING ALL TEST RESULTS - PRESS CTRL C TO STOP')

time.sleep(10)
wipe_file('index_odd_chars_results.txt')
wipe_file('index_odd_chars_source.txt')
wipe_file('index_normal_results.txt')
wipe_file('cls_file_test_data.txt')
wipe_file('index_normal_source.txt')
wipe_file('data.txt')
wipe_file('plan_test.txt')
wipe_file('datatable_sample.csv')
wipe_file('datatable_calcs.csv')
wipe_file('csv_sample.csv')
wipe_file('datatable_output.csv')
wipe_file('test_nested.zip')
wipe_file('test2.zip')
wipe_file('sample_small1.xml')
wipe_file('sample_small.xml')
wipe_file('summary_diary.dat')
wipe_file('command.log')
wipe_file('process.log')
wipe_file('filelist_images.csv')
wipe_file('filelist_image_metadata.csv')
wipe_file('review_ontology.txt')
wipe_file('review_file_samples.html')
wipe_file('review_ontology.txt')
wipe_file('test_world_traversed.txt')
wipe_file('test_world.txt')
wipe_file('review_ontology.html')
wipe_file('_sessions.txt')
wipe_file('programs_test_folder.csv')
wipe_file('programs_test_folder.md')
wipe_file('program_list.html')
wipe_file('tools.txt')
wipe_file('text_tools_sample.csv')
wipe_file('task.html')
wipe_file('task.md')
wipe_file('task.rst')
wipe_file('test.md')

wipe_file('config_credentials.txt')
wipe_file('programs_test_folder.md')
wipe_file('programs_test_folder.csv')

wipe_file('small_image.jpg')
wipe_file('image_metadata.csv')
wipe_file('rules_saved.txt')

wipe_file('local_test_agent.py')

wipe_file('BACKOUT_tbl_testload.SQL')
wipe_file('CREATE_tbl_testload.SQL')
wipe_file('LOAD_tbl_testload.BAT')
wipe_file('tbl_testload.CTL')
wipe_file('test_src_file.csv')
