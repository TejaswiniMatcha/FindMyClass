import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000",
});

// Existing APIs...

export const getFaculty = (id) =>
    api.get(`/faculties/${id}`);

export const getRoom = (id) =>
    api.get(`/rooms/${id}`);

export const getSection = (id) =>
    api.get(`/sections/${id}`);

export const getDepartment = (id) =>
    api.get(`/departments/${id}`);

export default api;