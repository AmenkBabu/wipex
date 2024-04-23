#!/usr/bin/env python3

import argparse
from wipex.core.database_updater import DatabaseUpdater

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WiPEx Database Updater")
    parser.add_argument("-d", "--database", required=True, help="Path to the database file")
    args = parser.parse_args()

    database_updater = DatabaseUpdater()
    database_updater.update_database(args.database)
