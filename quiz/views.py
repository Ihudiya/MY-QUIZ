from django.shortcuts import render, redirect
import random


TOPICS = {
    "software_architecture": {
        "name": "Software Architecture and Design",
        "description": "Explore system structures, design patterns, and software design principles.",
        "questions": [
            {
                "question": "What is the main purpose of software architecture?",
                "options": [
                    "To define the high-level structure of a software system",
                    "To write every line of code",
                    "To design only the user interface",
                    "To test individual variables",
                ],
                "answer": "To define the high-level structure of a software system",
            },
            {
                "question": "Which design pattern ensures that a class has only one instance?",
                "options": [
                    "Factory Pattern",
                    "Singleton Pattern",
                    "Observer Pattern",
                    "Adapter Pattern",
                ],
                "answer": "Singleton Pattern",
            },
    {
        "question": "What does high cohesion mean in software design?",
        "options": [
            "A module performs closely related tasks",
            "A system has many unrelated features",
            "All modules depend heavily on one another",
            "A program contains no functions",
        ],
        "answer": "A module performs closely related tasks",
    },
    {
        "question": "What is the main benefit of low coupling?",
        "options": [
            "Modules become harder to maintain",
            "Every module must use the same code",
            "Changes in one module have less impact on others",
            "The software no longer needs testing",
        ],
        "answer": "Changes in one module have less impact on others",
    },
            {
                "question": "Which principle encourages a software component to have one clear responsibility?",
                "options": [
                    "Single Responsibility Principle",
                    "Repeated Execution Principle",
                    "Multiple Inheritance Rule",
                    "Sequential Processing Principle",
                ],
                "answer": "Single Responsibility Principle",
            },
        ],
    },

    "software_testing": {
        "name": "Software Testing and Quality Assurance",
        "description": "Learn about test types, debugging, and software quality.",
        "questions": [
            {
                "question": "What is the main purpose of software testing?",
                "options": [
                    "To find defects and evaluate software quality",
                    "To increase the size of an application",
                    "To replace all documentation",
                    "To design computer hardware",
                ],
                "answer": "To find defects and evaluate software quality",
            },
            {
                "question": "Which design pattern ensures that a class has only one instance?",
                "options": [
                    "Factory Pattern",
                    "Singleton Pattern",
                    "Observer Pattern",
                    "Adapter Pattern",
                ],
                "answer": "Singleton Pattern",
            },
            {
                "question": "What does high cohesion mean in software design?",
                "options": [
                    "A module performs closely related tasks",
                    "A system has many unrelated features",
                    "All modules depend heavily on one another",
                    "A program contains no functions",
                ],
                "answer": "A module performs closely related tasks",
            },
            {
                "question": "What is the main benefit of low coupling?",
                "options": [
                    "Modules become harder to maintain",
                    "Every module must use the same code",
                    "Changes in one module have less impact on others",
                    "The software no longer needs testing",
                ],
                "answer": "Changes in one module have less impact on others",
            },
            {
                "question": "What is unit testing?",
                "options": [
                    "Testing individual components of software",
                    "Testing an entire organization",
                    "Testing only the website's appearance",
                    "Testing a computer's power supply",
                ],
                "answer": "Testing individual components of software",
            },
        ],
    },

    "data_structures": {
        "name": "Data Structures and Algorithms",
        "description": "Practise arrays, stacks, queues, trees, and algorithms.",
        "questions": [
            {
                "question": "Which data structure follows the Last In, First Out (LIFO) principle?",
                "options": [
                    "Stack",
                    "Queue",
                    "Graph",
                    "Linked list",
                ],
                "answer": "Stack",
            },
            {
                "question": "Which algorithm is commonly used to find the shortest path in a graph with non-negative edge weights?",
                "options": [
                    "Bubble Sort",
                    "Dijkstra's Algorithm",
                    "Binary Search",
                    "Insertion Sort",
                ],
                "answer": "Dijkstra's Algorithm",
            },
            {
                "question": "What is the time complexity of binary search on a sorted array?",
                "options": [
                    "O(n)",
                    "O(n²)",
                    "O(log n)",
                    "O(1) in every case",
                ],
                "answer": "O(log n)",
            },
            {
                "question": "Which data structure is commonly used to manage function calls?",
                "options": [
                    "Queue",
                    "Stack",
                    "Graph",
                    "Hash table",
                ],
                "answer": "Stack",
            },
            {
                "question": "Which data structure commonly follows the First In, First Out (FIFO) principle?",
                "options": [
                    "Queue",
                    "Stack",
                    "Binary search tree",
                    "Heap",
                ],
                "answer": "Queue",
            },
        ],
    },

    "requirements_analysis": {
        "name": "Software Requirements Analysis",
        "description": "Understand user needs, requirements, and software specifications.",
        "questions": [
            {
                "question": "What is requirements gathering?",
                "options": [
                    "Understanding what users need from software",
                    "Writing code before understanding the problem",
                    "Removing all project documentation",
                    "Testing computer hardware",
                ],
                "answer": "Understanding what users need from software",
            },
            {
                "question": "Which technique involves asking users questions to understand their needs?",
                "options": [
                    "Interviewing",
                    "Code compilation",
                    "Unit testing",
                    "Debugging",
                ],
                "answer": "Interviewing",
            },
            {
                "question": "What is a functional requirement?",
                "options": [
                    "A description of what the system should do",
                    "A description of the system's colour scheme only",
                    "A list of the developer's personal preferences",
                    "A requirement that describes hardware prices",
                ],
                "answer": "A description of what the system should do",
            },
            {
                "question": "What is the main purpose of requirements validation?",
                "options": [
                    "To confirm that requirements reflect stakeholders' actual needs",
                    "To begin coding without reviewing requirements",
                    "To remove all user feedback",
                    "To choose a programming language without analysis",
                ],
                "answer": "To confirm that requirements reflect stakeholders' actual needs",
            },
            {
                "question": "What does SRS stand for in Software Engineering?",
                "options": [
                    "Software Requirements Specification",
                    "System Repair Service",
                    "Software Runtime Sequence",
                    "Standard Resource Storage",
                ],
                "answer": "Software Requirements Specification",
            },
        ],
    },

    "programming_oop": {
        "name": "Programming and Object-Oriented Programming",
        "description": "Explore programming concepts, functions, classes, and objects.",
        "questions": [
            {
                "question": "Which of these is a programming language?",
                "options": [
                    "Python",
                    "HTML",
                    "Windows",
                    "Google",
                ],
                "answer": "Python",
            },
            {
                "question": "What is encapsulation in object-oriented programming?",
                "options": [
                    "Bundling data and methods together while controlling access",
                    "Repeating the same code without a purpose",
                    "Deleting all objects from a program",
                    "Converting every variable into a function",
                ],
                "answer": "Bundling data and methods together while controlling access",
            },
            {
                "question": "What is inheritance in object-oriented programming?",
                "options": [
                    "A class acquiring properties or behaviours from another class",
                    "A method running without being called",
                    "A program storing data only in files",
                    "A technique for removing all classes",
                ],
                "answer": "A class acquiring properties or behaviours from another class",
            },
            {
                "question": "What is a function in programming?",
                "options": [
                    "A reusable block of code that performs a task",
                    "A physical part of a computer",
                    "A type of internet connection",
                    "A folder that must contain images",
                ],
                "answer": "A reusable block of code that performs a task",
            },
            {
                "question": "In object-oriented programming, what is a class?",
                "options": [
                    "A blueprint for creating objects",
                    "A type of database table only",
                    "A tool for testing internet speed",
                    "A folder containing images only",
                ],
                "answer": "A blueprint for creating objects",
            },
        ],
    },

    "databases": {
        "name": "Database Management",
        "description": "Practise SQL, keys, relationships, and database design.",
        "questions": [
            {
                "question": "What is the main purpose of a primary key in a database table?",
                "options": [
                    "To uniquely identify each record",
                    "To make every record identical",
                    "To store only images",
                    "To remove all relationships",
                ],
                "answer": "To uniquely identify each record",
            },
            {
                "question": "What is a foreign key used for in a relational database?",
                "options": [
                    "To link records between related tables",
                    "To encrypt every database record",
                    "To replace all primary keys",
                    "To change the database colour",
                ],
                "answer": "To link records between related tables",
            },
            {
                "question": "Which SQL command retrieves data from a database?",
                "options": [
                    "INSERT",
                    "DELETE",
                    "SELECT",
                    "UPDATE",
                ],
                "answer": "SELECT",
            },
            {
                "question": "What is database normalization primarily intended to reduce?",
                "options": [
                    "Data redundancy and update anomalies",
                    "The number of users allowed",
                    "The need for database tables",
                    "The speed of every query",
                ],
                "answer": "Data redundancy and update anomalies",
            },
            {
                "question": "Which language is commonly used to query relational databases?",
                "options": [
                    "SQL",
                    "HTML",
                    "CSS",
                    "XML",
                ],
                "answer": "SQL",
            },
        ],
    },

    "development_process": {
        "name": "Software Development Process",
        "description": "Learn about SDLC, Agile, Scrum, and development methods.",
        "questions": [
            {
                "question": "What does SDLC stand for?",
                "options": [
                    "Software Development Life Cycle",
                    "System Data Language Code",
                    "Software Design List Control",
                    "Standard Development Logic Class",
                ],
                "answer": "Software Development Life Cycle",
            },
            {
                "question": "Which phase of the SDLC focuses on identifying what the software must do?",
                "options": [
                    "Requirements analysis",
                    "Deployment",
                    "Maintenance",
                    "Coding",
                ],
                "answer": "Requirements analysis",
            },
            {
                "question": "What is a major characteristic of the Waterfall development model?",
                "options": [
                    "Work proceeds through phases in a largely sequential order",
                    "There are no planned development phases",
                    "All testing is permanently skipped",
                    "Users write every line of code",
                ],
                "answer": "Work proceeds through phases in a largely sequential order",
            },
            {
                "question": "What is the main purpose of a software prototype?",
                "options": [
                    "To explore or demonstrate a proposed solution before full development",
                    "To replace every stage of software development",
                    "To guarantee that no bugs will occur",
                    "To store all project passwords",
                ],
                "answer": "To explore or demonstrate a proposed solution before full development",
            },
            {
                "question": "Which development approach organizes work into short, iterative cycles called sprints?",
                "options": [
                    "Scrum",
                    "Waterfall",
                    "Big bang development",
                    "Code-and-forget",
                ],
                "answer": "Scrum",
            },
        ],
    },

    "uml_modelling": {
        "name": "Software Modelling and UML",
        "description": "Practise use-case, class, sequence, and activity diagrams.",
        "questions": [
            {
                "question": "Which UML diagram shows interactions between actors and a system's use cases?",
                "options": [
                    "Use-case diagram",
                    "Class diagram",
                    "Deployment diagram",
                    "Object diagram",
                ],
                "answer": "Use-case diagram",
            },
            {
                "question": "Which UML diagram represents the structure of classes and their relationships?",
                "options": [
                    "Sequence diagram",
                    "Class diagram",
                    "Use-case diagram",
                    "Activity diagram",
                ],
                "answer": "Class diagram",
            },
            {
                "question": "What does an actor represent in a UML use-case diagram?",
                "options": [
                    "A person or external system that interacts with the system",
                    "A database table",
                    "A programming error",
                    "A method inside every class",
                ],
                "answer": "A person or external system that interacts with the system",
            },
            {
                "question": "Which UML diagram is best for representing the flow of activities in a process?",
                "options": [
                    "Class diagram",
                    "Deployment diagram",
                    "Activity diagram",
                    "Object diagram",
                ],
                "answer": "Activity diagram",
            },
            {
                "question": "Which UML diagram shows the messages exchanged between objects over time?",
                "options": [
                    "Sequence diagram",
                    "Use-case diagram",
                    "Package diagram",
                    "Component diagram",
                ],
                "answer": "Sequence diagram",
            },
        ],
    },

    "git_github": {
        "name": "Git and GitHub",
        "description": "Learn version control, repositories, branches, and collaboration.",
        "questions": [
            {
                "question": "What is Git mainly used for?",
                "options": [
                    "Version control",
                    "Creating presentation slides",
                    "Managing computer hardware",
                    "Editing photographs",
                ],
                "answer": "Version control",
            },
            {
                "question": "Which Git command creates a new commit from staged changes?",
                "options": [
                    "git push",
                    "git commit",
                    "git pull",
                    "git status",
                ],
                "answer": "git commit",
            },
            {
                "question": "What is the purpose of a Git repository?",
                "options": [
                    "To track and manage changes to files",
                    "To increase a computer's RAM",
                    "To design website layouts",
                    "To host video calls only",
                ],
                "answer": "To track and manage changes to files",
            },
            {
                "question": "What does git clone do?",
                "options": [
                    "Deletes a remote repository",
                    "Copies an existing repository to your computer",
                    "Renames every file in a project",
                    "Automatically fixes all code errors",
                ],
                "answer": "Copies an existing repository to your computer",
            },
            {
                "question": "What is a Git branch commonly used for?",
                "options": [
                    "Developing changes separately from another line of work",
                    "Deleting the entire repository automatically",
                    "Replacing the programming language",
                    "Increasing internet speed",
                ],
                "answer": "Developing changes separately from another line of work",
            },
        ],
    },

    "project_management": {
        "name": "Software Project Management",
        "description": "Explore project planning, estimation, risks, and maintenance.",
        "questions": [
            {
                "question": "Why is project scheduling important in software development?",
                "options": [
                    "It helps plan tasks and track timelines",
                    "It guarantees that software has no defects",
                    "It eliminates the need for communication",
                    "It automatically writes all the code",
                ],
                "answer": "It helps plan tasks and track timelines",
            },
            {
                "question": "What is risk management in software projects?",
                "options": [
                    "Identifying and addressing potential problems",
                    "Ignoring problems until the project ends",
                    "Removing the need for project planning",
                    "Guaranteeing that the project costs nothing",
                ],
                "answer": "Identifying and addressing potential problems",
            },
            {
                "question": "What is a project milestone?",
                "options": [
                    "A significant point or event in a project",
                    "A programming language",
                    "A type of database",
                    "A tool used only for graphic design",
                ],
                "answer": "A significant point or event in a project",
            },
            {
                "question": "Why is project cost estimation important?",
                "options": [
                    "To help plan the budget and allocate resources",
                    "To guarantee that no changes will occur",
                    "To eliminate the need for developers",
                    "To determine the colour of the user interface",
                ],
                "answer": "To help plan the budget and allocate resources",
            },
            {
                "question": "What is software maintenance?",
                "options": [
                    "Modifying software after delivery to fix or improve it",
                    "Writing requirements without developing software",
                    "Installing a computer keyboard",
                    "Creating a logo before planning a project",
                ],
                "answer": "Modifying software after delivery to fix or improve it",
            },
        ],
    },
}




