import { useMemo } from "react";

function MapPreview({ latitude, longitude, name }) {
  const mapSrc = useMemo(() => {
    if (!latitude || !longitude) return null;
    return `https://www.google.com/maps?q=${latitude},${longitude}&output=embed`;
  }, [latitude, longitude]);

  if (!latitude || !longitude) {
    return (
      <div className="map-preview empty">
        <p>Location data is not available for this building.</p>
      </div>
    );
  }

  return (
    <div className="map-preview">
      <iframe
        title={`Map preview for ${name}`}
        src={mapSrc}
        loading="lazy"
        allowFullScreen
      />
      <div className="map-actions">
        <a
          href={`https://www.google.com/maps/dir/?api=1&destination=${latitude},${longitude}`}
          target="_blank"
          rel="noreferrer"
          className="map-button"
        >
          Navigate with Google Maps
        </a>
      </div>
    </div>
  );
}

export default MapPreview;
