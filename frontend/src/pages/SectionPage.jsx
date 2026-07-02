import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getSection } from "../api/axios";

function SectionPage() {
    const { id } = useParams();

    const [section, setSection] = useState(null);

    useEffect(() => {
        getSection(id)
            .then((res) => setSection(res.data))
            .catch(console.error);
    }, [id]);

    if (!section) return <h2>Loading...</h2>;

    return (
        <div className="container mt-4">
            <h2>
                {section.name} ({section.year})
            </h2>

            <hr />

            <p>
                <strong>Department:</strong>{" "}
                {section.department.name}
            </p>

            <p>
                <strong>Room:</strong>{" "}
                {section.room.room_no}
            </p>

            <p>
                <strong>Building:</strong>{" "}
                {section.room.building.name}
            </p>
        </div>
    );
}

export default SectionPage;