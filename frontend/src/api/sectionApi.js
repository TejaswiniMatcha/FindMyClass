import api from "./axios";

export const getSections = async () => {
    const { data } = await api.get("/sections");
    return data;
};

export const getSection = async (id) => {
    const { data } = await api.get(`/sections/${id}`);
    return data;
};