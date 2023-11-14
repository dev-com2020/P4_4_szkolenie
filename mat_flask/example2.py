import os

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template

matplotlib.use('Agg')


app = Flask(__name__)


def get_plot():
    data = {
        'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)
    }
    data['b'] = data['a'] + 10 * np.random.randn(50)
    data['d'] = np.abs(data['d']) * 100

    plt.scatter('a', 'b', c='c', s='c', data=data)
    plt.xlabel('X')
    plt.ylabel('Y')
    return plt


@app.get('/')
def single_converter():
    plot = get_plot()
    plot.savefig(os.path.join('static', 'images', 'plot2.png'))
    return render_template('matplotlib-plot2.html')


if __name__ == '__main__':
    app.run(debug=True)
