import argparse
from myapp.migration.switcher import switcher
def run():
    print("APP is running...")
    parser = argparse.ArgumentParser()
    parser.add_argument("src_db", help="source database type")
    parser.add_argument("tar_db", help="target database type")
    parser.add_argument("tar_db_name", help="tar_db_name or tar")
    group1 = parser.add_mutually_exclusive_group()  # exclusive group for reading either file or from table
    group1.add_argument('-f', '--file', help="tables details: YAML file")
    group1.add_argument('-t', '--table', help="src_schema_name.src_table_name")
    parser.add_argument('-o', '--overwrite', help='overwrite existing table/collection', action='store_true')
    args = parser.parse_args()
    migration_details = {}
    migration_details['src_db'] = args.src_db.lower()
    migration_details['tar_db'] = args.tar_db.lower()
    migration_details['tar_db_name'] = args.tar_db_name.lower()
    if args.file:
        migration_details['file'] = args.file
    elif args.table:
        migration_details['table'] = args.table
    if args.overwrite:
        migration_details['overwrite'] = True
    switcher(migration_details)
