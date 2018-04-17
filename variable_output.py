from io import StringIO  # Python3
 
 
import sys
 
# Store the reference, in case you want to show things again in standard output
 
old_stdout = sys.stdout
 
# This variable will store everything that is sent to the standard output
 
result = StringIO()
 
sys.stdout = result
 
print('ok')
 

 
# Redirect again the std output to screen
 
sys.stdout = old_stdout
 
# Then, get the stdout like a string and process it!
 
result_string = result.getvalue()
 

