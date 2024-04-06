# repo_query_assistant
Studying project using large language models to analyze code repositories

# Repository Management Methodology

## Overview

In the `repo_query_assistant` project, we follow a structured methodology to ensure consistent progress and quality in our development process. This methodology encompasses task management, coding practices, testing, and release strategies.

## Task Management

- **Notion for Project Management:** We utilize Notion as our central tool for managing the project. It serves as a single source of truth for all project-related information, including planning, documentation, and progress tracking.
- **Kanban Model:** Our workflow is based on the Kanban model, which allows us to visualize work at various stages. In Notion, we set up Kanban boards to track tasks from inception to completion, categorizing them into columns like To Do, In Progress, and Done. This approach helps us maintain a clear overview of the workload and prioritize tasks efficiently.
- **Continuous Flow:** By adhering to Kanban principles, we focus on continuous delivery of tasks, minimizing bottlenecks and ensuring a steady flow of work. This method allows us to quickly adapt to changes and prioritize tasks that deliver the most value to the project.
- **Collaboration and Transparency:** Notion facilitates collaboration among team members and provides transparency in the project's progress. Every team member has access to the board, which fosters a collaborative environment and ensures that everyone is aligned with the project's goals and current status.

## Coding Practices

- **Branching Strategy:** We adhere to the Git Flow branching model. Development work is done in feature branches, which are merged into the `dev` branch upon completion. The `main` branch is reserved for production releases.
- **Code Reviews:** Every pull request must be reviewed by at least one team member before merging to ensure code quality and adherence to project standards.

## Testing

- **Automated Tests:** We strive to cover our code with unit and integration tests. Tests are run automatically via CI pipelines on every pull request to the `dev` and `main` branches.
- **Manual Testing:** For significant features, manual testing is also performed to ensure functionality meets our standards and user expectations.

## Release Strategy

- **Versioning:** We follow Semantic Versioning (SemVer) for our releases. This approach helps us to track changes and manage version compatibility.
- **Continuous Integration and Delivery (CI/CD):** Our CI/CD pipelines automate the testing and deployment processes, enabling us to release frequently and with confidence.

## Contribution

We welcome contributions from the community. Please refer to our `CONTRIBUTING.md` file for guidelines on how to contribute to the project.

By adopting these practices, we aim to maintain a high standard of quality and a transparent, efficient workflow in the `repo_query_assistant` project.