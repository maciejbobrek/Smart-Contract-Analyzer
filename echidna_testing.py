
import os
import subprocess


def echidna_test(filepath):
   result = subprocess.run(['echidna',filepath], 
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
   output=result.stderr.decode()
   length=len(output)
   return length