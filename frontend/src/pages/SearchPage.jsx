import { useState, useEffect, useRef } from "react";
import { Link, useNavigate } from "react-router-dom";

import { searchCampus, searchCampusSuggestions } from "../api/searchApi";

function SearchPage() {
    const [query, setQuery] = useState("");
    const [year, setYear] = useState("");
    const [results, setResults] = useState([]);
    const [suggestions, setSuggestions] = useState([]);
    const [activeIndex, setActiveIndex] = useState(-1);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");
    const [isListening, setIsListening] = useState(false);
    const [speechSupported, setSpeechSupported] = useState(false);

    const recognitionRef = useRef(null);
    const navigate = useNavigate();

    const years = ["1st", "2nd", "3rd", "4th"];

    const normalizeYearFilter = (items) => {
        if (!year) return items;
        return items.filter((item) => {
            if (item.type === "Section") {
                return item.subtitle.toLowerCase().includes(year.toLowerCase());
            }
            return true;
        });
    };

    useEffect(() => {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (!SpeechRecognition) {
            setSpeechSupported(false);
            return;
        }

        setSpeechSupported(true);
        const recognition = new SpeechRecognition();
        recognition.lang = "en-US";
        recognition.interimResults = false;
        recognition.maxAlternatives = 1;

        recognition.onresult = (event) => {
            const phrase = event.results?.[0]?.[0]?.transcript;
            if (phrase) {
                setQuery(phrase);
            }
            setIsListening(false);
        };

        recognition.onend = () => setIsListening(false);
        recognition.onerror = () => setIsListening(false);
        recognitionRef.current = recognition;
    }, []);

    useEffect(() => {
        if (!query.trim() || query.trim().length < 2) {
            setSuggestions([]);
            return;
        }

        const timeout = setTimeout(async () => {
            try {
                const data = await searchCampusSuggestions(query, 8);
                setSuggestions(normalizeYearFilter(data));
            } catch {
                setSuggestions([]);
            }
        }, 250);

        return () => clearTimeout(timeout);
    }, [query, year]);

    const handleSearch = async () => {
        if (!query.trim()) {
            setError("Please enter a search term.");
            setResults([]);
            return;
        }

        setLoading(true);
        setError("");
        setSuggestions([]);

        try {
            let data = await searchCampus(query);
            data = normalizeYearFilter(data);
            setResults(data);
        } catch {
            setError("Unable to search right now.");
            setResults([]);
        } finally {
            setLoading(false);
        }
    };

    const handleVoiceClick = () => {
        if (!speechSupported || !recognitionRef.current) {
            return;
        }

        if (isListening) {
            recognitionRef.current.stop();
            setIsListening(false);
            return;
        }

        setIsListening(true);
        recognitionRef.current.start();
    };

    const handleSuggestionSelect = (item) => {
        setQuery(item.title);
        setSuggestions([]);
        navigate(item.route);
    };

    const handleInputKeyDown = (e) => {
        if (e.key === "ArrowDown") {
            e.preventDefault();
            setActiveIndex((current) => Math.min(current + 1, suggestions.length - 1));
            return;
        }

        if (e.key === "ArrowUp") {
            e.preventDefault();
            setActiveIndex((current) => Math.max(current - 1, 0));
            return;
        }

        if (e.key === "Escape") {
            setSuggestions([]);
            setActiveIndex(-1);
            return;
        }

        if (e.key === "Enter") {
            if (activeIndex >= 0 && suggestions[activeIndex]) {
                e.preventDefault();
                handleSuggestionSelect(suggestions[activeIndex]);
                return;
            }

            handleSearch();
        }
    };

    const activeSuggestion = suggestions[activeIndex] || null;
    const resultCount = results.length;

    const resultsSummary = () => {
        if (!query.trim()) return null;

        if (loading) {
            return <p className="results-summary">Searching campus content, please wait...</p>;
        }

        if (!loading && !error && resultCount === 0) {
            return (
                <p className="results-summary">
                    No results found for <strong>“{query}”</strong>. Try broader terms or remove the year filter.
                </p>
            );
        }

        if (resultCount > 0) {
            return (
                <div className="results-summary">
                    <div>
                        <p className="results-count">{resultCount} results</p>
                        <p className="results-subtitle">Showing the most relevant campus locations.</p>
                    </div>
                    <p className="results-status">Refine with building names, room numbers, faculty, or section codes.</p>
                </div>
            );
        }

        return null;
    };

    return (
        <div className="page-shell small-shell">
            <div className="detail-card">
                <Link to="/" className="back-link">
                    ← Back Home
                </Link>

                <div className="detail-header">
                    <div>
                        <p className="eyebrow">Search</p>
                        <h1>Find Anything on Campus</h1>
                        <p className="hero-text">
                            Search buildings, rooms, departments, faculty members and sections.
                        </p>
                    </div>
                </div>

                <div className="search-panel">
                    <div className="search-controls">
                        <div className="search-field">
                            <input
                                value={query}
                                placeholder="Search campus by building, room, faculty, or section..."
                                onChange={(e) => {
                                    setQuery(e.target.value);
                                    setActiveIndex(-1);
                                }}
                                onKeyDown={handleInputKeyDown}
                                aria-label="Search campus"
                            />
                            {speechSupported && (
                                <button
                                    type="button"
                                    className={`voice-button ${isListening ? "listening" : ""}`}
                                    onClick={handleVoiceClick}
                                    aria-label={isListening ? "Stop voice search" : "Start voice search"}
                                >
                                    {isListening ? "🎙️ Listening" : "🎤"}
                                </button>
                            )}
                        </div>

                        <select value={year} onChange={(e) => setYear(e.target.value)}>
                            <option value="">All Years</option>
                            {years.map((y) => (
                                <option key={y} value={y}>
                                    {y} Year
                                </option>
                            ))}
                        </select>

                        <button className="search-button" onClick={handleSearch}>
                            {loading ? "Searching..." : "Search"}
                        </button>
                    </div>

                    {suggestions.length > 0 && (
                        <div className="autocomplete-list" role="listbox">
                            {suggestions.map((item, index) => (
                                <button
                                    key={`${item.type}-${item.id}`}
                                    type="button"
                                    className={`suggestion-item ${index === activeIndex ? "active" : ""}`}
                                    onClick={() => handleSuggestionSelect(item)}
                                    onMouseEnter={() => setActiveIndex(index)}
                                    role="option"
                                    aria-selected={index === activeIndex}
                                >
                                    <span className="suggestion-title">{item.title}</span>
                                    <span className="suggestion-meta">{item.subtitle}</span>
                                    <span className="suggestion-type">{item.type}</span>
                                </button>
                            ))}
                        </div>
                    )}
                </div>

                {error && <p className="hero-text">{error}</p>}

                {resultsSummary()}

                <div className="results-list" aria-live="polite">
                    {!loading && query && results.length === 0 && !error && (
                        <p>No results found.</p>
                    )}

                    {results.map((item) => (
                        <Link
                            key={`${item.type}-${item.id}`}
                            to={item.route}
                            className="result-item"
                            style={{ textDecoration: "none", color: "inherit" }}
                        >
                            <div>
                                <h3>{item.title}</h3>
                                <p>{item.subtitle}</p>
                            </div>
                            <span className="tag">{item.type}</span>
                        </Link>
                    ))}
                </div>
            </div>
        </div>
    );
}

export default SearchPage;