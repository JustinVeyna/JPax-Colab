import SaveLoader as sl
from collections import defaultdict

PROGRESS_FILE = "data_files/SavedProgress.p"

def load_progress_from_file():
    char_dict = defaultdict(int)
    try:
        char_dict = sl.pickle_load(PROGRESS_FILE)
    except:
        sl.pickle_save(defaultdict(int), PROGRESS_FILE)
        return defaultdict(int)
    return char_dict

if __name__ == "__main__":
    print(load_progress_from_file())
        
        
   
        
        
        
        
    
