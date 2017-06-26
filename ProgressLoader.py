import SaveLoader as SL
from collections import defaultdict


def load_progress_from_file():
    #returns list of [current character, base url, saved post id] in this order.
    #return None if no saved progress.
    char_dict = defaultdict(int)
    try:
        char_dict = pickle_load("SavedProgress.p","r")
        
    except:
        print("No saved progress currently. Proceeding from beginning.")
        return None
    
    else:
        if char_dict.len() == 0:
            print("Progress file is empty. Proceeding from beginning.")
            return None
        else:
            return char_dict
        
    finally:
        print("Progress loaded.")
        
        
   
        
        
        
        
    
