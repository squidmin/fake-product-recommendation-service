# fake-product-recommendation-service

Companion repo for the `RecommendationController` in the [`java-spring-reactive-web-reference`](https://github.com/squidmin/java-spring-reactive-web-reference) project.\
Generates ✨fake product data✨.

## Installation

### 1. Install Python

You can install Python using `pyenv` on macOS or Linux. On Windows, you can use `pyenv-win`.

### 2. Install dependencies

You can install the dependencies using `pip` and the `requirements.txt` file.

```shell
pip3 install -r requirements.txt
```

### 3. Run the application

You can run the application using `uvicorn`.

```shell
uvicorn main:app --reload
```

The `--reload` flag enables hot reloading so the server will automatically reload when you make changes to your code.

You should see output indicating that the server is running, typically on http://127.0.0.1:8000.
