import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";

import { getBuilding } from "../api/buildingApi";

function BlockPage() {

    const { slug } = useParams();

    const [building, setBuilding] = useState(null);

    const [loading, setLoading] = useState(true);

    const [error, setError] = useState("");

    useEffect(() => {

        async function fetchBuilding() {

            try {

                const data = await getBuilding(slug);

                setBuilding(data);

            }

            catch {

                setError("Building not found.");

            }

            finally {

                setLoading(false);

            }

        }

        fetchBuilding();

    }, [slug]);

    if (loading) {

        return (

            <div className="page-shell">

                <h2>Loading building...</h2>

            </div>

        );

    }

    if (error || !building) {

        return (

            <div className="page-shell small-shell">

                <div className="detail-card">

                    <p className="eyebrow">

                        Not Found

                    </p>

                    <h2>

                        {error}

                    </h2>

                    <Link
                        to="/"
                        className="back-link"
                    >
                        ← Return Home
                    </Link>

                </div>

            </div>

        );

    }

    return (

        <div className="page-shell small-shell">

            <div className="detail-card">

                <Link
                    to="/"
                    className="back-link"
                >
                    ← Back Home
                </Link>

                <div className="detail-header">

                    <img
                        src={`http://127.0.0.1:8000/static/${building.image}`}
                        alt={building.name}
                        className="detail-image"
                    />

                    <div>

                        <p className="eyebrow">

                            Building Profile

                        </p>

                        <h1>

                            {building.name}

                        </h1>

                        <p className="hero-text">

                            {building.description}

                        </p>

                    </div>

                </div>

                <div className="detail-stats">

                    <div>

                        <strong>

                            {building.floors}

                        </strong>

                        <span>

                            Floors

                        </span>

                    </div>

                    <div>

                        <strong>

                            {building.room_count}

                        </strong>

                        <span>

                            Rooms

                        </span>

                    </div>

                    <div>

                        <strong>

                            {building.code}

                        </strong>

                        <span>

                            Block Code

                        </span>

                    </div>

                </div>

                <div className="detail-section">

                    <h2>

                        Highlights

                    </h2>

                    <ul>

                        {building.highlights.map((item) => (

                            <li key={item}>

                                {item}

                            </li>

                        ))}

                    </ul>

                </div>

            </div>

        </div>

    );

}

export default BlockPage;