import re
import os

class InvalidTaskIDError(Exception):
    """Raises when given task_id is not unique or not valid."""

class FolderCreator:
    TASK_ID_PATTERN = r"^[a-zA-Z0-9][a-zA-Z0-9_]*[a-zA-Z0-9]$"
    TASKS_FOLDER_PATH = "tasks"
    SOLUTION_TEMPLATE = (
        "class Solution:\n"
        "    # your code here\n"
        "    pass\n\n\n"
        "if __name__ == \"__main__\":\n"
        "    solution = Solution()\n"
        "    # testcases\n"
    )

    @staticmethod
    def create(task_id: str) -> None:
        path_to_task_folder = FolderCreator._create_task_folder(
            task_id=task_id
        )
        os.makedirs(path_to_task_folder)

        path_to_solution = os.path.join(path_to_task_folder, f"solution.py")
        with open(path_to_solution, 'w') as file:
            file.write(FolderCreator.SOLUTION_TEMPLATE)

        readme_header = " ".join(map(str.capitalize, task_id.split("_")))
        readme_header = f"# {readme_header}"

        path_to_readme = os.path.join(path_to_task_folder, "README.md")
        with open(path_to_readme, 'w') as file:
            file.write(readme_header)

    @staticmethod
    def _create_task_folder(task_id: str) -> str:
        if not re.match(FolderCreator.TASK_ID_PATTERN, task_id):
            raise InvalidTaskIDError(
                f"task_id must match next template: {FolderCreator.TASK_ID_PATTERN}"
            )

        path_to_task_folder = os.path.join(FolderCreator.TASKS_FOLDER_PATH, task_id)
        if os.path.exists(path_to_task_folder):
            raise InvalidTaskIDError(
                f"folder with task_id {task_id} already exists"
            )

        return path_to_task_folder