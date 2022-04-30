import argparse

from app import create_app

app = create_app(config='dev')
# app = create_app(config='prod')

# now we just run command to start server, without params like other python code. It might be attended later

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False, host='0.0.0.0', port=5001)
