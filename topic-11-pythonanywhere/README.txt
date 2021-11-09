PythonAnywhere quick notes

1. Get an account at PythonAnywhere
   - Custom account
   - Put all choices as low as possible
   - Increase web apps to -2-
   - This should cost $7/mo

3. Log in to console

--- Create the dev copy ---

1. Create ~/projects/<app>
2. Create web app at URL: <app>-dev-<account>.pythonanywhere.com
    - Select the appropriate app type and python version
    - Point the web app at /home/<account>/projects/<app>/<server-file>.py
    - Set source and working directory to /home/<account>/projects/<app>
    - Set /static/ to /home/<account>/projects/<app>/static
3. Go to ~/projects ($ cd ~/projects)
4. Remove app directory ($ rm -rf <app>)
5. Clone your repo ($ git clone <app-repo-ssh-string>)
6. Go to the web page and refresh the app

--- Create the production copy (optional) ---

1. Create ~/sites/<app>
2  Create web app at URL: <app>-<account>.pythonanywhere.com
    - Select the appropriate app type and python version
    - Point the web app at /home/<account>/sites/<app>/<server-file>.py
    - Set source and working directory to /home/<account>/sites/<app>
    - Set /static/ to /home/<account>/sites/<app>/static
3. Go to ~/sites ($ cd ~/sites)
4. Remove app directory ($ rm -rf <app>)
5. Clone your repo ($ git clone <app-repo-ssh-string>)
6. Go to the web page and refresh the app

--- Edit the code

1. Go to the dev copy (~/projects/<app>)
2. Make changes
3. Refresh dev web app
4. Look at dev web app
5. When done, push to git origin  
    ($ git status)
    ($ git add all)
    ($ git commit -m <message>)
    ($ git push)

--- Deploy to production

1. Go to the production copy (~/sites/<app>)
2. Pull the origin code ($ git pull)