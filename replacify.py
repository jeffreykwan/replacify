import os, sys

folder = sys.argv[1] 
separ = os.sep

for n in os.listdir(folder):
   sys.stdout.write(n)
   if os.path.isfile(folder + separ + n):
      filename_zero, extension = os.path.splitext(n)
      newfilename = filename_zero.replace('-', ' ').replace('.', ' ').replace('_',' ').replace('  ', ' ') 
      os.rename(folder + separ + n , folder + separ + newfilename + extension)
   sys.stdout.write("---->")
   sys.stdout.write(newfilename)
   print extension
