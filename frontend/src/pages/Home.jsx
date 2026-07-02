import { Link } from 'react-router-dom';

const [blocks, setBlocks] = useState([]);
useEffect(() => {

    getBuildings()
        .then(setBlocks)
        .catch(console.error);

}, []);



function Home() {
  return (
    <div className="page-shell">
      <header className="topbar">
        <div className="brand">
          <div className="brand-mark">F</div>
          <div>
            <p className="brand-title">FindMyClass</p>
            <p className="brand-subtitle">Campus Navigator</p>
          </div>
        </div>
        <nav className="nav-links" aria-label="Primary navigation">
          <a href="#home">Home</a>
          <a href="#blocks">Blocks</a>
          <a href="#explore">Explore</a>
          <a href="#support">Support</a>
        </nav>
      </header>

      <main id="home">
        <section className="hero-card">
          <div className="hero-copy">
            <p className="eyebrow">VVIT Campus</p>
            <h1>Find your next class in seconds.</h1>
            <p className="hero-text">
              Search by course name, code, room number, or instructor and reach the right building without confusion.
            </p>
            <Link to="/search" className="search-box">
              <input type="text" placeholder="e.g. CS201, A Block, Dr. Aruna..." readOnly />
              <button type="button">Search</button>
            </Link>
          </div>
          <div className="hero-visual" aria-hidden="true">
            <div className="visual-ring" />
            <div className="visual-card">
              <p>Live campus guide</p>
              <strong>Fast directions</strong>
              <span>From blocks to labs</span>
            </div>
          </div>
        </section>

        <section className="section-block" id="blocks">
          <div className="section-heading">
            <p className="eyebrow">Campus layout</p>
            <h2>Explore the major buildings on campus</h2>
          </div>
          <div className="cards-grid">
            {blocks.map((block) => (
              <Link key={block.slug} to={`/block/${block.slug}`} className="block-card">
                <img src={block.image} alt={block.name} className="block-image" />
                <div className="block-card-content">
                  <div className="block-icon">{block.shortName}</div>
                  <div>
                    <h3>{block.name}</h3>
                    <p>{block.floors} floors · {block.room_count} rooms</p>
                  </div>
                </div>
              </Link>
            ))}
          </div>
        </section>

      </main>

      <footer className="footer" id="support">
        <p>Built for students who want a faster campus experience.</p>
      </footer>
    </div>
  );
}

export default Home;
