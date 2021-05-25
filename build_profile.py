def build_profile(first_name,last_name,**user_info):
    profile={}
    profile['f_name']=first_name
    profile['l_name']=last_name
    
    for key,value in user_info.items():
        profile[key]=value
    return profile