def home(request):
    return render(request, "quiz/home.html", {
        "topics": TOPICS,
    })



def start_quiz(request, topic_slug=None):
    is_mixed = topic_slug == "mixed"

    # Get questions for the selected quiz
    if is_mixed:
        questions = []
        for topic in TOPICS.values():
            questions.extend(topic["questions"])

        quiz_title = "Mixed Challenge"
    elif topic_slug in TOPICS:
        topic = TOPICS[topic_slug]
        questions = topic["questions"]
        quiz_title = topic["name"]
    else:
        return redirect("home")

    # Start a fresh Mixed Challenge session
    if request.method == "GET":
        if is_mixed:
            request.session["mixed_used"] = []
            request.session["mixed_round"] = 1

        if is_mixed:
            used = request.session.get("mixed_used", [])
            available = [
                q for q in questions
                if q["question"] not in used
            ]
            random.shuffle(available)
            round_questions = available[:20]
            request.session["mixed_current"] = [
                q["question"] for q in round_questions
            ]
        else:
            round_questions = questions

        request.session["quiz_questions"] = round_questions
        request.session["quiz_title"] = quiz_title
        request.session["is_mixed"] = is_mixed

        return render(request, "quiz/questions.html", {
            "questions": round_questions,
            "quiz_title": quiz_title,
        })

    # Mark submitted answers
    if request.method == "POST":
        round_questions = request.session.get("quiz_questions", [])
        quiz_title = request.session.get("quiz_title", quiz_title)
        is_mixed = request.session.get("is_mixed", is_mixed)

        score = 0
        results = []

        for index, question in enumerate(round_questions):
            selected = request.POST.get(f"question_{index}")
            correct = selected == question["answer"]

            if correct:
                score += 1

            results.append({
                "question": question["question"],
                "selected": selected,
                "answer": question["answer"],
                "correct": correct,
            })

        total = len(round_questions)
        percentage = round((score / total) * 100) if total else 0

        if is_mixed:
            used = request.session.get("mixed_used", [])
            used.extend(
                q["question"]
                for q in round_questions
                if q["question"] not in used
            )
            request.session["mixed_used"] = used

        request.session["last_score"] = score
        request.session["last_total"] = total
        request.session["last_percentage"] = percentage
        request.session["last_results"] = results
        request.session["last_quiz_title"] = quiz_title
        request.session["last_is_mixed"] = is_mixed
        
        #     if is_mixed:
        # return render(request, "quiz/questions.html", {
        #     "questions": [
        #         {
        #             **question,
        #             "selected": results[index]["selected"],
        #             "correct": results[index]["correct"],
        #         }
        #         for index, question in enumerate(round_questions)
        #     ],
        #     "quiz_title": quiz_title,
        #     "is_mixed": True,
        #     "submitted": True,
        #     "score": score,
        #     "total": total,
        #     "percentage": percentage,
        #     "quiz_slug": "mixed",
        #     "has_more_questions": len(request.session.get("mixed_used", []))
        #     <escape><</escape> sum(len(t["questions"]) for t in TOPICS.values()),
        # })

        return redirect("quiz_results")

    return redirect("home")


