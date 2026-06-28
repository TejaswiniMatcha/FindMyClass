import api from "../api/axios";

export const getRooms = async () => {
    const response = await api.get("/rooms");
    return response.data;
};