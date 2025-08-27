import React, {useState} from 'react';
import "../styles/NavBar.css"


const NavBar = () => {
    const [visiable, setVisiable] = useState<boolean | null>(false)

    return (
        <nav className="navbar">
            <div className="navbar-left">
                <a href="/" className="logo">
                Toronto Permit Tracker
                </a>
            </div>
            <div className="navbar-center">
                <ul className="nav-links">
                    <li>
                        <a href="/map">Map</a>
                    </li>
                    <li>
                        <a href="/stats">Stats</a>
                    </li>
                    <li>
                        <a href="/about">About</a>
                    </li>
                </ul>
            </div>
            <div className="navbar-right">
                <a href="/help" className="help-icon">
                Help
                </a>
            </div>
        </nav>
    );
};

export default NavBar;