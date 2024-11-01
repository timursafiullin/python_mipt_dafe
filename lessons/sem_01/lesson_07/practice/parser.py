from argparse import ArgumentParser

parser = ArgumentParser(
    description=(
        "There is a script to create template"
        "folder for leetcode75 task solutions"
    )
)

parser.add_argument(
    '--task-id',
    type=str,
    help='ID for new task'
)
