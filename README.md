FunnelBeam testing services Documentation
-----------------------------------
This project is for FunnelBeam project testing


# 1. Project Structure
This project consists of the following components:
- __app__
    
    This is the main component of the project, it consists of all main sub-modules of the project. These modules are used to handle data, manage connections from client.
    - modules
        - common
    - settings
    - utils
    - apis.py
    - app.py
- __test__
- __README.md__
- __manage.py__
- __requirements.txt__
- __.gitignore__

# 2. Deployment
## 2.1. Minimum Requirements (main libraries)
```yaml
- flask
- flask-restx
- flask-sqlalchemy
- flask-testing
```


## 2.2. Deployment

- Install miniconda, download [here](https://docs.conda.io/en/latest/miniconda.html).

E.g, For Linux distribution:
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```
- Create conda environment and activate it:
```bash
conda create --name <env_name>
conda activate <env_name>
```
- Install required dependencies:

```bash
pip install -r requirements.txt
```
- Run project:
```bash
python manage.py
```

**Notes**: 
- To run project in the background of development mode, you should use [**`tmux`**](https://gist.github.com/ladin157/d2f6bfa09df584ec13f3f6e2055952b7) to manage processes.
- To run in production mode:
  - Database params should be stored in enviroment variables.
  - uWSGI/Unicorn + Nginx are used to deploy.

# 3. Testing
- Unittest files are stored in folder `test`
  - To test authentication, use `test_auth.py`
  - To test phone, use `test_phone.py`
- To test API, we use the Postman to connect and test. The collection is available [here](https://www.getpostman.com/collections/57a103e84d459b2f6015) 
  - The API is live served [here](http://159.65.13.232:3000/) (It is available for testing through Browser).
  - Authentication:
    - Admin account: `admin@gmail.com/1`
    - Normal account: `test@gmail.com/1`

# 3. Tips
- Install all dependencies in Linux distribution before installing the packages to avoiding errors during installation.
- If you get any trouble while installing a dependency, install it separately using conda.
```bash
conda install <package_name>
``` 
- Each service is running under `tmux` process.
