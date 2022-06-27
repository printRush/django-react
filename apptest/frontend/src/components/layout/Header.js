import React, { Component } from 'react'

export class Header extends Component {
    render() {
        return (
            <nav className="navbar navbar-expand-sm bg-light">
                <div className="container-fluid">
                    <a className="navbar-brand" href="#">APPLICATION FOR TESTS</a>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
                        <div class="navbar-nav">
                        </div>
                    </div>
                </div>
            </nav>
        )
    }
}

export default Header
