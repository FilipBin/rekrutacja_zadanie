# Properties
# ==========
# OBJECT NAME: main
# DESCRIPTION: initializing file

# Revision history
# ==========================================================================================
# ChangeDate    Author  Version     Narrative
# 2023-11-29    FB      branch1     Created
# 2023-11-29    FB      branch1     Code formatting and removing drop tables statements
# ==========    ======  =======     ========================================================

import initialization
import create_db


def main():

    # create_db.CreateDb()
    initialization.start()


if __name__ == "__main__":
    main()
