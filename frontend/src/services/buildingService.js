import api from "../api/axios";

export const getBuildings = async () => {
    const response = await api.get("/buildings");
    return response.data;
};