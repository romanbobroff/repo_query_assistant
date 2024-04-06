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

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have met the following requirements:
- Docker installed on your machine
- Git installed on your machine

### Installing and Running with Docker

To set up and run the `repo_query_assistant` project using Docker, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/romanbobroff/repo_query_assistant.git
   cd repo_query_assistant
   ```
   Navigate to the directory containing the Dockerfile (if it's located in a specific subdirectory, adjust the path as necessary):
    ```
   cd docker
   ```
2. Build the Docker image:
   ```
   docker build -t repo_query_assistant .
   ```
3. Run the container from the image:
   ```
   docker run --name rq_assistant -d repo_query_assistant
    ```

## Contribution

We welcome contributions from the community. Please refer to our `CONTRIBUTING.md` file for guidelines on how to contribute to the project.

By adopting these practices, we aim to maintain a high standard of quality and a transparent, efficient workflow in the `repo_query_assistant` project.
