import { useState } from "react";
import { Link } from "react-router-dom";

import { searchCampus } from "../api/searchApi";

function SearchPage() {

    const [query, setQuery] = useState("");

    const [year, setYear] = useState("");

    const [results, setResults] = useState([]);

    const [loading, setLoading] = useState(false);

    const [error, setError] = useState("");

    const years = [
        "1st",
        "2nd",
        "3rd",
        "4th"
    ];

    async function handleSearch() {

        if (!query.trim()) {

            setError("Please enter a search term.");

            setResults([]);

            return;

        }

        setLoading(true);

        setError("");

        try {

            let data = await searchCampus(query);

            if (year) {

                data = data.filter((item) => {

                    if (item.type === "Section") {

                        return item.subtitle.includes(year);

                    }

                    return true;

                });

            }

            setResults(data);

        }

        catch {

            setError("Unable to search right now.");

            setResults([]);

        }

        finally {

            setLoading(false);

        }

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

                    <div>

                        <p className="eyebrow">

                            Search

                        </p>

                        <h1>

                            Find Anything on Campus

                        </h1>

                        <p className="hero-text">

                            Search buildings, rooms, departments, faculty members and sections.

                        </p>

                    </div>

                </div>

                <div className="search-panel">

                    <div
                        style={{
                            display: "flex",
                            gap: "10px",
                            marginBottom: "10px"
                        }}
                    >

                        <input
                            value={query}
                            placeholder="Search..."
                            onChange={(e) => setQuery(e.target.value)}
                            onKeyDown={(e) => {

                                if (e.key === "Enter") {

                                    handleSearch();

                                }

                            }}
                            style={{ flex: 1 }}
                        />

                        <select
                            value={year}
                            onChange={(e) => setYear(e.target.value)}
                        >

                            <option value="">

                                All Years

                            </option>

                            {years.map((y) => (

                                <option
                                    key={y}
                                    value={y}
                                >

                                    {y} Year

                                </option>

                            ))}

                        </select>

                        <button
                            onClick={handleSearch}
                        >

                            {loading ? "Searching..." : "Search"}

                        </button>

                    </div>

                </div>

                {error && (

                    <p className="hero-text">

                        {error}

                    </p>

                )}

                <div className="results-list">

                    {!loading &&
                        query &&
                        results.length === 0 &&
                        !error && (

                            <p>

                                No results found.

                            </p>

                        )}

                    {results.map((item) => (

                        <Link
                            key={`${item.type}-${item.id}`}
                            to={item.route}
                            className="result-item"
                            style={{
                                textDecoration: "none",
                                color: "inherit"
                            }}
                        >

                            <div>

                                <h3>

                                    {item.title}

                                </h3>

                                <p>

                                    {item.subtitle}

                                </p>

                            </div>

                            <span className="tag">

                                {item.type}

                            </span>

                        </Link>

                    ))}

                </div>

            </div>

        </div>

    );

}

export default SearchPage;