# project/db_create_script.py

try:
    from project.models import *
    from project.new_report import *
except ModuleNotFoundError:
    from models import *
    from new_report import *

import argparse



def init_db(db_path):
    db_sq = SqliteDatabase(db_path)
    data_base.initialize(db_sq)
    OriginReport.create_table()


def fill_db(folder_path):
    build = build_report(folder_path)
    rep = sort_report(build, 'asc')
    for abbr, item in rep.items():
        db = OriginReport(
            abbr=item['abbr'],
            name=item['name'],
            team=item['team'],
            duration=item['duration'],
            start=item['start'],
            end=item['end']
        )
        db.save()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--db_path", dest='db', help='Input path to the database')
    parser.add_argument('--folder_path', dest="folder_path", help="Input path to the data files folder")

    args = parser.parse_args()
    if args.db and args.folder_path:
        init_db(db_path=args.db)
        fill_db(folder_path=args.folder_path)
    else:
        print(
            "You must input arguments properly. Example: python db_create_script.py --db_path 'some.db' --folder_path "
            "'./some_folder/data_folder'")