def quiz_results(request):
    return render(request, "quiz/results.html", {
        "score": request.session.get("last_score", 0),
        "total": request.session.get("last_total", 0),
        "percentage": request.session.get("last_percentage", 0),
        "results": request.session.get("last_results", []),
        "quiz_title": request.session.get("last_quiz_title", "Quiz Results"),
        "is_mixed": request.session.get("last_is_mixed", False),
        "round_number": request.session.get("mixed_round", 1),
        "has_more_questions": bool(
            request.session.get("last_is_mixed", False)
            and len(request.session.get("mixed_used", [])) < sum(
                len(t["questions"]) for t in TOPICS.values()
            )
        ),
    })


def next_round(request):
    if request.method != "POST":
        return redirect("home")

    used = request.session.get("mixed_used", [])
    questions = [
        q
        for topic in TOPICS.values()
        for q in topic["questions"]
        if q["question"] not in used
    ]

    if not questions:
        return redirect("home")

    random.shuffle(questions)
    round_questions = questions[:20]

    request.session["mixed_round"] = (
        request.session.get("mixed_round", 1) + 1
    )
    request.session["quiz_questions"] = round_questions
    request.session["quiz_title"] = "Mixed Challenge"
    request.session["is_mixed"] = True
    request.session["mixed_current"] = [
        q["question"] for q in round_questions
    ]

    return render(request, "quiz/questions.html", {
        "questions": round_questions,
        "quiz_title": "Mixed Challenge — Round "
        + str(request.session["mixed_round"]),
    })
