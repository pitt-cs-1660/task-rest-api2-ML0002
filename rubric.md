# **Task Manager API Assignment Grading Rubric**

## **Overview**

In this assignment, you will implement the **Task Manager API** using the Python **FastAPI** web framework and **SQLite**. Your API must support CRUD operations (`GET`, `POST`, `PUT`, `DELETE`) for managing tasks. Your implementation will be graded automatically based on the results of the provided `pytest` tests, which will be run in **GitHub Actions** to ensure that your implementation works correctly on the `main` branch.

---

## **Grading Rubric**

Each test case is worth **3 points**. The total score for the assignment is **15 points**.

| **Test Name**     | **Description**                                | **Points** |
|-------------------|-------------------------------------------------|------------|
| `test_read_root`  | Tests the root endpoint (`GET /`).               | 3 points   |
| `test_create_task`| Tests creating a task (`POST /tasks/`).          | 3 points   |
| `test_get_tasks`  | Tests retrieving all tasks (`GET /tasks/`).      | 3 points   |
| `test_update_task`| Tests updating a task (`PUT /tasks/{task_id}/`). | 3 points   |
| `test_delete_task`| Tests deleting a task (`DELETE /tasks/{task_id}/`). | 3 points   |

---

## **Total Score: 15 Points**

Your score will be based on the number of tests passed:
- **5/5 tests passed:** 15 points
- **4/5 tests passed:** 12 points
- **3/5 tests passed:** 9 points
- **2/5 tests passed:** 6 points
- **1/5 tests passed:** 3 points
- **0/5 tests passed:** 0 points

---

## **Test Descriptions**

### **1. `test_read_root`**
- **Route:** `GET /`
- **Purpose:** Tests that the API returns the correct welcome message.
- **Expected Output:**
  ```json
  {"message": "Welcome to the Cloud Computing!"}
  ```
- **Criteria:** Passes if the response status is `200 OK` and the returned message matches exactly.

---

### **2. `test_create_task`**
- **Route:** `POST /tasks/`
- **Purpose:** Tests creating a new task.
- **Request Body Example:**
  ```json
  {
    "title": "Test Task",
    "description": "This is a test task",
    "completed": false
  }
  ```
- **Criteria:** Passes if the response status is `200 OK` and the returned task matches the request body.

---

### **3. `test_get_tasks`**
- **Route:** `GET /tasks/`
- **Purpose:** Tests retrieving all tasks.
- **Criteria:** Passes if the response status is `200 OK` and all tasks are returned in the correct order.

---

### **4. `test_update_task`**
- **Route:** `PUT /tasks/{task_id}/`
- **Purpose:** Tests updating a task.
- **Request Body Example:**
  ```json
  {
    "title": "Updated Task",
    "description": "Updated description",
    "completed": true
  }
  ```
- **Criteria:** Passes if the task is updated correctly and the updated values are returned.

---

### **5. `test_delete_task`**
- **Route:** `DELETE /tasks/{task_id}/`
- **Purpose:** Tests deleting a task by ID.
- **Criteria:** Passes if the response status is `200 OK` and a success message is returned:
  ```json
  {"message": "Task {task_id} deleted successfully"}
  ```

---

## **Running the Tests Locally**

### **Run All Tests**
To run all tests inside the Vagrant environment:
```bash
poetry run pytest tests/ --maxfail=1 --disable-warnings
```

### **Run a Specific Test**
To run a specific test, use:
```bash
poetry run pytest -k "test_create_task"
```

---

## **Automated Testing in GitHub Actions**

Your code will be automatically tested using **GitHub Actions** when you push to the `main` or any development branch. Follow these steps to ensure your tests pass:

### **1. Commit and Push Code**
Ensure your changes are committed and pushed to GitHub:
```bash
git add .
git commit -m "Implemented CRUD endpoints"
git push origin main
```

### **2. Check GitHub Actions**
1. Navigate to your GitHub repository.
2. Click the [**Actions**](images/github_actions_tab.png) tab.
3. Review the latest workflow run to see if your tests [passed](images/successful_action.png).

If your tests fail, click on the failed job to see the detailed error logs.

---

## **Manual Testing with `cURL` (Optional)**
You can manually test your API using **`cURL`** from your local machine (outside the Vagrant box):

### **1. Get Welcome Message (`GET /`)**
```bash
curl -X GET "http://localhost:8000/"
```

### **2. Create a New Task (`POST /tasks/`)**
```bash
curl -X POST "http://localhost:8000/tasks/" -H "Content-Type: application/json" -d '{"title": "Test Task", "description": "Test description", "completed": false}'
```

### **3. Get All Tasks (`GET /tasks/`)**
```bash
curl -X GET "http://localhost:8000/tasks/" -H "accept: application/json"
```

### **4. Update a Task (`PUT /tasks/{task_id}/`)**
```bash
curl -X PUT "http://localhost:8000/tasks/1/" \
-H "Content-Type: application/json" \
-d '{
  "title": "Updated Task Title",
  "description": "Updated task description",
  "completed": true
}'
```

### **5. Delete a Task (`DELETE /tasks/{task_id}/`)**
```bash
curl -X DELETE "http://localhost:8000/tasks/1/" -H "accept: application/json"
```

---

## **Submission Instructions**

1. Implement all endpoints (`GET`, `POST`, `PUT`, `DELETE`) in `server.py`.
2. Run the tests inside the Vagrant box to ensure all tests pass.
3. Push your code to the `main` branch of your GitHub repository.
4. Submit the GitHub repository link for grading.

---

## **Important Notes**

- Do **NOT** modify the `tests.py` file. Any modifications to the test file will result in a **0 score**.
- Ensure all dependencies are installed using:
  ```bash
  poetry install --with=dev
  ```
- If you encounter `ModuleNotFoundError`, set the `PYTHONPATH`:
  ```bash
  export PYTHONPATH="/home/vagrant/app"
  ```

---

## **Grading Example**

If you pass the following tests:
- `test_read_root` ✅
- `test_create_task` ✅
- `test_get_tasks` ✅
- `test_update_task` ❌
- `test_delete_task` ❌

Your score is:
```
3 points x 3 tests passed = 9/15 points
```
