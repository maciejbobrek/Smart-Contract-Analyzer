
import subprocess


def slither_test(filepath):
   result = subprocess.run(['slither',filepath], 
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
   output=result.stderr.decode()
   length=len(output)
   warning_number= output.count('warn')
   error_number=output.count('err')
   call_number=output.count('Reference')
   return warning_number,error_number,call_number,length