import api from "./axios";

export const getRooms = async () => {
    const { data } = await api.get("/rooms");
    return data;
};

export const getRoom = async (id) => {
    const { data } = await api.get(`/rooms/${id}`);
    return data;
};