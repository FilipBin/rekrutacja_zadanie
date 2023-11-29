# Properties
# ==========
# OBJECT NAME: save_dataframe_to_csv
# DESCRIPTION: this file is to save dataframe to csv file

# Revision history
# ==========================================================================================
# ChangeDate    Author  Version     Narrative
# 2023-11-29    FB      branch1     Created
# ==========    ======  =======     ========================================================

import support
import pandas as pd
import os



def save_df_to_csv(dataframe, filename):
    df = pd.DataFrame(dataframe)
    output_path = os.path.join(support.path_to_csv, filename)

    try:
        df.to_csv(output_path, index=False)
        print(f"File '{filename}' successfully created at: {output_path}")
    except Exception as e:
        print(f"Error: {e}")
        print(f"File '{filename}' could not be created.")
