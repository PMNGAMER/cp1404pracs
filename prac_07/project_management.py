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

def save_projects(filename, projects):
    with open(filename, 'w') as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for p in projects:
            print(f"{p.name}\t{p.start_date.strftime('%d/%m/%Y')}\t{p.priority}\t{p.cost_estimate}\t{p.completion_percentage}", file=out_file)

def sort_by_date(projects):
    for i in range(len(projects)):
        for j in range(i + 1, len(projects)):
            if projects[j].start_date < projects[i].start_date:
                temp = projects[i]
                projects[i] = projects[j]
                projects[j] = temp
    return projects

def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    percent = int(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost, percent)
    projects.append(new_project)

def update_project(projects):
    for i in range(len(projects)):
        print(i, projects[i])

    index_input = input("Project choice: ")
    index = int(index_input)
    selected_project = projects[index]
    print(selected_project)

    percent_input = input("New Percentage: ")
    priority_input = input("New Priority: ")

    if percent_input != "":
        selected_project.completion_percentage = int(percent_input)
    if priority_input != "":
        selected_project.priority = int(priority_input)

def save_projects(filename, projects):
    out_file = open(filename, 'w')
    print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
    for p in projects:
        line = f"{p.name}\t{p.start_date.strftime('%d/%m/%Y')}\t{p.priority}\t{p.cost_estimate}\t{p.completion_percentage}"
        print(line, file=out_file)
    out_file.close()


def filter_projects_by_date(projects):
    date_input = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        user_date = datetime.strptime(date_input, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Use dd/mm/yyyy")
        return

    filtered_projects = []
    for project in projects:
        if project.start_date > user_date:
            filtered_projects.append(project)

    filtered_projects = sort_by_date(filtered_projects)
    for project in filtered_projects:
        print(project)


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
    while choice != "q":
        if choice == "l":
            filename = input("Filename to load: ")
            projects = load_projects(filename)
            print("Loaded", len(projects), "projects from", filename)
        elif choice == "s":
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
            print("Projects saved to", filename)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("Function not implemented yet.")
        print(MENU)
        choice = input(">>> ").lower()
    save_prompt = input("Would you like to save to " + filename + "? ").lower()
    if save_prompt == "yes" or save_prompt == "y":
        save_projects(filename, projects)
        print("Projects saved to", filename)

    print("Thank you for using custom-built project management software.")



main()
