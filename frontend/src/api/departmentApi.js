import api from "./axios";

export const getDepartments = async () => {
    const { data } = await api.get("/departments");
    return data;
};

export const getDepartment = async (id) => {
    const { data } = await api.get(`/departments/${id}`);
    return data;
};