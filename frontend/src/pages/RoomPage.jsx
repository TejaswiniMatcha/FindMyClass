import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getRoom } from "../api/axios";

function RoomPage() {
    const { id } = useParams();

    const [room, setRoom] = useState(null);

    useEffect(() => {
        getRoom(id)
            .then((res) => setRoom(res.data))
            .catch(console.error);
    }, [id]);

    if (!room) return <h2>Loading...</h2>;

    return (
        <div className="container mt-4">
            <h2>Room {room.room_no}</h2>

            <hr />

            <p><strong>Floor:</strong> {room.floor}</p>

            <p>
                <strong>Building:</strong>{" "}
                {room.building.name}
            </p>
        </div>
    );
}

export default RoomPage;