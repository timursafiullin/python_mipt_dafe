from folder_creator import FolderCreator
from parser import parser

if  __name__ == "__main__":
    args = parser.parse_args()
    FolderCreator.create(args.task_id)