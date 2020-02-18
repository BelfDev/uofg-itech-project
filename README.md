<h1 align="center">Pickee | MadStax</h1> 

This project is part of the University of Glasgow MSc in Software Development Internet Technology coursework. It consists of a backend application written in Python (Django) with a multi-page frontend application written in JavaScript (Vue.js).

### Environment Setup

The project takes advantage of [poetry](https://github.com/python-poetry/poetry) dependency management tool to configure a virtual environment and the pertinent dependencies. Please make sure you have correctly installed the following technologies globally in your machine before you proceed.

- [Yarn 1.22.0](https://classic.yarnpkg.com/en/docs/install/#mac-stable)
- [Python 3.7.6](https://www.python.org/downloads/release/python-376/)
- [Poetry 1.0.3](https://github.com/python-poetry/poetry)
- [Vue.js 2.6.11](https://vuejs.org/v2/guide/installation.html)
- [Vue CLI 4.2.2](https://cli.vuejs.org/guide/installation.html)

**Make sure you use `yarn` instead of `npm` to install Vue.js and Vue CLI**

### Running the project (for the first time)

1. Select your preferred directory and clone this repo <br><br> 
    ```git clone git@github.com:BelfDev/uofg-itech-project.git```<br><br>

2. Enter the project directory<br><br>
    ```cd uofg-itech-project```<br><br>

3. Initiate a virtual environment<br><br>
    ```poetry shell```<br><br>

4. Install the backend dependencies<br><br>
    ```poetry install```<br><br>

5. Go to the frontend application<br><br>
    ```cd pickee_frontend```<br><br>

6. Install the frontend dependencies<br><br>
   ```yarn install```<br><br>

**The steps below should be repeated every time you come back to the project**<br><br>

7. Run the frontend application<br><br>
    ```yarn serve```<br><br>

8. Run the backend application<br><br>
    ```cd ..```<br><br>
    ```./manage.py runserver```<br><br>

9. Access the App's entry point at http://127.0.0.1:8000/<br><br>

10. Enjoy!
