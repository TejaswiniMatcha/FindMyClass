import { useState } from 'react';
import { Link } from 'react-router-dom';
import { searchCampus } from '../api/axios.js';

function SearchPage() {
  const [query, setQuery] = useState('');
  const [year, setYear] = useState(''); // Add year filter
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const years = ['1st', '2nd', '3rd', '4th'];

  const handleSearch = async () => {
    if (!query.trim()) {
      setResults([]);
      setError('Please enter a search term.');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const response = await searchCampus(query);
      let filteredResults = response.results || [];
      
      // Filter by year if selected
      if (year) {
        filteredResults = filteredResults.filter(item => {
          if (item.type === 'Section') {
            return item.subtitle.includes(year);
          }
          return true;
        });
      }
      
      setResults(filteredResults);
    } catch (err) {
      setError('Unable to reach the backend right now.');
      setResults([]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-shell small-shell">
      <div className="detail-card">
        <Link to="/" className="back-link">← Back home</Link>
        <div className="detail-header">
          <div>
            <p className="eyebrow">Search experience</p>
            <h1>Find classrooms, sections, and departments</h1>
            <p className="hero-text">
              Use this hub to discover classrooms, sections by year, faculty spaces, and campus resources.
            </p>
          </div>
        </div>

        <div className="search-panel">
          <div style={{ display: 'flex', gap: '10px', marginBottom: '10px' }}>
            <input
              type="text"
              placeholder="Search by room, block, section, or department"
              value={query}
              onChange={(event) => setQuery(event.target.value)}
              onKeyDown={(event) => event.key === 'Enter' && handleSearch()}
              style={{ flex: 1 }}
            />
            <select 
              value={year} 
              onChange={(event) => setYear(event.target.value)}
              style={{ padding: '8px 12px', borderRadius: '4px', border: '1px solid #ccc' }}
            >
              <option value="">All Years</option>
              {years.map((y) => (
                <option key={y} value={y}>{y} Year</option>
              ))}
            </select>
            <button type="button" onClick={handleSearch}>
              {loading ? 'Searching…' : 'Go'}
            </button>
          </div>
        </div>

        {error && <p className="hero-text">{error}</p>}

        <div className="results-list">
          {!loading && results.length === 0 && !error && query && (
            <p className="hero-text">No results found.</p>
          )}

          {results.map((item) => (
            <div key={item.id} className="result-item">
              <div>
                <h3>{item.title}</h3>
                <p>{item.subtitle}</p>
              </div>
              <span className="tag">{item.type}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default SearchPage;
