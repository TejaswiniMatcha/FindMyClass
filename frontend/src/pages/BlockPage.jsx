import { Link, useParams } from 'react-router-dom';
import { blocks } from '../data/campusData';

function BlockPage() {
  const { slug } = useParams();
  

const [block, setBlock] = useState(null);

useEffect(() => {

    getBuilding(slug)
        .then(setBlock);

}, [slug]);

  if (!block) {
    return (
      <div className="page-shell small-shell">
        <div className="detail-card">
          <p className="eyebrow">Not found</p>
          <h1>That block is not available yet.</h1>
          <Link to="/" className="back-link">← Return home</Link>
        </div>
      </div>
    );
  }

  return (
    <div className="page-shell small-shell">
      <div className="detail-card">
        <Link to="/" className="back-link">← Back to campus map</Link>
        <div className="detail-header">
          <img src={block.image} alt={block.name} className="detail-image" />
          <div>
            <p className="eyebrow">Building profile</p>
            <h1>{block.name}</h1>
            <p className="hero-text">{block.description}</p>
          </div>
        </div>

        <div className="detail-stats">
          <div>
            <strong>{block.floors}</strong>
            <span>Floors</span>
          </div>
          <div>
            <strong>{block.rooms}</strong>
            <span>Rooms</span>
          </div>
          <div>
            <strong>5 min</strong>
            <span>Walk from main gate</span>
          </div>
        </div>

        <div className="detail-section">
          <h2>Highlights</h2>
          <ul>
            {block.highlights.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}

export default BlockPage;
