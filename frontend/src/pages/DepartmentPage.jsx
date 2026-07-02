import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getDepartment } from "../api/axios";

function DepartmentPage() {

    const { id } = useParams();

    const [department, setDepartment] = useState(null);

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        getDepartment(id)
            .then((response) => {
                setDepartment(response.data);
                setLoading(false);
            })
            .catch((error) => {
                console.error(error);
                setLoading(false);
            });

    }, [id]);

    if (loading) {
        return <h2>Loading...</h2>;
    }

    if (!department) {
        return <h2>Department not found.</h2>;
    }

    return (
        <div className="container mt-4">

            <h2>{department.name}</h2>

            <hr />

            <p>
                <strong>Department Code:</strong>{" "}
                {department.code}
            </p>

            <p>
                <strong>Department ID:</strong>{" "}
                {department.id}
            </p>

        </div>
    );
}

export default DepartmentPage;