# document_AIKIF.py written by Duncan Murray 18/4/2014
# 
#   As at 26/8/2014: All Python Program Statistics
#  Files =  110  Bytes =  377221  Lines =  10694  Lines of Code =  8836
import sys
import os
sys.path.append('..')

import cls_programs as prog
import aikif.lib.cls_filelist as mod_fl
import aikif.lib.cls_file as mod_file

# because we are calling it several times for testing, clean the files first
#filemap.GetFullFilename(filemap.FindType('LOCATION'), filemap.FindOntology('FILE-PROGRAM')[0]))   	
#filemap.GetFullFilename(filemap.FindType('OBJECT'), filemap.FindOntology('FILE-PROGRAM')[0]))   	
os.remove('..\\..\\data\\core\\LOCATION_SYSTEM-PC-FILE-PROGRAM.CSV')   	
os.remove('..\\..\\data\\core\\OBJECT_SYSTEM-PC-FILE-PROGRAM.CSV')   	



aikifProgs = prog.Programs('AIKIF Programs', 'T:\\user\\dev\\src\\python\\AIKIF')
aikifProgs.add('program.py', 'test program')
aikifProgs.add('fileMapping.py', 'uses ontology to get list of files to save data')
aikifProgs.add('index.py', 'rebuilds indexes')
aikifProgs.add('view.py', 'view the data in AIKIF')
aikifProgs.add('AIKIF_utils.py', 'utils for getting standard file structures (soon to be deprecated)')
aikifProgs.add('AI.py', 'original main entry point - soon to be deprecated')
aikifProgs.add('add.py', 'command line utility to add information - not yet implemented')
aikifProgs.add('dataTools.py', 'data tools to manage database access')
aikifProgs.add('AIKIF_create.py', 'creates default structures with test data')
aikifProgs.add('generateTestData.py', 'Tool to generate various test data')
aikifProgs.add('processRawData.py', 'calls various sub tasks to collect raw data')
aikifProgs.add('loadInfoCourseLectures.py', 'loads course lecture notes into AIKIF')
aikifProgs.add('loadPIM_Filelist.py', 'loads generic filelists into AIKIF - indexing not implemented')
aikifProgs.add('loadCountry_Gdeltproject.py', 'sample load - loads country data into AIKIF')
aikifProgs.add('loadPIM_shoppingList.py', 'sample data - loads a users shopping list into AIKIF')
aikifProgs.add('security.py', 'future module to handle security and privacy settings')


aikifProgs.list()	# get list of all programs
aikifProgs.save()


# Get list of applications
apps = prog.Programs('Applications', 'C:\\apps')
fl = mod_fl.FileList(['C:\\apps'], ['*.exe'], ["\\bk\\"])
for file in fl.get_list():
	apps.add(file, 'autogenerated list')
apps.list()
apps.save()

# List all python programs
allPython = prog.Programs('All Python Programs', 'T:\\user\\dev\\src\\python\\AIKIF\\aikif')
tot_lines = 0
tot_bytes = 0
tot_files = 0
tot_loc = 0
fl = mod_fl.FileList(['T:\\user\\dev\\src\\python\\AIKIF'], ['*.py'], ["__pycache__", ".git", "\\sympy-master\\", "\\z_bk_python\\", "\\ext-dl\\"])
for file in fl.get_list():
    allPython.add(file, 'autogenerated list')
    f = mod_file.TextFile(file)
    tot_lines += f.count_lines_in_file()
    tot_loc += f.count_lines_of_code()
    tot_bytes += f.size
    tot_files += 1
    
    print(file)

print('All Python Program Statistics')
print('Files = ', tot_files, ' Bytes = ', tot_bytes, ' Lines = ', tot_lines, ' Lines of Code = ', tot_loc)
    
allPython.save('all_programs.csv')