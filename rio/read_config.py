
def read_configfile():
    import yaml
    
# Open the config file
######################
    with open("config_RIOcalc.yml","r") as ymlfile:
         configs = yaml.load(ymlfile)
    
# Derived setting variables and sanity checks
###############################################
# a) Read NCAT, do sanity checks and set configs['multiCAT'] flag
# b) Set configs['Lvol'] flag based on whether thickness or volume variable is provided
    
    # Mono-category
    if configs['coordinates']['ncat'] == 1:
        configs['multiCAT']=False
        if configs['variables']['siconc_name']==None:
            raise RuntimeError("IF NCAT is 1, you need to specify 'siconc_name'")
        if configs['variables']['sithick_name']==None and configs['variables']['sivol_name']==None :
            raise RuntimeError("IF NCAT is 1, you need to specify either 'sithick_name' or 'sivol_name'")
        else:
            if configs['variables']['sithick_name']==None:
                configs['Lvol']=True
            else:
                configs['Lvol']=False
    
    # Multi-category
    elif configs['coordinates']['ncat'] > 1:
        configs['multiCAT']=True
        if configs['coordinates']['ncat_name']==None:
            raise RuntimeError("IF NCAT > 1, you have to provide the name of the ice category dimension NCAT_NAME.")
        if configs['variables']['siitdconc_name']==None:
            raise RuntimeError("IF NCAT is >1, you need to specify 'siitdconc_name'")
        if configs['variables']['siitdthick_name']==None and configs['variables']['siitdvol_name']==None :
            raise RuntimeError("IF NCAT is >1, you need to specify either 'siitdthick_name' or 'siitdvol_name'")
        else:
            if configs['variables']['siitdthick_name']==None:
                configs['Lvol']=True
            else:
                configs['Lvol']=False
    
    else:
        raise RuntimeError("NCAT needs to be positive > 0.") 
    
# c) Make sure that only one of Lthick, Lage or Lsal is set.
    if sum([configs['RIOmethod'][i] for i in configs['RIOmethod']]) != 1:
        raise RuntimeError("You need to set exactly one of Lthick, Lage or Lsal to True.")
    
# d) Check that siage and sisali variables are given
    if configs['RIOmethod']['Lage'] and configs['variables']['siage_name']==None:
        raise RuntimeError("If 'Lage' is true, you need to provide 'siage_name'.")
    if configs['RIOmethod']['Lsal'] and configs['variables']['sisali_name']==None:
        raise RuntimeError("If 'Lsal' is true, you need to provide 'sisali_name'.")
        
# e) Check if ship classes make sense 
    
    
    return configs
