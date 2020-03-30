<h1 align="center">Pickee | MadStax</h1> 

This project is part of the University of Glasgow MSc in Software Development Internet Technology coursework. It consists of a backend application written in Python (Django) with a multi-page frontend application written in JavaScript (Vue.js).

### Environment Setup

The project takes advantage of [poetry](https://github.com/python-poetry/poetry) dependency management tool to configure a virtual environment and the pertinent dependencies. Please make sure you have correctly installed the following technologies globally in your machine before you proceed.

- [Yarn 1.22.0](https://classic.yarnpkg.com/en/docs/install/#mac-stable)
- [Python 3.7.6](https://www.python.org/downloads/release/python-376/)
- [Poetry 1.0.3](https://github.com/python-poetry/poetry)
- [Vue.js 2.6.11](https://vuejs.org/v2/guide/installation.html)
- [Vue CLI 4.2.2](https://cli.vuejs.org/guide/installation.html)

**Automated setup**
MadStax provides you with a beautiful automagical setup script!
If you want us to lift up everything for you simply navigate to he project's root directory and run the following command:<br>
    ```python setup.py```<br><br>

**Make sure you use `yarn` instead of `npm` to install Vue.js and Vue CLI**

### Manual local setup (development)

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
    **Note**: you can also chose to run `yarn build` instead of `serve`. In this case, new static files will be generated for you and you won't need to have a dedicated terminal serving frontend-related resources.<br><br>

8. Run the backend application<br><br>
    ```cd ..```<br><br>
    ```./manage.py runserver```<br><br>

9. Access the App's entry point at http://127.0.0.1:8000/<br><br>

10. Enjoy!

### Final notes
The project can also be run by using your own `virtual environment tool` (such as Anaconda) or `pip`. In this case, you'll have to activate your virtual environment manually.