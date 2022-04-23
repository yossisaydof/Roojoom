## Roojoom Full-stack developer test ##

### Installation ###
Open terminal in your workplace folder and type:

1. ```sh
   git clone git@github.com:yossisaydof/Roojoom.git ./test_project
   ```
2. Enter ```test_project``` folder with:
    ```sh 
    cd test_project
    ```
3. Install requirements.txt with:
   ```sh 
    pip install -r requirements.txt
    ```
4. Enter ```src``` folder with:
    ```sh 
    cd src
    ```
5. Run these lines (one by one):
   ```sh 
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py runserver
   ```
6. Go to: http://127.0.0.1:8000/


### Report a problem: ###
1. At the homepage press on `Report a problem`
2. Enter the following information about your problem
3. Press `Report`
4. Now the response will appear
