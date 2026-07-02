import api from "./axios";

export const getFaculties = async () => {
    const { data } = await api.get("/faculties");
    return data;
};

export const getFaculty = async (id) => {
    const { data } = await api.get(`/faculties/${id}`);
    return data;
};