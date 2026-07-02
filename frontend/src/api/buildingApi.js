import api from "./axios";

export const getBuildings = async () => {
    const { data } = await api.get("/buildings");
    return data;
};

export const getBuilding = async (slug) => {
    const { data } = await api.get(`/buildings/${slug}`);
    return data;
};