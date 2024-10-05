from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
# only if you run this main.py file directly it should run
# if you import it into some other program it won't run
# if we didn't have this line, then it would run even if this file was imported into another program. Which is usually not preferable.
# debug=True means anytime we change the code, it will automatically rerun the code and web server.
# you usually turn it off when running in production.