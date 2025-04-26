
# Bookstore

## Project Overview
The **Bookstore** is a simple web application built using Django that allows users to manage books, authors, and categories. The project includes features for adding, updating, deleting, and viewing books, as well as managing the inventory of the bookstore. It is designed to be easily extendable with additional features such as user authentication and reviews.

## Setup & Run Instructions

### 1. Clone the Repository
To clone the repository, run the following command:

```bash
git clone https://github.com/omnhinge/bookstore.git
cd bookstore
```

### 2. Set Up a Virtual Environment
It's recommended to create a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install Dependencies
Install the required dependencies listed in the `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
Apply the database migrations to set up the necessary database tables:

```bash
python manage.py migrate
```

### 5. Run the Development Server
To run the application locally:

```bash
python manage.py runserver
```

Now, you can visit `http://127.0.0.1:8000/` in your browser.

## Tech Stack Used
- **Django**: A high-level Python web framework for rapid development.
- **PostgreSQL**: Used as the database for storing book and user data.
- **Docker**: For containerization, ensuring consistency across development and production environments.
- **Jenkins**: For Continuous Integration and Continuous Deployment (CI/CD).
  
## Screenshots
(Insert your app's screenshots here if available)

Example:

![Screenshot of Bookstore](screenshots)

## Docker and Jenkins Usage Notes

### Docker Usage

1. **Build the Docker image**:

   Run the following command to build the Docker image for the project:

   ```bash
   docker-compose build
   ```

2. **Run the Docker containers**:

   Start the application with Docker Compose:

   ```bash
   docker-compose up -d
   ```

   This will run the application in detached mode.

3. **Access the application**:

   After the containers are up, you can access the application at `http://localhost:8000/`.

### Jenkins Usage

- Jenkins is set up to run the CI/CD pipeline for building, testing, and deploying the application.
- The pipeline is defined in the **Jenkinsfile**.
- The pipeline includes stages for:
  1. **Checkout**: Pulling the latest code from the Git repository.
  2. **Build Docker Image**: Building a Docker image for the application.
  3. **Test**: Running tests in the container.
  4. **Deploy**: Deploying the application to production.
- To trigger the Jenkins pipeline, push your changes to the repository, and Jenkins will automatically pick up the changes and run the pipeline.

---

**Happy coding!** 😎
```


