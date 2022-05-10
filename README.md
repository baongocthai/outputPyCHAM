# outputPyCHAM
 Post process output from PyCHAM
 - species information include name, molecular weight (g/mol) and O/C molar ratio
 - gas phase concentration for individual species per time step
 - particulate phase concentration for individual species (1) per size bins and (2) per time step
 - ariable needed in functions can be get from out_process.py. For example, if variable 'time' is needed in one function:
   import out_process as op
   time = op.time
 - run out_process.py can generate files included in out_process file
