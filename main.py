from website import create_app

app = create_app()

# only if run file, we'll import
# don't want to keep manually rerunning flask web server, so on
if __name__ == '__main__':
    app.run(debug=True)
