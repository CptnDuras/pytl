from app import app

# run on port 5000:
if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    except Exception as ex:
        print ex
