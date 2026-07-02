import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

import { getBuildings } from "../api/buildingApi";

function Home() {

    const [buildings, setBuildings] = useState([]);

    const [loading, setLoading] = useState(true);

    const [error, setError] = useState("");

    useEffect(() => {

        async function fetchBuildings() {

            try {

                const data = await getBuildings();

                setBuildings(data);

            }

            catch {

                setError("Unable to load campus buildings.");

            }

            finally {

                setLoading(false);

            }

        }

        fetchBuildings();

    }, []);

    if (loading) {

        return (

            <div className="page-shell">

                <h2>Loading campus...</h2>

            </div>

        );

    }

    if (error) {

        return (

            <div className="page-shell">

                <h2>{error}</h2>

            </div>

        );

    }

    return (

        <div className="page-shell">

            <header className="topbar">

                <div className="brand">

                    <div className="brand-mark">

                        F

                    </div>

                    <div>

                        <p className="brand-title">

                            FindMyClass

                        </p>

                        <p className="brand-subtitle">

                            Campus Navigator

                        </p>

                    </div>

                </div>

                <nav className="nav-links">

                    <a href="#home">Home</a>

                    <a href="#blocks">Blocks</a>

                    <a href="#support">Support</a>

                </nav>

            </header>

            <main>

                <section className="hero-card">

                    <div className="hero-copy">

                        <p className="eyebrow">

                            VVIT Campus

                        </p>

                        <h1>

                            Find your next class in seconds.

                        </h1>

                        <p className="hero-text">

                            Search classrooms, faculty cabins, departments and sections.

                        </p>

                        <Link

                            to="/search"

                            className="search-box"

                        >

                            <input

                                readOnly

                                placeholder="Search..."

                            />

                            <button>

                                Search

                            </button>

                        </Link>

                    </div>

                </section>

                <section
                    className="section-block"
                    id="blocks"
                >

                    <div className="section-heading">

                        <p className="eyebrow">

                            Campus Buildings

                        </p>

                        <h2>

                            Explore the Campus

                        </h2>

                    </div>

                    <div className="cards-grid">

                        {buildings.map((building) => (

                            <Link
                                key={building.id}
                                to={`/block/${building.slug}`}
                                className="block-card"
                            >

                                <img

                                    src={`http://127.0.0.1:8000/static/${building.image}`}

                                    alt={building.name}

                                    className="block-image"

                                />

                                <div className="block-card-content">

                                    <div className="block-icon">

                                        {building.short_name}

                                    </div>

                                    <div>

                                        <h3>

                                            {building.name}

                                        </h3>

                                        <p>

                                            {building.floors} Floors • {building.room_count} Rooms

                                        </p>

                                    </div>

                                </div>

                            </Link>

                        ))}

                    </div>

                </section>

            </main>

            <footer
                className="footer"
                id="support"
            >

                <p>

                    Built for VVIT Students.

                </p>

            </footer>

        </div>

    );

}

export default Home;