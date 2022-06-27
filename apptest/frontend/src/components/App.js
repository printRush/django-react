import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';

import Header from './layout/Header';
import Dashboard from './Test/Dashboard';

class App extends Component {
    render() {
        return (
            <Fragment>
                <Header />
                <Dashboard />
            </Fragment>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));

// npm run dev + fix <fragment>
