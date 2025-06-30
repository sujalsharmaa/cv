import pandas as pd
import random
import datetime # Import for better file naming

def create_csv():
    """
    Generates a CSV file containing mock student data including names,
    roll numbers, and marks in English, Maths, and Computer Science.
    The CSV file is named 'Student_list-YYYYMMDD_HHMMSS.csv'.
    """
    names = []
    roll_no = []
    english_marks = []
    maths_marks = []
    cs_marks = []

    for i in range(1000): # Looping from 0 to 999 directly
        name = f'stuart-{random.randint(0, 1000)}-gary-{random.randint(0, 1000)}'
        names.append(name)
        
        roll_no.append(i + 1) # Start roll numbers from 1 for better human readability
        
        english_mark = random.randint(0, 100)
        maths_mark = random.randint(0, 100)
        cs_mark = random.randint(0, 100)
        
        english_marks.append(english_mark)
        cs_marks.append(cs_mark)
        maths_marks.append(maths_mark)

    df = pd.DataFrame({
        'name': names, # Changed to 'name' for consistency
        'roll_no': roll_no,
        'english_marks': english_marks,
        'maths_marks': maths_marks,
        'cs_marks': cs_marks
    })
    
    # Generate a timestamp for the filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'Student_list-{timestamp}.csv'
    
    # Save to CSV, excluding the DataFrame index
    df.to_csv(filename, index=False)
    
    print(f'Students marks data has been generated successfully as {filename}')

# Call the function to create the CSV
create_csv()