import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getFaculty } from "../api/axios";

function FacultyPage() {
    const { id } = useParams();

    const [faculty, setFaculty] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        getFaculty(id)
            .then((res) => {
                setFaculty(res.data);
                setLoading(false);
            })
            .catch(console.error);
    }, [id]);

    if (loading) return <h2>Loading...</h2>;

    return (
        <div className="container mt-4">
            <h2>{faculty.name}</h2>

            <hr />

            <p><strong>Email:</strong> {faculty.email}</p>

            <p><strong>Designation:</strong> {faculty.designation}</p>

            <p><strong>Department:</strong> {faculty.department.name}</p>

            <p>
                <strong>Room:</strong>{" "}
                {faculty.room.room_no}
            </p>

            <p>
                <strong>Building:</strong>{" "}
                {faculty.room.building.name}
            </p>
        </div>
    );
}

export default FacultyPage;