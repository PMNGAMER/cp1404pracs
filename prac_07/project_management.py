from project import Project


def load_projects(filename):
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            project = Project(*parts)
            projects.append(project)
    return projects


def display_projects(projects):
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]

    print("Incomplete projects:")
    for p in sorted(incomplete):
        print(f"  {p}")

    print("Completed projects:")
    for p in sorted(complete):
        print(f"  {p}")


def main():
    print("Welcome to Pythonic Project Management")
    filename = "projects.txt"
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from {filename}")

    MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""
    print(MENU)

    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'd':
            display_projects(projects)
        else:
            print("Function not implemented yet.")
        print(MENU)
        choice = input(">>> ").lower()

    print("Thank you for using custom-built project management software.")



main()
